tasks = ["MOVE", "TURN"]
print(tasks)

tasks.append("STOP")
print("after append:", tasks)

tasks.insert(1, "SCAN")
print("after insert:", tasks)

tasks.remove("MOVE")
print("after remove:", tasks)

#--------------------------------------------------

p = [5, 10, 15]
q = p
r = p[:]

q.append(20)
r.append(50)

print("p =", p)
print("q =", q)
print("r =", r)

print("q is p:", q is p, "| r is p:", r is p)

#--------------------------------------------------

speeds = [10, 0, 25, 0, 40]
for s in speeds[:]:
    if s == 0:
        speeds.remove(s)
print("valid speeds:", speeds)

#--------------------------------------------------

temperatures = [18, 26, 35, 42, 29]
increased = [t + 5 for t in temperatures]
high = [t for t in temperatures if t >= 30]

print("increased temperatures:", increased)
print("high temperatures:", high)
