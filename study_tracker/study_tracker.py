print("This is a study tracker.")
print("Input a subject and the amount of time it was studied to begin. \nTo finish entering subjects, type \"quit\".")

sessions = []

while True: 
    subject = input("Subject: ")

    if subject == "quit":
        break
    
    minutes = int(input("Minutes studied: "))
    sessions.append((subject, minutes))

print("List of subjects:", sessions)

total_mins = 0

for subject, minutes in sessions:
    total_mins += minutes

print("Total minutes studied:", total_mins, "minutes")

most_studied = ""
highest_time = 0

for subject, minutes in sessions:
    if minutes > highest_time:
        highest_time = minutes
        most_studied = subject

print("Your most-studied subject was", most_studied, "which you studied for", highest_time, "minutes")