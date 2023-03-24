import random
   
while True:
#     taking input from the user.
    my_turn=str(input("enter your answer(choose from Rock, Paper, Scissors):"))
    my_turn=my_turn.lower()
    my_list=["rock", "paper", "scissors"]
    comp_turn=random.choice(my_list)
    my_turn = str(my_turn)
    comp_turn=str(comp_turn)
    
#     if the user enters incorrect word executes the following code.
    if my_turn !="rock" and my_turn !="paper" and my_turn!="scissors":
       print("please check your answer")
       continue

   
    print("your answer is", my_turn)
    print("computer answer is", comp_turn)

#     if your answer and computers answer are same.
    if my_turn==comp_turn:
      print("both tie, try again :")
    
#    if your answer is rock and computers answer is paper, you will be the winner.
    elif my_turn=="rock" and comp_turn=="paper":
      print("you loose, try again :")
      continue


#     if your answer is rock and computers answer is scissor, you will loose.
    elif my_turn=="rock" and comp_turn=="scissors":
      print("you Won")
      break 
#     if your answer is paper and computers answer is rock, you will be the winner
    elif my_turn=="paper" and comp_turn =="rock":
       print("you won")
       break

#     if your answer is paper and computers answer is scissor, you will loose.
    elif my_turn=="paper" and comp_turn =="scissors":
       print("you loose, try again:")
       continue

#     if your answer is scissor and computers answer is rock, you will loose.
    elif my_turn=="scissors" and comp_turn =="rock":
       print("you loose, try again")
       continue

#     if your answer is scissor and computers answer is paper, you will be the win.
    elif my_turn=="scissors" and comp_turn =="paper":
       print("you won")
       break
    
   
    


