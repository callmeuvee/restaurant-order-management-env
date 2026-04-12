def grade_easy_task(state):
    accuracy = float(state.get("on_time_accuracy", 0.0))
    score = max(0.001, min(0.999, accuracy))
    return float(score)

def grade_medium_task(state):
    accuracy = float(state.get("on_time_accuracy", 0.0))
    completed = int(state.get("completed_orders", 0))
    total = int(state.get("total_orders", 1))
    efficiency = completed / total if total > 0 else 0.0
    score = (min(accuracy / 0.75, 0.999) * 0.6) + (efficiency * 0.4)
    return float(max(0.001, min(0.999, score)))

def grade_hard_task(state):
    accuracy = float(state.get("on_time_accuracy", 0.0))
    completed = int(state.get("completed_orders", 0))
    total = int(state.get("total_orders", 1))
    avg_wait = float(state.get("avg_wait_time", 0.0))
    efficiency = completed / total if total > 0 else 0.0
    fairness = max(0.0, 1.0 - (avg_wait / 20.0))
    score = (min(accuracy / 0.85, 0.999) * 0.5) + (efficiency * 0.3) + (fairness * 0.2)
    return float(max(0.001, min(0.999, score)))
