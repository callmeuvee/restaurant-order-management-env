def grade_easy_task(state):
    """Easy task grader"""
    accuracy = state["on_time_accuracy"]
    return float(min(max(accuracy / 0.6, 0.0), 1.0))

def grade_medium_task(state):
    """Medium task grader"""
    accuracy = state["on_time_accuracy"]
    return float(min(max(accuracy / 0.75, 0.0), 1.0))

def grade_hard_task(state):
    """Hard task grader"""
    accuracy = state["on_time_accuracy"]
    return float(min(max(accuracy / 0.85, 0.0), 1.0))
