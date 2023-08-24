print("WELCOME TO KBC GAME!")

def kbc():
    questions = [
        "What is the IT capital of India?",
        "Which language is widely used in AI?",
        "How many bits make a byte??",
        "The System unit is referred to as the?",
    ]
     

    options = [
        ["A) Delhi", "B) Hyderabad", "C) Bangalore", "D) Pune"],
        ["A) Python", "B) C++", "C) Javascript", "D) Java"],
        ["A) 16", "B) 8", "C) 24", "D) 12"],
        ["A) The Heart of the Computer", "B) Central Processing Unit", "C) The hard drive", "D) System Software"],
    ]

    answers = [3, 1, 2, 1]  # Index of correct options (starting from 1)

    prize_money = [1000, 5000, 10000, 50000]  # Prize money for each level

    total_prize = 0

    
    for level in range(len(questions)):

        print(f"\nLevel {level + 1}: {questions[level]}")
        
        for option in options[level]:
            print(option)

        Input = input("Enter your answer (A/B/C/D): ").upper()
        
        if Input == 'A':
            answer = 1
        elif Input == 'B':
            answer = 2
        elif Input == 'C':
            answer = 3
        elif Input == 'D':
            answer = 4
        else:
            print("Invalid input. Please choose A, B, C, or D.")
            continue
        
        if answer == answers[level]:
            print("Correct answer!")
            total_prize += prize_money[level]
        else:
            print("Wrong answer. Game over!")
            break
        
        print(f"Total prize money so far: {total_prize}")

    print(f"\nCongratulations! You won {total_prize} rupees!")

kbc()
