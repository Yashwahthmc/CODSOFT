import random
choices=["rock","paper","scissors"]
def get_winner(user, computer):
    if user==computer:
        return "It's a tie!"
    elif (user=="rock"and computer=="scissors") or (user=="paper"and computer=="rock") or (user=="scissors"and computer=="paper"):
        return "You win!"
    else:
        return "Computer wins!"
print("🎮 Welcome to Rock,Paper,Scissors Game!")
while True:
    user_choice=input("Enter your choice (rock/paper/scissors or 'exit' to quit):").lower()
    if user_choice=='exit':
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid input.Try again.")
        continue
    computer_choice=random.choice(choices)
    print(f"You chose:{user_choice}")
    print(f"Computer chose:{computer_choice}")
    result=get_winner(user_choice,computer_choice)
    print("Result:",result)
