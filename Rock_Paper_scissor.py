import random
   
while True:
    my_turn=str(input("enter your answer(choose from Rock, Paper, Scissors):"))
    my_turn=my_turn.lower()
    my_list=["rock", "paper", "scissors"]
    comp_turn=random.choice(my_list)
    my_turn = str(my_turn)
    comp_turn=str(comp_turn)
    
    if my_turn !="rock" and my_turn !="paper" and my_turn!="scissors":
       print("please check your answer")
       continue


    print("your answer is", my_turn)
    print("computer answer is", comp_turn)

    
    if my_turn==comp_turn:
      print("both tie, try again :")
    
    elif my_turn=="rock" and comp_turn=="paper":
      print("you loose, try again :")
      continue


    elif my_turn=="rock" and comp_turn=="scissors":
      print("you Won")
      break 

    elif my_turn=="paper" and comp_turn =="rock":
       print("you won")
       break

    elif my_turn=="paper" and comp_turn =="scissors":
       print("you loose, try again:")
       continue


    elif my_turn=="scissors" and comp_turn =="rock":
       print("you loose, try again")
       continue


    elif my_turn=="scissors" and comp_turn =="paper":
       print("you won")
       break
    
   
    


