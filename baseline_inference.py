from restaurant_env import RestaurantOrderEnv
from graders import grade_easy_task, grade_medium_task, grade_hard_task

def run_baseline(difficulty="medium", num_episodes=1):
    """Run baseline agent"""
    
    print(f"\n{'='*60}")
    print(f"BASELINE INFERENCE - {difficulty.upper()} DIFFICULTY")
    print(f"{'='*60}\n")
    
    env = RestaurantOrderEnv(difficulty=difficulty)
    
    for episode in range(num_episodes):
        print(f"Episode {episode + 1}:")
        obs = env.reset()
        
        done = False
        total_reward = 0
        step = 0
        max_steps = 50
        
        while not done and step < max_steps:
            # Simple baseline: cook orders in order (FIFO)
            if len(env.pending_orders) == 0:
                done = True
                break
            
            action = 0  # Always cook first order
            
            obs, reward, done, info = env.step(action)
            total_reward += reward
            step += 1
            
            if step % 10 == 0 or step == 1:
                print(f"  Step {step}: Reward={reward:.2f}, Orders Left={len(env.pending_orders)}")
        
        # Get final score
        state = env.state()
        
        if difficulty == "easy":
            score = grade_easy_task(state)
        elif difficulty == "medium":
            score = grade_medium_task(state)
        else:
            score = grade_hard_task(state)
        
        print(f"\n  Final Results:")
        print(f"  - Completed: {state['completed_orders']}")
        print(f"  - Accuracy: {state['on_time_accuracy']:.2%}")
        print(f"  - Avg Wait: {state['avg_wait_time']:.1f} min")
        print(f"  - Score: {score:.2f}\n")
    
    print(f"{'='*60}")
    print("BASELINE COMPLETE")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    # Run baselines for all difficulties
    for difficulty in ["easy", "medium", "hard"]:
        run_baseline(difficulty=difficulty, num_episodes=1)
