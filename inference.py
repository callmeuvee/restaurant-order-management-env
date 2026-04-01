"""
Inference Script for Restaurant Order Management Environment
"""

import os
from restaurant_env import RestaurantOrderEnv
from graders import grade_easy_task, grade_medium_task, grade_hard_task

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
HF_TOKEN = os.getenv("HF_TOKEN", "")

def run_baseline(difficulty="medium"):
    """Run baseline inference"""
    env = RestaurantOrderEnv(difficulty=difficulty)
    obs = env.reset()
    
    done = False
    step = 0
    total_reward = 0
    
    while not done and step < 50:
        action = 0
        obs, reward, done, info = env.step(action)
        total_reward += reward
        step += 1
    
    state = env.state()
    
    if difficulty == "easy":
        score = grade_easy_task(state)
    elif difficulty == "medium":
        score = grade_medium_task(state)
    else:
        score = grade_hard_task(state)
    
    return {
        "difficulty": difficulty,
        "completed": state['completed_orders'],
        "accuracy": state['on_time_accuracy'],
        "score": score,
        "total_reward": total_reward
    }

if __name__ == "__main__":
    for difficulty in ["easy", "medium", "hard"]:
        result = run_baseline(difficulty)
        print(f"\n{difficulty.upper()}: Score={result['score']:.2f}")
