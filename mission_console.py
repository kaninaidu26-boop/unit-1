readings = []

while True:
    print("\n1- Add reading  2- Show readings  3- Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        value = float(input("Enter sensor value: "))
        readings.append(value)
        print("Reading added")

    elif choice == "2":
        print("Readings:", readings)
        print("Total readings:", len(readings))

    elif choice == "3":
        print("Console closed")
        break

    else:
        print("Invalid choice")
