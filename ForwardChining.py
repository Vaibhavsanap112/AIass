#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx


rules = [
    ([("problem","power_light_off")], ("solution","check_power_supply")),
    ([("problem","computer_not_starting")], ("solution","check_RAM")),
    ([("problem","blank_display")], ("solution","check_monitor_cable")),
    ([("problem","strange_beep")], ("solution","check_hard_disk"))
]

def forward_chain(facts, rules):
    inferred = set(facts)
    changed = True
    while changed:
        changed = False
        for p, c in rules:
            if all(x in inferred for x in p) and c not in inferred:
                inferred.add(c)
                changed = True
    return inferred

facts=[]
while True:
    s=input("Enter problem (done to stop): ").strip().lower()
    if s=="done": break
    facts.append(("problem",s))

res=forward_chain(facts,rules)
print("\nSuggested Solutions:")
for r in res:
    if r[0]=="solution": print("-",r[1])


 #Enter problem (done to stop): BLANK_DISPLAY
 #  power_light_off
# computer_not_starting
# blank_display
# strange_beep

#Enter problem (done to stop): done

#Suggested Solutions:
#- check_monitor_cable   

# ------------------------------------------------------
# EXPLANATION OF THE CODE (FORWARD CHAINING EXPERT SYSTEM)
# ------------------------------------------------------

# 📘 AIM:
# Suggest solutions for computer problems using a **Forward Chaining** rule-based system.
# The system infers solutions automatically based on given facts and rules.

# ------------------------------------------------------
# 🧩 CONCEPT USED
# ------------------------------------------------------
# **Forward Chaining**:
# - A rule-based reasoning method.
# - Starts from known facts and applies rules to infer new facts until no more new facts can be inferred.
# - In this system, problems entered by the user are facts, 
#   and solutions are inferred using rules.

# ------------------------------------------------------
# 🧩 CODE EXPLANATION (LINE BY LINE)
# ------------------------------------------------------

# rules = [...]
# → Defines the rules of the expert system.
# Each rule is a tuple:
#   ([conditions], (conclusion))
# Example:
# ([("problem","blank_display")], ("solution","check_monitor_cable"))
# Means: If the problem is "blank_display", then suggest "check_monitor_cable".

# ------------------------------------------------------
# FUNCTION: forward_chain(facts, rules)
# ------------------------------------------------------
# def forward_chain(facts, rules):
#     inferred = set(facts)
#     changed = True
#     while changed:
#         changed = False
#         for p, c in rules:
#             if all(x in inferred for x in p) and c not in inferred:
#                 inferred.add(c)
#                 changed = True
#     return inferred
# → Takes the initial facts and applies rules repeatedly.
# → Adds new inferred facts to the set until no new facts can be inferred.

# ------------------------------------------------------
# USER INPUT SECTION
# ------------------------------------------------------
# facts=[]
# while True:
#     s=input("Enter problem (done to stop): ").strip().lower()
#     if s=="done": break
#     facts.append(("problem",s))
# → Takes user input for problems one by one.
# → Stops when user enters "done".

# ------------------------------------------------------
# APPLY FORWARD CHAINING
# ------------------------------------------------------
# res=forward_chain(facts,rules)
# print("\nSuggested Solutions:")
# for r in res:
#     if r[0]=="solution": print("-",r[1])
# → Calls the forward_chain function and prints inferred solutions.
# → Only facts with type "solution" are printed.

# ------------------------------------------------------
# 🧮 SAMPLE INPUT / OUTPUT
# ------------------------------------------------------
# Input:
# Enter problem (done to stop): BLANK_DISPLAY
# Enter problem (done to stop): done

# Output:
# Suggested Solutions:
# - check_monitor_cable

# ------------------------------------------------------
# 🧠 SIMPLE UNDERSTANDING
# ------------------------------------------------------
# - The program starts with user-provided problems (facts).
# - Rules are applied repeatedly to infer solutions.
# - This is a **data-driven reasoning system**, commonly called a Forward Chaining Expert System.

# ------------------------------------------------------
# 🌍 REAL-TIME APPLICATIONS
# ------------------------------------------------------
# 1. Troubleshooting computer or electronic issues.
# 2. Medical diagnosis systems (suggest treatment based on symptoms).
# 3. Automated customer support chatbots.
# 4. Industrial fault detection systems.
# ------------------------------------------------------
