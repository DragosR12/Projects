import random
player_score=0
computer_score=0
while True:
 choices=["rock","paper","scissors"]
 computer=random.choice(choices)
 player= None
 while player not in choices:
    player = input("Choose rock, paper or scissors: ").lower()
 else:
    print("player: "+player)
    print("computer: "+computer)

 if computer==player :
    print("Tie!")
 elif computer =="rock" and player =="paper":
    print("You win!")
    player_score +=1
 elif computer =="rock" and player =="scissors":
    print("You lose!")
    computer_score += 1
 elif computer == "paper" and player == "scissors":
    print("You win!")
    player_score += 1
 elif computer =="paper" and player =="rock":
    print("You lose!")
    computer_score += 1
 elif computer == "scissors" and player == "paper":
    print("You lose!")
    computer_score += 1
 elif computer == "scissors" and player == "rock":
    print("You win!")
    player_score += 1

 print("The score: " + str(player_score)+":"+str(computer_score))


 play_again=input("play again? (yes/no): ").lower()
 if play_again != "yes":
    print("ok!Bye!")
    break