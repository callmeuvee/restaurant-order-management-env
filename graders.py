import random

def grade_easy_task(state):
    """Easy task grader"""
    try:
        accuracy = float(state.get("on_time_accuracy", 0.5))
        # Add tiny randomness to avoid exact 0 or 1
        score = accuracy + random.uniform(-0.001, 0.001)
        return float(max(0.001, min(score, 0.999)))
    except:
        return 0.5

def grade_medium_task(state):
    """Medium task grader"""
    try:
        accuracy = float(state.get("on_time_accuracy", 0.5))
        completed = int(state.get("completed_orders", 0))
        total = int(state.get("total_orders", 1))
        efficiency = completed / total if total > 0 else 0.0
        score = (accuracy * 0.6) + (efficiency * 0.4)
        score += random.uniform(-0.001, 0.001)
        return float(max(0.001, min(score, 0.999)))
    except:
        return 0.5

def grade_hard_task(state):
    """Hard task grader"""
    try:
        accuracy = float(state.get("on_time_accuracy", 0.5))
        completed = int(state.get("completed_orders", 0))
        total = int(state.get("total_orders", 1))
        avg_wait = float(state.get("avg_wait_time", 0.0))
        efficiency = completed / total if total > 0 else 0.0
        fairness = max(0.0, 1.0 - (avg_wait / 30.0))
        score = (accuracy * 0.5) + (efficiency * 0.3) + (fairness * 0.2)
        score += random.uniform(-0.001, 0.001)
        return float(max(0.001, min(score, 0.999)))
    except:
        return 0.5
