import random
from typing import Dict, List, Tuple, Any

class RestaurantOrderEnv:
    """Production-ready restaurant kitchen management environment"""
    
    def __init__(self, difficulty="medium"):
        """Initialize environment"""
        self.difficulty = difficulty
        
        # 40 Dishes with equipment requirements
        self.dishes = [
            {"id": 1, "name": "Biryani", "prep_time": 20, "equipment": "oven", "ingredients": {"rice": "cooked", "chicken": "marinated"}},
            {"id": 2, "name": "Butter Chicken", "prep_time": 12, "equipment": "stove", "ingredients": {"chicken": "diced", "cream": "ready"}},
            {"id": 3, "name": "Samosa", "prep_time": 8, "equipment": "fryer", "ingredients": {"potato": "boiled", "dough": "rolled"}},
            {"id": 4, "name": "Paneer Tikka", "prep_time": 15, "equipment": "oven", "ingredients": {"paneer": "cubed", "spices": "ready"}},
            {"id": 5, "name": "Dal Makhani", "prep_time": 25, "equipment": "slow_cooker", "ingredients": {"lentils": "cooked", "cream": "ready"}},
            {"id": 6, "name": "Tandoori Chicken", "prep_time": 18, "equipment": "tandoor", "ingredients": {"chicken": "marinated", "spices": "ready"}},
            {"id": 7, "name": "Naan", "prep_time": 5, "equipment": "tandoor", "ingredients": {"dough": "proofed", "butter": "ready"}},
            {"id": 8, "name": "Masala Dosa", "prep_time": 7, "equipment": "stove", "ingredients": {"batter": "ready", "potato": "cooked"}},
            {"id": 9, "name": "Chana Masala", "prep_time": 20, "equipment": "stove", "ingredients": {"chickpeas": "cooked", "spices": "ready"}},
            {"id": 10, "name": "Aloo Paratha", "prep_time": 10, "equipment": "stove", "ingredients": {"dough": "rolled", "potato": "boiled"}},
            {"id": 11, "name": "Rajma", "prep_time": 30, "equipment": "slow_cooker", "ingredients": {"beans": "cooked", "spices": "ready"}},
            {"id": 12, "name": "Chole Bhature", "prep_time": 12, "equipment": "fryer", "ingredients": {"chickpeas": "cooked", "dough": "proofed"}},
            {"id": 13, "name": "Rogan Josh", "prep_time": 18, "equipment": "stove", "ingredients": {"mutton": "marinated", "spices": "ready"}},
            {"id": 14, "name": "Korma", "prep_time": 16, "equipment": "stove", "ingredients": {"chicken": "diced", "cream": "ready"}},
            {"id": 15, "name": "Pakora", "prep_time": 6, "equipment": "fryer", "ingredients": {"vegetables": "cut", "batter": "ready"}},
            {"id": 16, "name": "Dhokla", "prep_time": 12, "equipment": "oven", "ingredients": {"batter": "fermented", "oil": "ready"}},
            {"id": 17, "name": "Idli", "prep_time": 8, "equipment": "oven", "ingredients": {"batter": "fermented", "oil": "ready"}},
            {"id": 18, "name": "Vada", "prep_time": 7, "equipment": "fryer", "ingredients": {"lentils": "soaked", "oil": "ready"}},
            {"id": 19, "name": "Upma", "prep_time": 8, "equipment": "stove", "ingredients": {"semolina": "roasted", "vegetables": "cut"}},
            {"id": 20, "name": "Poha", "prep_time": 6, "equipment": "stove", "ingredients": {"rice_flakes": "ready", "potatoes": "boiled"}},
            {"id": 21, "name": "Biryani Rice", "prep_time": 5, "equipment": "oven", "ingredients": {"rice": "cooked", "spices": "ready"}},
            {"id": 22, "name": "Pulao", "prep_time": 10, "equipment": "oven", "ingredients": {"rice": "cooked", "vegetables": "diced"}},
            {"id": 23, "name": "Khichdi", "prep_time": 12, "equipment": "stove", "ingredients": {"rice": "cooked", "lentils": "cooked"}},
            {"id": 24, "name": "Puri", "prep_time": 6, "equipment": "fryer", "ingredients": {"dough": "rolled", "oil": "ready"}},
            {"id": 25, "name": "Bhakri", "prep_time": 4, "equipment": "stove", "ingredients": {"millet": "flour", "oil": "ready"}},
            {"id": 26, "name": "Roti", "prep_time": 3, "equipment": "stove", "ingredients": {"wheat": "flour", "oil": "ready"}},
            {"id": 27, "name": "Lachha Paratha", "prep_time": 8, "equipment": "stove", "ingredients": {"dough": "rolled", "butter": "ready"}},
            {"id": 28, "name": "Shahi Tukda", "prep_time": 10, "equipment": "stove", "ingredients": {"bread": "cut", "cream": "ready"}},
            {"id": 29, "name": "Gulab Jamun", "prep_time": 15, "equipment": "fryer", "ingredients": {"milk_powder": "mixed", "oil": "ready"}},
            {"id": 30, "name": "Kheer", "prep_time": 20, "equipment": "slow_cooker", "ingredients": {"rice": "cooked", "milk": "ready"}},
            {"id": 31, "name": "Rasgulla", "prep_time": 12, "equipment": "stove", "ingredients": {"cottage_cheese": "formed", "syrup": "ready"}},
            {"id": 32, "name": "Jalebi", "prep_time": 8, "equipment": "fryer", "ingredients": {"batter": "ready", "oil": "ready"}},
            {"id": 33, "name": "Barfi", "prep_time": 15, "equipment": "stove", "ingredients": {"milk_powder": "mixed", "ghee": "ready"}},
            {"id": 34, "name": "Halwa", "prep_time": 18, "equipment": "stove", "ingredients": {"semolina": "roasted", "ghee": "ready"}},
            {"id": 35, "name": "Laddu", "prep_time": 10, "equipment": "stove", "ingredients": {"flour": "roasted", "ghee": "ready"}},
            {"id": 36, "name": "Payasam", "prep_time": 20, "equipment": "slow_cooker", "ingredients": {"rice": "cooked", "coconut": "grated"}},
            {"id": 37, "name": "Fafda", "prep_time": 8, "equipment": "fryer", "ingredients": {"flour": "mixed", "oil": "ready"}},
            {"id": 38, "name": "Kachumbari", "prep_time": 5, "equipment": None, "ingredients": {"tomatoes": "cut", "onions": "sliced"}},
            {"id": 39, "name": "Raita", "prep_time": 3, "equipment": None, "ingredients": {"yogurt": "ready", "cucumber": "grated"}},
            {"id": 40, "name": "Pickle", "prep_time": 2, "equipment": None, "ingredients": {"pickle": "ready"}},
        ]
        
        # Ingredient states and prep times
        self.ingredients = {
            "rice": {
                "states": ["raw", "washed", "soaked", "cooked", "seasoned"],
                "prep_times": {"raw": 5, "washed": 5, "soaked": 30, "cooked": 15, "seasoned": 0},
                "current_state": "raw"
            },
            "chicken": {
                "states": ["frozen", "thawed", "diced", "marinated", "cooked"],
                "prep_times": {"frozen": 15, "thawed": 10, "diced": 10, "marinated": 20, "cooked": 0},
                "current_state": "frozen"
            },
            "paneer": {
                "states": ["block", "cut", "cubed", "marinated", "grilled"],
                "prep_times": {"block": 8, "cut": 3, "cubed": 3, "marinated": 10, "grilled": 0},
                "current_state": "block"
            },
            "lentils": {
                "states": ["raw", "washed", "soaked", "cooked", "tempered"],
                "prep_times": {"raw": 5, "washed": 5, "soaked": 60, "cooked": 45, "tempered": 0},
                "current_state": "raw"
            },
            "dough": {
                "states": ["flour", "mixed", "kneaded", "rested", "rolled", "proofed"],
                "prep_times": {"flour": 10, "mixed": 10, "kneaded": 15, "rested": 60, "rolled": 3, "proofed": 0},
                "current_state": "flour"
            },
            "potato": {
                "states": ["raw", "washed", "cut", "boiled"],
                "prep_times": {"raw": 5, "washed": 2, "cut": 5, "boiled": 0},
                "current_state": "raw"
            },
            "cream": {"states": ["ready"], "prep_times": {"ready": 0}, "current_state": "ready"},
            "oil": {"states": ["ready"], "prep_times": {"ready": 0}, "current_state": "ready"},
            "butter": {"states": ["ready"], "prep_times": {"ready": 0}, "current_state": "ready"},
            "ghee": {"states": ["ready"], "prep_times": {"ready": 0}, "current_state": "ready"},
            "spices": {"states": ["ready"], "prep_times": {"ready": 0}, "current_state": "ready"},
            "milk": {"states": ["ready"], "prep_times": {"ready": 0}, "current_state": "ready"},
            "yogurt": {"states": ["ready"], "prep_times": {"ready": 0}, "current_state": "ready"},
            "batter": {"states": ["raw", "fermented", "ready"], "prep_times": {"raw": 0, "fermented": 120, "ready": 0}, "current_state": "raw"},
        }
        
        # Equipment with capacity and staff requirements
        self.equipment = {
            "oven": {"capacity": 4, "busy": 0, "requires_staff": 1, "health": 1.0},
            "stove": {"capacity": 3, "busy": 0, "requires_staff": 1, "health": 1.0},
            "fryer": {"capacity": 2, "busy": 0, "requires_staff": 1, "health": 1.0},
            "tandoor": {"capacity": 2, "busy": 0, "requires_staff": 1, "health": 1.0},
            "slow_cooker": {"capacity": 2, "busy": 0, "requires_staff": 0, "health": 1.0},
        }
        
        # Staff management
        self.staff = {
            "total": 0,
            "available": 0,
            "busy": 0,
            "on_break": 0,
        }
        
        # Set difficulty parameters
        if difficulty == "easy":
            self.max_orders = 10
            self.prep_ratio = 0.8  # 80% prepped
            self.staff["total"] = 4
            self.equipment_reliability = 1.0
            self.ingredient_shortage_rate = 0.0
        elif difficulty == "medium":
            self.max_orders = 20
            self.prep_ratio = 0.5  # 50% prepped
            self.staff["total"] = 3
            self.equipment_reliability = 0.7
            self.ingredient_shortage_rate = 0.1
        else:  # hard
            self.max_orders = 40
            self.prep_ratio = 0.2  # 20% prepped
            self.staff["total"] = 2
            self.equipment_reliability = 0.5
            self.ingredient_shortage_rate = 0.3
        
        self.staff["available"] = self.staff["total"]
        
        # Episode state
        self.pending_orders = []
        self.completed_orders = []
        self.spoiled_items = []
        self.step_count = 0
        self.total_wait_time = 0
        self.max_steps = 100
    
    def reset(self):
        """Start new episode"""
        self.pending_orders = []
        self.completed_orders = []
        self.spoiled_items = []
        self.step_count = 0
        self.total_wait_time = 0
        self.staff["available"] = self.staff["total"]
        self.staff["busy"] = 0
        
        # Generate orders with random ingredients in various prep states
        for i in range(self.max_orders):
            dish = random.choice(self.dishes)
            priority = "vip" if random.random() < 0.1 else "normal"
            
            # Randomize ingredient prep states based on difficulty
            ingredients_state = {}
            for ing_name in dish.get("ingredients", {}):
                if random.random() < self.prep_ratio:
                    # Pre-prepped: skip to last state
                    ing_info = self.ingredients.get(ing_name, {})
                    if ing_info.get("states"):
                        ingredients_state[ing_name] = ing_info["states"][-1]
                else:
                    # Raw: start from first state
                    ing_info = self.ingredients.get(ing_name, {})
                    if ing_info.get("states"):
                        ingredients_state[ing_name] = ing_info["states"][0]
            
            order = {
                "id": i + 1,
                "dish_id": dish["id"],
                "dish_name": dish["name"],
                "prep_time": dish["prep_time"],
                "equipment": dish["equipment"],
                "ingredients_needed": dish.get("ingredients", {}),
                "ingredients_state": ingredients_state,
                "wait_time": 0,
                "priority": priority,
                "arrival_time": i,
                "status": "pending",
            }
            self.pending_orders.append(order)
        
        # Reset equipment health
        for eq in self.equipment.values():
            eq["busy"] = 0
            eq["health"] = 1.0 if random.random() > (1 - self.equipment_reliability) else 0.5
        
        observation = self._get_observation()
        return observation
    
    def step(self, action):
        """Agent chooses order to cook"""
        self.step_count += 1
        
        # If no pending orders, episode ends
        if len(self.pending_orders) == 0:
            return self._get_observation(), 0.0, True, {"status": "all_orders_done"}
        
        # Validate action
        if action < 0 or action >= len(self.pending_orders):
            action = 0
        
        order = self.pending_orders[action]
        
        # Check ingredient readiness
        ingredients_ready = self._check_ingredients_ready(order)
        
        # Calculate reward (complex logic)
        reward = self._calculate_reward(order, ingredients_ready)
        
        # Process order
        self.completed_orders.append(order)
        self.pending_orders.pop(action)
        self.total_wait_time += order["wait_time"]
        
        # Update equipment
        if order["equipment"]:
            self.equipment[order["equipment"]]["busy"] += 1
            # Random equipment breakdown
            if random.random() > self.equipment_reliability:
                self.equipment[order["equipment"]]["health"] = 0.5
        
        # Update staff
        if self.staff["available"] > 0:
            self.staff["available"] -= 1
            self.staff["busy"] += 1
        
        # Increment wait times for remaining orders
        for o in self.pending_orders:
            o["wait_time"] += 1
        
        # Check spoilage (old ingredients go bad)
        for o in self.pending_orders:
            if o["wait_time"] > 25:
                self.spoiled_items.append(o["dish_name"])
                reward -= 0.5
        
        # Check if done
        done = len(self.pending_orders) == 0 or self.step_count >= self.max_steps
        
        observation = self._get_observation()
        
        info = {
            "cooked_dish": order["dish_name"],
            "wait_time": order["wait_time"],
            "priority": order["priority"],
            "ingredients_ready": ingredients_ready,
        }
        
        return observation, reward, done, info
    
    def _check_ingredients_ready(self, order):
        """Check if all ingredients are in ready state"""
        for ing_name in order.get("ingredients_needed", {}):
            current_state = order["ingredients_state"].get(ing_name)
            if current_state is None:
                return False
            
            ing_info = self.ingredients.get(ing_name, {})
            if ing_info.get("states"):
                ready_state = ing_info["states"][-1]
                if current_state != ready_state:
                    return False
        
        return True
    
    def _calculate_reward(self, order, ingredients_ready):
        """Calculate sophisticated reward based on multiple factors"""
        base = 0.5
        
        # Time-based reward (fairness)
        if order["wait_time"] >= 15:
            time_reward = 0.5
        elif order["wait_time"] >= 10:
            time_reward = 0.3
        elif order["wait_time"] >= 5:
            time_reward = 0.1
        else:
            time_reward = -0.2
        
        # Priority bonus
        priority_bonus = 0.3 if order["priority"] == "vip" else 0.0
        
        # Ingredient readiness bonus
        ingredient_bonus = 0.2 if ingredients_ready else -0.1
        
        # Equipment health penalty
        equipment_penalty = -0.2 if order["equipment"] and self.equipment[order["equipment"]]["health"] < 1.0 else 0.0
        
        # Staff shortage penalty
        staff_penalty = -0.1 if self.staff["available"] <= 1 else 0.0
        
        total = base + time_reward + priority_bonus + ingredient_bonus + equipment_penalty + staff_penalty
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
        total = len(self.completed_orders) + len(self.pending_orders)
        accuracy = len(self.completed_orders) / total if total > 0 else 0
        
        on_time = sum(1 for o in self.completed_orders if o["wait_time"] <= 10)
        on_time_accuracy = on_time / max(len(self.completed_orders), 1)
        
        staff_util = 1.0 - (self.staff["available"] / self.staff["total"]) if self.staff["total"] > 0 else 0
        
        waste_penalty = len(self.spoiled_items) / max(len(self.completed_orders), 1)
        
        return {
            "total_orders": total,
            "completed_orders": len(self.completed_orders),
            "pending_orders": len(self.pending_orders),
            "accuracy": accuracy,
            "on_time_accuracy": on_time_accuracy,
            "avg_wait_time": self.total_wait_time / max(len(self.completed_orders), 1),
            "staff_utilization": staff_util,
            "waste_percentage": waste_penalty,
            "difficulty": self.difficulty,
            "step_count": self.step_count,
        }
