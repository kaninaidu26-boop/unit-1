robot = {"name": "Nova", "battery": 92, "mode": "manual"}
print(robot)
print(robot["mode"])

robot["battery"] -= 10
robot["speed"] = 0.6
print("updated robot:", robot)

print("keys:", list(robot.keys()))
print("values:", list(robot.values()))

#----------------------------------------------------

robot = {"name": "Nova", "battery": 82}

print(robot.get("speed"))
print(robot.get("speed", 0.5))
print("battery" in robot)

#----------------------------------------------------

errors = ["E3", "E4", "E3", "E5", "E4", "E3"]
frequency = {}

for error in errors:
    frequency[error] = frequency.get(error, 0) + 1

print(frequency)

for error in sorted(frequency, key=frequency.get):
    print(f"{error} occurred {frequency[error]} time(s)")

#----------------------------------------------------

"""
Write a program to count the frequency of characters
in a word and print the most frequent character.
"""

word = "robotics"
counts = {}

for letter in word:
    counts[letter] = counts.get(letter, 0) + 1

print(counts)

for letter in sorted(counts, key=counts.get, reverse=True):
    print(f"{letter} occurred {counts[letter]} times")

most_frequent = max(counts, key=counts.get)
print("Most frequent character:", most_frequent)
print("Frequency:", counts[most_frequent])
