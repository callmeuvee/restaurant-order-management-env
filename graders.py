def grade_easy_task(state):
    """Easy: on-time delivery target 60%"""
    accuracy = float(state.get("on_time_accuracy", 0.0))
    score = accuracy / 0.6 if accuracy > 0 else 0.0
    return float(max(0.0, min(score, 1.0)))

def grade_medium_task(state):
    """Medium: on-time (75%) + efficiency"""
    accuracy = float(state.get("on_time_accuracy", 0.0))
    completed = int(state.get("completed_orders", 0))
    total = int(state.get("total_orders", 1))
    efficiency = completed / total if total > 0 else 0.0
    
    # Weighted: 60% accuracy, 40% efficiency
    score = (min(accuracy / 0.75, 1.0) * 0.6) + (efficiency * 0.4)
    return float(max(0.0, min(score, 1.0)))

def grade_hard_task(state):
    """Hard: on-time (85%) + efficiency + fairness"""
    accuracy = float(state.get("on_time_accuracy", 0.0))
    completed = int(state.get("completed_orders", 0))
    total = int(state.get("total_orders", 1))
    avg_wait = float(state.get("avg_wait_time", 0.0))
    
    efficiency = completed / total if total > 0 else 0.0
    fairness = max(0.0, 1.0 - (avg_wait / 20.0))
    
    # Weighted: 50% accuracy, 30% efficiency, 20% fairness
    score = (min(accuracy / 0.85, 1.0) * 0.5) + (efficiency * 0.3) + (fairness * 0.2)
    return float(max(0.0, min(score, 1.0)))
