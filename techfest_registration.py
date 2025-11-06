# TechFest Registration System A Python program that records event participants and analyzes track diversity.


# Task 1: Registration Setup
print("Welcome to SMIT TechFest!")
print("Event organized by Philip Andrei Teves of APPDAET BTCS2\n")

# Ask user how many participants will join
num_participants = int(input("How many participants will register? "))

if num_participants <= 0:
    print("Invalid number of participants.")
else:
    # Task 2: Collect Participant Information
    participants = []

    for i in range(num_participants):
        print()
        name = input("Enter participant name: ")
        track = input("Enter chosen track: ")

        record = {"name": name, "track": track}
        participants.append(record)

    print("\nRegistered Participants:")
    for i in range(num_participants):
        data = participants[i]
        print(f"{i + 1}. {data['name']} - {data['track']}")
    print()
    # Task 3: Track Diversity Report
    track_list = set()
    for p in participants:
        track_list.add(p["track"])

    print("Tracks offered in this event:")
    print(", ".join(track_list))
    print()

    if len(track_list) < 2:
        print("Not enough variety in tracks.\n")
    # Task 4: Duplicate Name Detection
    checked_names = set()
    found_duplicate = False

    for p in participants:
        name = p["name"]
        if name in checked_names:
            print(f"Duplicate name found: {name}")
            found_duplicate = True
        else:
            checked_names.add(name)

    if not found_duplicate:
        print("No duplicate names.")




