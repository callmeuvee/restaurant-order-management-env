def grade_easy_task(state):
    """
    Easy task grader: Agent manages 10 orders with plenty of resources
    Target: 60% orders delivered on-time (within 10 min wait)
    """
    on_time = state.get("on_time_accuracy", 0.0)
    completed = state.get("completed_orders", 0)
    total = state.get("total_orders", 1)
    
    # Penalize if orders aren't completed
    completion_rate = completed / total if total > 0 else 0.0
    
    # Score: weighted average of on-time delivery and completion
    score = (on_time * 0.7 + completion_rate * 0.3)
    
    # Normalize: agent needs 60% on-time to get full score
    if on_time >= 0.6:
        final_score = min(1.0, score)
    else:
        final_score = on_time / 0.6 * score
    
    return max(0.0, min(float(final_score), 1.0))

def grade_medium_task(state):
    """
    Medium task grader: Agent manages 20 orders with moderate resources
    Target: 75% on-time + fair staff utilization
    """
    on_time = state.get("on_time_accuracy", 0.0)
    completed = state.get("completed_orders", 0)
    total = state.get("total_orders", 1)
    avg_wait = state.get("avg_wait_time", 0.0)
    
    completion_rate = completed / total if total > 0 else 0.0
    
    # Fairness penalty: long average wait times are bad
    fairness = max(0.0, 1.0 - (avg_wait / 20.0))
    
    # Weighted score: on-time (40%), completion (35%), fairness (25%)
    score = (on_time * 0.4 + completion_rate * 0.35 + fairness * 0.25)
    
    # Normalize to 75% target
    if on_time >= 0.75:
        final_score = min(1.0, score)
    else:
        final_score = (on_time / 0.75) * score
    
    return max(0.0, min(float(final_score), 1.0))

def grade_hard_task(state):
    """
    Hard task grader: Agent manages 40 orders with limited resources
    Target: 85% on-time + optimize staff utilization
    Penalties: long waits, incomplete orders
    """
    on_time = state.get("on_time_accuracy", 0.0)
    completed = state.get("completed_orders", 0)
    total = state.get("total_orders", 1)
    avg_wait = state.get("avg_wait_time", 0.0)
    
    completion_rate = completed / total if total > 0 else 0.0
    
    # Severe fairness penalty for high wait times
    fairness = max(0.0, 1.0 - (avg_wait / 30.0))
    
    # Weighted: on-time (50%), efficiency (30%), fairness (20%)
    score = (on_time * 0.5 + completion_rate * 0.3 + fairness * 0.2)
    
    # Normalize to 85% target (hardest)
    if on_time >= 0.85:
        final_score = min(1.0, score)
    else:
        final_score = (on_time / 0.85) * score
    
    return max(0.0, min(float(final_score), 1.0))
