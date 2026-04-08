def grade_easy_task(state):
    """Easy task grader: 60% on-time accuracy target"""
    accuracy = state["on_time_accuracy"]
    if accuracy >= 0.6:
        score = min(1, int(accuracy * 100) / 100)
    else:
        score = int(accuracy / 0.6 * 100) / 100
    return max(0, min(score, 1))

def grade_medium_task(state):
    """Medium task grader: balanced scoring"""
    accuracy = state["on_time_accuracy"]
    completed = state["completed_orders"]
    total = state["total_orders"]
    
    if total == 0:
        return 0
    
    efficiency = min(1, completed / total)
    accuracy_normalized = min(1, accuracy / 0.75)
    
    score = int((accuracy_normalized * 0.5 + efficiency * 0.5) * 100) / 100
    return max(0, min(score, 1))

def grade_hard_task(state):
    """Hard task grader: strict scoring"""
    accuracy = state["on_time_accuracy"]
    completed = state["completed_orders"]
    total = state["total_orders"]
    
    if total == 0:
        return 0
    
    efficiency = min(1, completed / total)
    accuracy_normalized = min(1, accuracy / 0.85)
    
    score = int((accuracy_normalized * 0.6 + efficiency * 0.4) * 100) / 100
    return max(0, min(score, 1))
