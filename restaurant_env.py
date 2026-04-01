import random
from typing import Dict, List, Tuple, Any

class RestaurantOrderEnv:
    """Production-ready restaurant kitchen management environment"""
    
    def __init__(self, difficulty="medium"):
        """Initialize environment"""
        self.difficulty = difficulty
        
        # 40 Dishes
        self.dishes = [
            {"id": 1, "name": "Biryani", "prep_time": 20, "equipment": "oven", "ingredients": {"rice": "cooked", "chicken": "marinated", "spices": "measured"}},
            {"id": 2, "name": "Butter Chicken", "prep_time": 12, "equipment": "stove", "ingredients": {"chicken": "diced", "cream": "poured", "spices": "measured"}},
            {"id": 3, "name": "Samosa", "prep_time": 8, "equipment": "fryer", "ingredients": {"potato": "boiled", "dough": "rolled", "filling": "ready"}},
            {"id": 4, "name": "Paneer Tikka", "prep_time": 15, "equipment": "oven", "ingredients": {"paneer": "cubed", "spices": "marinated", "oil": "brushed"}},
            {"id": 5, "name": "Dal Makhani", "prep_time": 25, "equipment": "slow_cooker", "ingredients": {"lentils": "cooked", "cream": "ready", "butter": "melted"}},
            {"id": 6, "name": "Tandoori Chicken", "prep_time": 18, "equipment": "tandoor", "ingredients": {"chicken": "marinated", "oil": "brushed", "spices": "ready"}},
            {"id": 7, "name": "Naan", "prep_time": 5, "equipment": "tandoor", "ingredients": {"dough": "proofed", "butter": "ready"}},
            {"id": 8, "name": "Masala Dosa", "prep_time": 7, "equipment": "stove", "ingredients": {"batter": "ready", "oil": "ready", "potato": "cooked"}},
            {"id": 9, "name": "Chana Masala", "prep_time": 20, "equipment": "stove", "ingredients": {"chickpeas": "cooked", "onions": "diced", "spices": "measured"}},
            {"id": 10, "name": "Aloo Paratha", "prep_time": 10, "equipment": "stove", "ingredients": {"dough": "rolled", "potato": "boiled", "butter": "ready"}},
            {"id": 11, "name": "Rajma", "prep_time": 30, "equipment": "slow_cooker", "ingredients": {"beans": "soaked", "onions": "diced", "spices": "measured"}},
            {"id": 12, "name": "Chole Bhature", "prep_time": 12, "equipment": "fryer", "ingredients": {"chickpeas": "cooked", "dough": "proofed", "oil": "ready"}},
            {"id": 13, "name": "Rogan Josh", "prep_time": 18, "equipment": "stove", "ingredients": {"mutton": "marinated", "yogurt": "ready", "spices": "measured"}},
            {"id": 14, "name": "Korma", "prep_time": 16, "equipment": "stove", "ingredients": {"chicken": "diced", "cream": "ready", "coconut": "grated"}},
            {"id": 15, "name": "Pakora", "prep_time": 6, "equipment": "fryer", "ingredients": {"vegetables": "cut", "batter": "ready", "oil": "ready"}},
            {"id": 16, "name": "Dhokla", "prep_time": 12, "equipment": "oven", "ingredients": {"batter": "fermented", "oil": "ready", "spices": "measured"}},
            {"id": 17, "name": "Idli", "prep_time": 8, "equipment": "oven", "ingredients": {"batter": "fermented", "oil": "ready"}},
            {"id": 18, "name": "Vada", "prep_time": 7, "equipment": "fryer", "ingredients": {"lentils": "soaked", "oil": "ready", "spices": "measured"}},
            {"id": 19, "name": "Upma", "prep_time": 8, "equipment": "stove", "ingredients": {"semolina": "roasted", "vegetables": "cut", "oil": "ready"}},
            {"id": 20, "name": "Poha", "prep_time": 6, "equipment": "stove", "ingredients": {"rice_flakes": "ready", "potatoes": "boiled", "oil": "ready"}},
            {"id": 21, "name": "Biryani Rice", "prep_time": 5, "equipment": "oven", "ingredients": {"rice": "cooked", "spices": "measured"}},
            {"id": 22, "name": "Pulao", "prep_time": 10, "equipment": "oven", "ingredients": {"rice": "cooked", "vegetables": "diced", "spices": "measured"}},
            {"id": 23, "name": "Khichdi", "prep_time": 12, "equipment": "stove", "ingredients": {"rice": "cooked", "lentils": "cooked", "ghee": "ready"}},
            {"id": 24, "name": "Puri", "prep_time": 6, "equipment": "fryer", "ingredients": {"dough": "rolled", "oil": "ready"}},
            {"id": 25, "name": "Bhakri", "prep_time": 4, "equipment": "stove", "ingredients": {"millet": "flour", "oil": "ready"}},
            {"id": 26, "name": "Roti", "prep_time": 3, "equipment": "stove", "ingredients": {"wheat": "flour", "oil": "ready"}},
            {"id": 27, "name": "Lachha Paratha", "prep_time": 8, "equipment": "stove", "ingredients": {"dough": "rolled", "butter": "ready", "oil": "ready"}},
            {"id": 28, "name": "Shahi Tukda", "prep_time": 10, "equipment": "stove", "ingredients": {"bread": "cut", "cream": "ready", "milk": "boiled"}},
            {"id": 29, "name": "Gulab Jamun", "prep_time": 15, "equipment": "fryer", "ingredients": {"milk_powder": "mixed", "oil": "ready", "syrup": "boiled"}},
            {"id": 30, "name": "Kheer", "prep_time": 20, "equipment": "slow_cooker", "ingredients": {"rice": "cooked", "milk": "ready", "sugar": "measured"}},
            {"id": 31, "name": "Rasgulla", "prep_time": 12, "equipment": "stove", "ingredients": {"cottage_cheese": "formed", "syrup": "boiling", "milk": "ready"}},
            {"id": 32, "name": "Jalebi", "prep_time": 8, "equipment": "fryer", "ingredients": {"batter": "ready", "oil": "ready", "syrup": "boiling"}},
            {"id": 33, "name": "Barfi", "prep_time": 15, "equipment": "stove", "ingredients": {"milk_powder": "mixed", "ghee": "melted", "sugar": "measured"}},
            {"id": 34, "name": "Halwa", "prep_time": 18, "equipment": "stove", "ingredients": {"semolina": "roasted", "ghee": "melted", "sugar": "syrup"}},
            {"id": 35, "name": "Laddu", "prep_time": 10, "equipment": "stove", "ingredients": {"flour": "roasted", "ghee": "melted", "sugar": "powdered"}},
            {"id": 36, "name": "Payasam", "prep_time": 20, "equipment": "slow_cooker", "ingredients": {"rice": "cooked", "coconut": "grated", "jaggery": "melted"}},
            {"id": 37, "name": "Fafda", "prep_time": 8, "equipment": "fryer", "ingredients": {"flour": "mixed", "oil": "ready", "spices": "measured"}},
            {"id": 38, "name": "Kachumbari", "prep_time": 5, "equipment": None, "ingredients": {"tomatoes": "cut", "onions": "sliced", "lemon": "ready"}},
            {"id": 39, "name": "Raita", "prep_time": 3, "equipment": None, "ingredients": {"yogurt": "ready", "cucumber": "grated", "spices": "measured"}},
            {"id": 40, "name": "Pickle", "prep_time": 2, "equipment": None, "ingredients": {"pickle": "ready"}},
        ]
        
        # Ingredient states
        self.ingredients = {
            "rice": {"states": ["raw", "washed", "soaked", "cooked", "seasoned"], "current": "raw"},
            "chicken": {"states": ["frozen", "thawed", "diced", "marinated", "cooked"], "current": "frozen"},
            "paneer": {"states": ["block", "cut", "cubed", "marinated", "grilled"], "current": "block"},
            "lentils": {"states": ["raw", "washed", "soaked", "cooked", "tempered"], "current": "raw"},
            "dough": {"states": ["flour", "mixed", "kneaded", "rested", "rolled", "proofed"], "current": "flour"},
            "potato": {"states": ["raw", "washed", "cut", "boiled"], "current": "raw"},
            "cream": {"states": ["ready"], "current": "ready"},
            "oil": {"states": ["ready"], "current": "ready"},
            "butter": {"states": ["ready"], "current": "ready"},
            "spices": {"states": ["measured"], "current": "measured"},
        }
        
        # Equipment
        self.equipment = {
            "oven": {"capacity": 4, "busy": 0, "requires_staff": 1, "health": 1.0},
            "stove": {"capacity": 3, "busy": 0, "requires_staff": 1, "health": 1.0},
            "fryer": {"capacity": 2, "busy": 0, "requires_staff": 1, "health": 1.0},
            "tandoor": {"capacity": 2, "busy": 0, "requires_staff": 1, "health": 1.0},
            "slow_cooker": {"capacity": 2, "busy": 0, "requires_staff": 0, "health": 1.0},
        }
        
        # Staff management
        self.staff = {
            "total": 5,
            "available": 5,
            "busy": 0,
            "on_break": 0,
        }
        
        # Episode state
        self.pending_orders = []
        self.completed_orders = []
        self.spoiled_items = []
        self.step_count = 0
        self.total_wait_time = 0
        self.max_steps = 100
        
        # Set difficulty
        if difficulty == "easy":
            self.max_orders = 10
            self.prep_ratio = 0.8  # 80% prepped
            self.staff["total"] = 4
            self.equipment_reliability = 1.0
        elif difficulty == "medium":
            self.max_orders = 20
            self.prep_ratio = 0.5  # 50% prepped
            self.staff["total"] = 3
            self.equipment_reliability = 0.7
        else:  # hard
            self.max_orders = 40
            self.prep_ratio = 0.2  # 20% prepped
            self.staff["total"] = 2
            self.equipment_reliability = 0.5
        
        self.staff["available"] = self.staff["total"]
    
    def reset(self):
        """Start new episode"""
        self.pending_orders = []
        self.completed_orders = []
        self.spoiled_items = []
        self.step_count = 0
        self.total_wait_time = 0
        
        # Generate orders
        for i in range(self.max_orders):
            dish = random.choice(self.dishes)
            priority = "vip" if random.random() < 0.1 else "normal"
            order = {
                "id": i + 1,
                "dish_id": dish["id"],
                "dish_name": dish["name"],
                "prep_time": dish["prep_time"],
                "equipment": dish["equipment"],
                "ingredients_needed": dish["ingredients"],
                "wait_time": 0,
                "priority": priority,
                "arrival_time": i,
                "status": "pending",
            }
            self.pending_orders.append(order)
        
        # Reset equipment
        for eq in self.equipment.values():
            eq["busy"] = 0
            eq["health"] = 1.0 if random.random() > (1 - self.equipment_reliability) else 0.5
        
        # Reset staff
        self.staff["available"] = self.staff["total"]
        self.staff["busy"] = 0
        self.staff["on_break"] = 0
        
        observation = self._get_observation()
        return observation
    
    def step(self, action):
        """Agent chooses order to cook"""
        self.step_count += 1
        
        # Validate action
        if action < 0 or action >= len(self.pending_orders):
            return self._get_observation(), -1.0, True, {"error": "Invalid order"}
        
        order = self.pending_orders[action]
        
        # Check staff availability
        if self.staff["available"] <= 0:
            return self._get_observation(), -0.5, False, {"error": "No staff available"}
        
        # Check equipment availability
        if order["equipment"] and self.equipment[order["equipment"]]["busy"] >= self.equipment[order["equipment"]]["capacity"]:
            return self._get_observation(), -0.4, False, {"error": "Equipment busy"}
        
        # Calculate reward
        reward = self._calculate_reward(order)
        
        # Process order
        self.completed_orders.append(order)
        self.pending_orders.pop(action)
        self.total_wait_time += order["wait_time"]
        
        # Update equipment
        if order["equipment"]:
            self.equipment[order["equipment"]]["busy"] += 1
        
        # Update staff
        self.staff["available"] -= 1
        self.staff["busy"] += 1
        
        # Increment wait times
        for o in self.pending_orders:
            o["wait_time"] += 1
        
        # Check if done
        done = len(self.pending_orders) == 0 or self.step_count >= self.max_steps
        
        observation = self._get_observation()
        
        info = {
            "cooked_dish": order["dish_name"],
            "wait_time": order["wait_time"],
            "priority": order["priority"],
        }
        
        return observation, reward, done, info
    
    def _calculate_reward(self, order):
        """Calculate reward based on multiple factors"""
        base = 0.5
        
        # Time-based reward
        if order["wait_time"] >= 15:
            time_reward = 0.5  # High priority, been waiting
        elif order["wait_time"] >= 10:
            time_reward = 0.3
        elif order["wait_time"] >= 5:
            time_reward = 0.1
        else:
            time_reward = -0.2
        
        # Priority bonus
        priority_bonus = 0.3 if order["priority"] == "vip" else 0.0
        
        # Efficiency penalty
        equipment_penalty = -0.1 if order["equipment"] and self.equipment[order["equipment"]]["busy"] >= self.equipment[order["equipment"]]["capacity"] else 0.0
        staff_penalty = -0.1 if self.staff["available"] <= 1 else 0.0
        
        # Equipment health
        health_penalty = -0.2 if order["equipment"] and self.equipment[order["equipment"]]["health"] < 1.0 else 0.0
        
        total = base + time_reward + priority_bonus + equipment_penalty + staff_penalty + health_penalty
        return min(max(total, -2.0), 2.0)
    
    def _get_observation(self):
        """Return current observation"""
        return {
            "pending_orders": len(self.pending_orders),
            "completed_orders": len(self.completed_orders),
            "step_count": self.step_count,
            "staff_available": self.staff["available"],
            "avg_wait_time": self.total_wait_time / max(len(self.completed_orders), 1),
        }
    
    def state(self):
        """Return ground truth for grading"""
        accuracy = len(self.completed_orders) / (len(self.completed_orders) + len(self.pending_orders)) if (len(self.completed_orders) + len(self.pending_orders)) > 0 else 0
        
        on_time = sum(1 for o in self.completed_orders if o["wait_time"] <= 10)
        on_time_accuracy = on_time / max(len(self.completed_orders), 1)
        
        return {
            "total_orders": len(self.completed_orders) + len(self.pending_orders),
            "completed_orders": len(self.completed_orders),
            "pending_orders": len(self.pending_orders),
            "accuracy": accuracy,
            "on_time_accuracy": on_time_accuracy,
            "avg_wait_time": self.total_wait_time / max(len(self.completed_orders), 1),
            "difficulty": self.difficulty,
            "step_count": self.step_count,
        }