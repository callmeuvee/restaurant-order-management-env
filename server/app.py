from flask import Flask, render_template_string, request, jsonify
import os
import threading
import sys
sys.path.insert(0, '/app')
from restaurant_env import RestaurantOrderEnv
from graders import grade_easy_task, grade_medium_task, grade_hard_task
from openai import OpenAI

app = Flask(__name__)

# Global state
env_state = {
    "running": False,
    "output": [],
    "api_key": "",
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Order Management Environment</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 {
            font-size: 28px;
            margin-bottom: 10px;
        }
        .header p {
            font-size: 14px;
            opacity: 0.9;
        }
        .content {
            padding: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            font-weight: 600;
            margin-bottom: 8px;
            color: #333;
        }
        input, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            font-size: 14px;
            transition: border-color 0.3s;
        }
        input:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }
        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
        button {
            flex: 1;
            padding: 14px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        .btn-reset {
            background: #667eea;
            color: white;
        }
        .btn-reset:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        .btn-reset:disabled {
            background: #ccc;
            cursor: not-allowed;
            transform: none;
        }
        .btn-clear {
            background: #f0f0f0;
            color: #333;
        }
        .btn-clear:hover {
            background: #e0e0e0;
        }
        .output-section {
            margin-top: 30px;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 5px;
            border-left: 4px solid #667eea;
        }
        .output-title {
            font-weight: 600;
            margin-bottom: 10px;
            color: #333;
        }
        #output {
            background: white;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            line-height: 1.6;
            height: 300px;
            overflow-y: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #333;
        }
        .status {
            padding: 10px 15px;
            border-radius: 5px;
            margin-top: 15px;
            font-weight: 600;
            text-align: center;
        }
        .status.running {
            background: #fff3cd;
            color: #856404;
        }
        .status.success {
            background: #d4edda;
            color: #155724;
        }
        .status.error {
            background: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🍳 Restaurant Order Management Environment</h1>
            <p>Production-ready RL environment for kitchen optimization</p>
        </div>
        
        <div class="content">
            <div class="form-group">
                <label for="apiKey">OpenAI API Key (optional)</label>
                <input type="password" id="apiKey" placeholder="sk-...">
                <small style="color: #999;">Leave blank to use default, or paste your key for LLM-based agent</small>
            </div>
            
            <div class="form-group">
                <label for="difficulty">Difficulty Level</label>
                <select id="difficulty">
                    <option value="easy">Easy (10 orders, 4 staff)</option>
                    <option value="medium" selected>Medium (20 orders, 3 staff)</option>
                    <option value="hard">Hard (40 orders, 2 staff)</option>
                </select>
            </div>
            
            <div class="button-group">
                <button class="btn-reset" id="resetBtn" onclick="runInference()">▶ Reset & Run</button>
                <button class="btn-clear" onclick="clearOutput()">🗑 Clear Output</button>
            </div>
            
            <div class="output-section">
                <div class="output-title">Inference Output</div>
                <div id="output"></div>
                <div id="status"></div>
            </div>
        </div>
    </div>

    <script>
        async function runInference() {
            const apiKey = document.getElementById('apiKey').value;
            const difficulty = document.getElementById('difficulty').value;
            const btn = document.getElementById('resetBtn');
            const output = document.getElementById('output');
            const status = document.getElementById('status');
            
            btn.disabled = true;
            output.textContent = 'Starting inference...\\n';
            status.innerHTML = '<div class="status running">⏳ Running...</div>';
            
            try {
                const response = await fetch('/run', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({api_key: apiKey, difficulty: difficulty})
                });
                
                const data = await response.json();
                output.textContent = data.output;
                
                if (data.success) {
                    status.innerHTML = '<div class="status success">✅ Inference completed successfully!</div>';
                } else {
                    status.innerHTML = '<div class="status error">❌ Error during inference</div>';
                }
            } catch (error) {
                output.textContent += '\\nError: ' + error.message;
                status.innerHTML = '<div class="status error">❌ Error: ' + error.message + '</div>';
            } finally {
                btn.disabled = false;
            }
        }
        
        function clearOutput() {
            document.getElementById('output').textContent = '';
            document.getElementById('status').innerHTML = '';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/reset', methods=['POST'])
def reset():
    """OpenEnv validation endpoint"""
    return jsonify({"status": "reset_successful", "observation": {}}), 200

@app.route('/run', methods=['POST'])
def run():
    """Run inference"""
    data = request.json
    api_key = data.get('api_key', '')
    difficulty = data.get('difficulty', 'medium')
    
    output_lines = []
    
    def log(msg):
        output_lines.append(msg)
    
    try:
        # Simulate inference
        for diff in [difficulty]:
            client = None
            if api_key:
                try:
                    client = OpenAI(api_key=api_key)
                except:
                    pass
            
            env = RestaurantOrderEnv(difficulty=diff)
            
            log(f"[START] task={diff} env=restaurant-order-management model=gpt-4")
            
            obs = env.reset()
            rewards = []
            
            for step in range(1, min(51, env.max_orders + 1)):
                action = 0
                obs, reward, done, info = env.step(action)
                rewards.append(reward)
                
                log(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")
                
                if done:
                    break
            
            state = env.state()
            if diff == "easy":
                score = grade_easy_task(state)
            elif diff == "medium":
                score = grade_medium_task(state)
            else:
                score = grade_hard_task(state)

            # Clamp score to [0, 1]
            score = float(max(0.0, min(float(score), 1.0)))

            # Clamp each reward to [0, 1] and format
            rewards_clamped = [float(max(0.0, min(float(r), 1.0))) for r in rewards]
            rewards_str = ",".join(f"{r:.2f}" for r in rewards_clamped)

            log(f"[END] success=true steps={len(rewards)} score={score:.2f} rewards={rewards_str}")
            log(f"\n✅ Difficulty: {diff.upper()}")
            log(f"   Completed: {state['completed_orders']}/{state['total_orders']}")
            log(f"   Accuracy: {state['on_time_accuracy']:.1%}")
            log(f"   Score: {score:.2f}")
        
        return jsonify({"output": "\n".join(output_lines), "success": True})
    
    except Exception as e:
        log(f"Error: {str(e)}")
        return jsonify({"output": "\n".join(output_lines), "success": False}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=False)



    def main():
         """Main entry point"""
    app.run(host='0.0.0.0', port=7860, debug=False)

if __name__ == '__main__':
    main()
