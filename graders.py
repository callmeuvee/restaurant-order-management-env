def grade_easy_task(state):
    """Easy task grader: 60% on-time accuracy"""
    accuracy = state["on_time_accuracy"]
    score = min(accuracy / 0.6, 1.0)
    return max(0.0, min(score, 1.0))

def grade_medium_task(state):
    """Medium task grader: 75% on-time accuracy + efficiency"""
    accuracy = state["on_time_accuracy"]
    completed = state["completed_orders"]
    total = state["total_orders"]
    
    if total == 0:
        return 0.0
    
    efficiency = completed / total
    avg_wait = state["avg_wait_time"]
    
    fairness = 1.0 if avg_wait <= 10 else max(0.0, 1.0 - (avg_wait - 10) / 20)
    
    score = (accuracy / 0.75 + efficiency + fairness) / 3
    return max(0.0, min(score, 1.0))

def grade_hard_task(state):
    """Hard task grader: 85% on-time accuracy + optimization"""
    accuracy = state["on_time_accuracy"]
    completed = state["completed_orders"]
    total = state["total_orders"]
    
    if total == 0:
        return 0.0
    
    efficiency = completed / total
    avg_wait = state["avg_wait_time"]
    
    staff_util = max(0.0, 1.0 - (avg_wait / 30))
    waste_penalty = 0.0
    
    score = (
        min(accuracy / 0.85, 1.0) * 0.4 +
        efficiency * 0.3 +
        staff_util * 0.2 +
        (1.0 - waste_penalty) * 0.1
    )
    
    return max(0.0, min(score, 1.0))
