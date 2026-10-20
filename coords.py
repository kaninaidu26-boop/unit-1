visited_cells = {(1, 0), (1, 1)}
visited_cells.add((2, 1))
visited_cells.add((1, 0))

print(visited_cells)
print("total cells:", len(visited_cells))
print("(2, 1) visited?", (2, 1) in visited_cells)
print("(5, 5) visited?", (5, 5) in visited_cells)

#----------------------------------------------------

errors = ["E3", "E5", "E3", "E4", "E5"]
print("original errors:", errors)
print("different errors:", set(errors))
print("number of unique errors:", len(set(errors)))

#----------------------------------------------------

location = (6.5, 3.2)
print(location, type(location))

a, b = location
print("x =", a, "| y =", b)

single_value = (8,)
print(single_value, type(single_value))

#----------------------------------------------------

# Simulate a robot visiting grid cells

cells = set()

cells.add((1, 0))
cells.add((1, 1))
cells.add((1, 2))
cells.add((2, 0))
cells.add((1, 1))
cells.add((2, 1))
cells.add((2, 2))
cells.add((1, 0))

print("visited cells:", cells)
print("distinct cells:", len(cells))
print("(3, 3) visited?", (3, 3) in cells)
