"""
Inference Script for Restaurant Order Management Environment
===================================
MANDATORY
- Before submitting, ensure the following variables are defined in your environment configuration:
    API_BASE_URL   The API endpoint for the LLM.
    MODEL_NAME     The model identifier to use for inference.
    HF_TOKEN       Your Hugging Face / API key.

- The inference script must be named `inference.py` and placed in the root directory of the project
- Participants must use OpenAI Client for all LLM calls using above variables

STDOUT FORMAT
- The script must emit exactly three line types to stdout, in this order:

    [START] task=<task_name> env=<benchmark> model=<model_name>
    [STEP]  step=<n> action=<action> reward=<0.00> done=<true|false> error=<msg|null>
    [END]   success=<true|false> steps=<n> score=<score> rewards=<r1,r2,...,rn>

  Rules:
    - One [START] line at episode begin.
    - One [STEP] line per step, immediately after env.step() returns.
    - One [END] line after env.close(), always emitted (even on exception).
    - reward and rewards are formatted to 2 decimal places.
    - done and success are lowercase booleans: true or false.
    - error is the raw error string, or null if none.
    - All fields on a single line with no newlines within a line.
    - Each task should return score in [0, 1]
"""

import os
import sys
import textwrap
from typing import List, Optional
from openai import OpenAI

from restaurant_env import RestaurantOrderEnv
from graders import grade_easy_task, grade_medium_task, grade_hard_task

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
HF_TOKEN = os.getenv("HF_TOKEN", "")

# Configuration
MAX_STEPS = 100
TEMPERATURE = 0.7
MAX_TOKENS = 150
SUCCESS_SCORE_THRESHOLD = 0.5

SYSTEM_PROMPT = textwrap.dedent(
    """
    You are controlling a restaurant kitchen environment.
    You must decide which order to cook next (0-39).
    Reply with exactly one number (the order index).
    """
).strip()


def log_start(task: str, env: str, model: str) -> None:
    """Log episode start"""
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]) -> None:
    """Log each step"""
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]) -> None:
    """Log episode end"""
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}", flush=True)


def get_model_action(client: OpenAI, step: int, obs: dict, history: List[str]) -> str:
    """Get action from LLM"""
    pending = obs.get("pending_orders", 0)
    completed = obs.get("completed_orders", 0)
    
    user_prompt = textwrap.dedent(f"""
        Step: {step}
        Pending orders: {pending}
        Completed orders: {completed}
        Average wait time: {obs.get('avg_wait_time', 0):.1f} min
        Previous steps:
        {chr(10).join(history[-3:]) if history else 'None'}
        Choose order index (0-{pending-1}) to cook next.
    """).strip()
    
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            stream=False,
        )
        text = (completion.choices[0].message.content or "").strip()
        # Extract first number from response
        for char in text:
            if char.isdigit():
                return char
        return "0"
    except Exception as exc:
        print(f"[DEBUG] Model request failed: {exc}", flush=True)
        return "0"


def run_episode(difficulty: str = "medium") -> None:
    """Run single episode"""
    client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)
    env = RestaurantOrderEnv(difficulty=difficulty)
    
    history: List[str] = []
    rewards: List[float] = []
    steps_taken = 0
    score = 0.0
    success = False
    
    log_start(task=difficulty, env="restaurant-order-management", model=MODEL_NAME)
    
    try:
        obs = env.reset()
        
        for step in range(1, MAX_STEPS + 1):
            # Get action from model
            action_str = get_model_action(client, step, obs, history)
            try:
                action = int(action_str)
            except ValueError:
                action = 0
            
            # Clamp action to valid range
            if len(env.pending_orders) > 0:
                action = max(0, min(action, len(env.pending_orders) - 1))
            else:
                break
            
            # Step environment
            obs, reward, done, info = env.step(action)
            
            rewards.append(reward)
            steps_taken = step
            error = None
            
            log_step(step=step, action=str(action), reward=reward, done=done, error=error)
            
            history.append(f"Step {step}: action={action} reward={reward:.2f}")
            
            if done:
                break
        
        # Calculate score
        state = env.state()
        if difficulty == "easy":
            score = grade_easy_task(state)
        elif difficulty == "medium":
            score = grade_medium_task(state)
        else:
            score = grade_hard_task(state)
        
        score = min(max(score, 0.0), 1.0)
        success = score >= SUCCESS_SCORE_THRESHOLD
    
    except Exception as e:
        print(f"[DEBUG] Episode error: {e}", flush=True)
        success = False
    
    finally:
        log_end(success=success, steps=steps_taken, score=score, rewards=rewards)


def main() -> None:
    """Run all difficulty levels"""
    for difficulty in ["easy", "medium", "hard"]:
        run_episode(difficulty=difficulty)
        print()  # Blank line between episodes


if __name__ == "__main__":
    main()
