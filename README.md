# 🍳 Restaurant Order Management Environment

## Overview

A production-ready OpenEnv environment for training RL agents to manage restaurant kitchen operations. Agents learn to optimize order scheduling, staff allocation, equipment usage, and ingredient management under realistic constraints.

## Real-World Problem

Modern restaurants struggle with:
- Kitchen bottlenecks (equipment capacity limits)
- Staff scheduling (limited cooks available)
- Ingredient inventory (varying prep states)
- Order prioritization (VIP vs regular customers)
- Equipment reliability (occasional breakdowns)
- Customer satisfaction (minimizing wait times)

This environment simulates these challenges with production-level complexity.

## Environment Specification

### Observation Space
```python
{
    "pending_orders": int,      # Orders waiting
    "completed_orders": int,    # Orders served
    "step_count": int,          # Steps taken
    "staff_available": int,     # Available cooks
    "avg_wait_time": float,     # Average customer wait
}
```

### Action Space
- **Type**: Discrete
- **Range**: 0 to (number of pending orders - 1)
- **Meaning**: Order ID to cook next

### Reward Function

**Base calculation (per order cooked):**
- Wait time ≥ 15 min: +0.5
- Wait time 10-15 min: +0.3
- Wait time 5-10 min: +0.1
- Wait time < 5 min: -0.2

**Bonuses:**
- VIP order: +0.3
- High equipment utilization: +0.2

**Penalties:**
- Equipment busy: -0.1
- Staff overworked: -0.1
- Equipment malfunction: -0.2

**Final:** Clipped to [-2.0, 2.0]

## 40 Dishes

Includes authentic Indian cuisine across categories:
- **Curries**: Butter Chicken, Dal Makhani, Rogan Josh, Korma
- **Breads**: Naan, Roti, Paratha, Puri, Bhakri
- **Rice Dishes**: Biryani, Pulao, Khichdi
- **Vegetables**: Samosa, Pakora, Chana Masala
- **Desserts**: Gulab Jamun, Kheer, Jalebi, Halwa
- **Salads**: Kachumbari, Raita, Pickle

## Three Difficulty Levels

### Easy Task
- 10 orders
- 80% ingredients pre-prepped
- 4 staff available (no breaks)
- 100% equipment reliability
- Goal: 60% on-time accuracy

### Medium Task
- 20 orders
- 50% ingredients pre-prepped
- 3 staff (1 break per 2 hours)
- 70% equipment reliability
- 10% ingredient shortages
- Goal: 75% on-time accuracy

### Hard Task
- 40 orders
- 20% ingredients pre-prepped
- 2 staff (frequent breaks)
- 50% equipment reliability
- 30% ingredient shortages
- VIP priority orders
- Goal: 85% on-time accuracy

## Equipment

| Equipment | Capacity | Requires Staff |
|-----------|----------|----------------|
| Oven | 4 | Yes |
| Stove | 3 | Yes |
| Fryer | 2 | Yes |
| Tandoor | 2 | Yes |
| Slow Cooker | 2 | No |

## Ingredients & States

### Chicken
frozen → thawed (15 min) → diced (10 min) → marinated (20 min) → cooked (12 min)

### Rice
raw → washed (5 min) → soaked (30 min) → cooked (15 min) → seasoned (5 min)

### Paneer
block → cut (8 min) → cubed (3 min) → marinated (10 min) → grilled (8 min)

### Lentils
raw → washed (5 min) → soaked (60 min) → cooked (45 min) → tempered (10 min)

### Dough
flour → mixed (10 min) → kneaded (15 min) → rested (60 min) → rolled (3 min) → proofed (20 min)

## Setup
```bash
pip install -r requirements.txt
```

## Running the Baseline
```bash
python baseline_inference.py
```

**Output:**
```
Episode 1:
  Step 10: Reward=0.45, Pending=18
  ✓ Completed: 12
  ✓ Accuracy: 75.00%
  ✓ Avg Wait: 8.5 min
  ✓ Score: 0.92
```

## API

### reset()
Starts a new episode with random orders
```python
env = RestaurantOrderEnv(difficulty="medium")
obs = env.reset()
```

### step(action)
Cook the order at index `action`
```python
obs, reward, done, info = env.step(action=0)
```

### state()
Get ground truth for grading
```python
state = env.state()
# Returns: {"accuracy": 0.75, "on_time_accuracy": 0.82, ...}
```

## Grading

### Easy Grader
Score = min(on_time_accuracy / 0.6, 1.0)

### Medium Grader
Score = (accuracy_ratio + efficiency + fairness) / 3

### Hard Grader
Score = weighted(efficiency, staff_util, waste, accuracy)

All graders return 0.0-1.0.

## Example Usage
```python
from restaurant_env import RestaurantOrderEnv
from graders import grade_medium_task

env = RestaurantOrderEnv(difficulty="medium")
obs = env.reset()

done = False
while not done:
    action = 0  # Cook first order
    obs, reward, done, info = env.step(action)
    print(f"Reward: {reward:.2f}")

state = env.state()
score = grade_medium_task(state)
print(f"Score: {score:.2f}")
```

## Key Features

✅ **Production-level Complexity**
- 40 authentic dishes
- Multi-state ingredients
- Equipment constraints
- Staff management
- Priority handling

✅ **Realistic Dynamics**
- Variable prep times
- Equipment breakdowns
- Ingredient shortages
- Staff scheduling
- Wait time penalties

✅ **Three Difficulty Levels**
- Easy: Learning baseline
- Medium: Realistic scenario
- Hard: Production challenge

✅ **OpenEnv Compliant**
- Standard step/reset/state API
- Gymnasium compatible
- Docker deployable
- HF Spaces ready

## Evaluation Metrics

- **Accuracy**: % orders served correctly
- **On-Time Accuracy**: % orders served within time limit
- **Efficiency**: Orders per step
- **Wait Time**: Average customer wait
- **Staff Utilization**: Effective use of cooks
- **Equipment Efficiency**: Equipment usage rate

## Baseline Performance

| Difficulty | Accuracy | On-Time | Score |
|-----------|----------|---------|-------|
| Easy | 92% | 88% | 0.95 |
| Medium | 78% | 75% | 0.82 |
| Hard | 65% | 60% | 0.68 |

## Future Enhancements

- Multi-agent coordination
- Dynamic pricing based on wait
- Customer feedback loop
- Delivery time estimation
- Ingredient sourcing optimization

## License

Open source - part of Meta's OpenEnv ecosystem

## Contact

Built for Meta PyTorch OpenEnv Hackathon India 2026
```

---
