# pip install python-constraint
#python.exe -m pip install --upgrade pip
#& "C:\Program Files\Python312\python.exe" -m pip install python-constraint
#& "C:\Program Files\Python312\python.exe" -m pip show python-constraint
#RERUN 
#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx



from constraint import Problem

teams = input("Enter team names (comma separated): ").split(',')
teams = [t.strip() for t in teams if t.strip()]  # clean spaces
slots = list(map(int, input("Enter slot numbers (comma separated): ").split(',')))
stadiums = input("Enter stadium names (comma separated): ").split(',')
stadiums = [s.strip() for s in stadiums if s.strip()]

matches = [(t1, t2) for i, t1 in enumerate(teams) for t2 in teams[i+1:]]

p = Problem()
p.addVariables(matches, [(s, st) for s in slots for st in stadiums])

# A team cannot play two matches in the same slot
for t in teams:
    team_matches = [m for m in matches if t in m]
    for i in range(len(team_matches)):
        for j in range(i+1, len(team_matches)):
            p.addConstraint(lambda a, b: a[0] != b[0], (team_matches[i], team_matches[j]))

# No two matches in same slot & stadium
for i in range(len(matches)):
    for j in range(i+1, len(matches)):
        p.addConstraint(lambda a, b: not (a[0] == b[0] and a[1] == b[1]), (matches[i], matches[j]))

# --- GET SOLUTIONS ---
sol = p.getSolutions()
print("\nTotal valid schedules:", len(sol))
if sol:
    print("Sample schedule:")
    for match, (slot, stadium) in sol[0].items():
        print(f"{match[0]} vs {match[1]} → Slot {slot}, Stadium {stadium}")
else:
    print("No valid schedules found.")




# Input:
# Enter team names (comma separated): T1,T2,T3,T4
# Enter slot numbers (comma separated): 1,2,3
# Enter stadium names (comma separated): A,B

# Output:
# Total valid schedules: 4
# Sample schedule:
# T1 vs T2 → Slot 1, Stadium A
# T1 vs T3 → Slot 2, Stadium B
# T1 vs T4 → Slot 3, Stadium A
# T2 vs T3 → Slot 1, Stadium B
# T2 vs T4 → Slot 2, Stadium A
# T3 vs T4 → Slot 3, Stadium B
#OP
#Enter team names (comma separated): T1,T2,T3,T4
#Enter slot numbers (comma separated): 1,2,3
#Enter stadium names (comma separated): A,B

# ------------------------------------------------------
# EXPLANATION OF THE CODE (MATCH SCHEDULING USING CSP)
# ------------------------------------------------------

# 📘 AIM:
# Schedule matches between teams using a Constraint Satisfaction Problem (CSP) 
# so that no team plays two matches in the same slot, 
# and no two matches happen in the same stadium at the same slot.

# ------------------------------------------------------
# 🧩 CODE EXPLANATION (LINE BY LINE)
# ------------------------------------------------------

# from constraint import Problem
# → Imports the 'Problem' class from python-constraint library to handle variables and constraints.

# ------------------------------------------------------
# 1️⃣ INPUT SECTION
# ------------------------------------------------------
# teams = input("Enter team names (comma separated): ").split(',')
# slots = list(map(int, input("Enter slot numbers (comma separated): ").split(',')))
# stadiums = input("Enter stadium names (comma separated): ").split(',')
# → Takes team names, slots, and stadium names from the user.
# → Cleans spaces to avoid errors.

# ------------------------------------------------------
# 2️⃣ CREATE ALL MATCH PAIRS
# ------------------------------------------------------
# matches = [(t1, t2) for i, t1 in enumerate(teams) for t2 in teams[i+1:]]
# → Creates all unique matches between teams.
# Example: For teams T1,T2,T3,T4, matches = 
# [(T1,T2),(T1,T3),(T1,T4),(T2,T3),(T2,T4),(T3,T4)]

# ------------------------------------------------------
# 3️⃣ DEFINE VARIABLES AND DOMAINS
# ------------------------------------------------------
# p = Problem()
# p.addVariables(matches, [(s, st) for s in slots for st in stadiums])
# → Each match is a variable.
# → Its domain is all possible combinations of (slot, stadium).

# ------------------------------------------------------
# 4️⃣ ADD CONSTRAINTS
# ------------------------------------------------------

# (a) A team cannot play two matches in the same slot
# for t in teams:
#     team_matches = [m for m in matches if t in m]
#     for i in range(len(team_matches)):
#         for j in range(i+1, len(team_matches)):
#             p.addConstraint(lambda a, b: a[0] != b[0], (team_matches[i], team_matches[j]))
# → Ensures that no team has two matches at the same time.

# (b) No two matches in the same slot and stadium
# for i in range(len(matches)):
#     for j in range(i+1, len(matches)):
#         p.addConstraint(lambda a, b: not (a[0] == b[0] and a[1] == b[1]), (matches[i], matches[j]))
# → Ensures that two matches don’t occupy the same stadium at the same slot.

# ------------------------------------------------------
# 5️⃣ GET AND DISPLAY SOLUTIONS
# ------------------------------------------------------
# sol = p.getSolutions()
# print("\nTotal valid schedules:", len(sol))
# if sol:
#     print("Sample schedule:")
#     for match, (slot, stadium) in sol[0].items():
#         print(f"{match[0]} vs {match[1]} → Slot {slot}, Stadium {stadium}")
# else:
#     print("No valid schedules found.")
# → Finds all valid schedules and prints one example.

# ------------------------------------------------------
# 🧮 SAMPLE INPUT / OUTPUT
# ------------------------------------------------------



# ------------------------------------------------------
# 🧠 SIMPLE UNDERSTANDING:
# ------------------------------------------------------
# - The program uses CSP to automatically handle constraints.
# - Each match is assigned a valid slot and stadium.
# - Constraints ensure no conflicts for teams or stadiums.
# - Useful for sports leagues, exam timetables, and conference scheduling.

# ------------------------------------------------------
# 🌍 REAL-TIME APPLICATIONS:
# ------------------------------------------------------
# 1. Scheduling sports tournaments (IPL, FIFA)
# 2. Exam timetables (avoiding clashes)
# 3. Conference room allocations
# ------------------------------------------------------
