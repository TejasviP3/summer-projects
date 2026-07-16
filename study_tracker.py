sessions = []

while True: 
    subject = input("Subject: ")

    if subject == "quit":
        break
    
    sessions.append(subject)

print(sessions)