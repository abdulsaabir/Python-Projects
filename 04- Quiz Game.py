print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()

print("Okay! Let's play :)")
score = 0
QuestAns = {
    "cpu": "central processing unit",
    "gpu": "graphics processing unit",
    "ram": "random access memory",
    "psu": "power supply",
    "hdd": "hard disk drive",
    "ssd": "solid state drive",
    "os": "operating system",
    "lan": "local area network",
    "wan": "wide area network",
    "usb": "universal serial bus"
}

for key,value in QuestAns.items():
    ans = input(f"What does {key} stand For?:  ").strip()
    if ans.lower() == value:
        print('Correct!')
        score += 1
    else: 
        print("Incorrect!")

percentage_correct = (score / len(QuestAns)) * 100
print("\nYou got", score, "questions correct!")
print("You got {:.2f}%.".format(percentage_correct))