def grade_easy_task(state):
    """Easy task grader: 60% on-time accuracy target"""
    accuracy = state["on_time_accuracy"]
    score = 1 if accuracy >= 0.6 else 0
    return score

def grade_medium_task(state):
    """Medium task grader: 75% on-time accuracy"""
    accuracy = state["on_time_accuracy"]
    completed = state["completed_orders"]
    total = state["total_orders"]
    
    if total == 0:
        return 0
    
    efficiency = completed / total
    avg_score = (accuracy + efficiency) / 2
    
    score = 1 if avg_score >= 0.75 else 0
    return score

def grade_hard_task(state):
    """Hard task grader: 85% on-time accuracy"""
    accuracy = state["on_time_accuracy"]
    completed = state["completed_orders"]
    total = state["total_orders"]
    
    if total == 0:
        return 0
    
    efficiency = completed / total
    avg_score = (accuracy + efficiency) / 2
    
    score = 1 if avg_score >= 0.85 else 0
    return score
