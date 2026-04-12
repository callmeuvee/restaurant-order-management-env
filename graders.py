def grade_easy_task(state):
    """Easy task grader"""
    accuracy = state.get("on_time_accuracy", 0.0)
    score = float(accuracy) / 0.6 if accuracy > 0 else 0.0
    return float(max(0.0, min(score, 1.0)))

def grade_medium_task(state):
    """Medium task grader"""
    accuracy = state.get("on_time_accuracy", 0.0)
    score = float(accuracy) / 0.75 if accuracy > 0 else 0.0
    return float(max(0.0, min(score, 1.0)))

def grade_hard_task(state):
    """Hard task grader"""
    accuracy = state.get("on_time_accuracy", 0.0)
    score = float(accuracy) / 0.85 if accuracy > 0 else 0.0
    return float(max(0.0, min(score, 1.0)))
