class GoalStackPlanner:
    def __init__(self, initial, goal, actions):
        self.state = set(initial)
        self.goal = goal
        self.actions = actions
        self.stack = list(goal)
        self.plan = []

    def is_satisfied(self, fact):
        return fact in self.state

    def apply_action(self, action):
        for d in action["delete"]:
            self.state.discard(d)
        for a in action["add"]:
            self.state.add(a)

    def plan_steps(self):
        while self.stack:
            top = self.stack.pop()

            if isinstance(top, str): 
                if not self.is_satisfied(top):
                    for action in self.actions:
                        if top in action["add"]:
                            self.stack.append(action)
                            self.stack.extend(action["preconditions"])
                            break
            else:   
                if all(pre in self.state for pre in top["preconditions"]):
                    self.apply_action(top)
                    self.plan.append(top["name"])
        return self.plan


def pickup(x):
    return {
        "name": f"PickUp({x})",
        "preconditions": [f"OnTable({x})", f"Clear({x})", "ArmEmpty"],
        "add": [f"Holding({x})"],
        "delete": [f"OnTable({x})", "ArmEmpty"]
    }


def putdown(x):
    return {
        "name": f"PutDown({x})",
        "preconditions": [f"Holding({x})"],
        "add": [f"OnTable({x})", f"Clear({x})", "ArmEmpty"],
        "delete": [f"Holding({x})"]
    }


def stack(x, y):
    return {
        "name": f"Stack({x},{y})",
        "preconditions": [f"Holding({x})", f"Clear({y})"],
        "add": [f"On({x},{y})", f"Clear({x})", "ArmEmpty"],
        "delete": [f"Holding({x})", f"Clear({y})"]
    }


def unstack(x, y):
    return {
        "name": f"UnStack({x},{y})",
        "preconditions": [f"On({x},{y})", f"Clear({x})", "ArmEmpty"],
        "add": [f"Holding({x})", f"Clear({y})"],
        "delete": [f"On({x},{y})", "ArmEmpty"]
    }


initial = [
    "OnTable(A)", "OnTable(B)", "OnTable(C)",
    "Clear(A)", "Clear(B)", "Clear(C)", "ArmEmpty"
]

goal = ["On(C,B)", "On(B,A)"]

actions = [
    pickup("A"), pickup("B"), pickup("C"),
    putdown("A"), putdown("B"), putdown("C"),
    stack("A", "B"), stack("A", "C"),
    stack("B", "A"), stack("B", "C"),
    stack("C", "A"), stack("C", "B"),
    unstack("A", "B"), unstack("B", "A"),
    unstack("C", "A"), unstack("C", "B")
]

planner = GoalStackPlanner(initial, goal, actions)
solution = planner.plan_steps()
print("Plan:", solution)