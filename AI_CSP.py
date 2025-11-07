from constraint import Problem

teams = ["T1", "T2", "T3", "T4"]
matches = [(t1, t2) for i, t1 in enumerate(teams) for t2 in teams[i + 1:]]
time_slots = [1, 2, 3]
stadiums = ["A", "B"]

p = Problem()
p.addVariables(matches, [(t, s) for t in time_slots for s in stadiums])

for team in teams:
    team_matches = [m for m in matches if team in m]
    for i in range(len(team_matches)):
        for j in range(i + 1, len(team_matches)):
            p.addConstraint(
                lambda m1, m2: m1[0] != m2[0],
                (team_matches[i], team_matches[j])
            )

for i in range(len(matches)):
    for j in range(i + 1, len(matches)):
        p.addConstraint(
            lambda m1, m2: not (m1[0] == m2[0] and m1[1] == m2[1]),
            (matches[i], matches[j])
        )

solutions = p.getSolutions()

print("Total valid schedules:", len(solutions))
print("Sample Schedule:")
for match, schedule in solutions[0].items():
    print(f"{match}: Time Slot {schedule[0]}, Stadium {schedule[1]}")