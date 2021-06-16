from random import randint
# dictionary for Snakes
snakes = { 17:7, 54:34, 62:19, 98:79 }

#dictionary for Ladder
ladder = { 3:38, 24:33, 42:93, 72:84 }

# funtion to check Snake and Ladder
def ladder_snake(player , points) :
    points_final = 0
    for key in snakes:
        if points == key :#snake bite
            points_final = snakes[key]
            print("OH NO !!! Snake bite " + player + " Your Final Position is " + str(points_final))
            return(points_final)
    for key in ladder:
        if points == key :#ladder climb
            points_final = ladder[key]
            print("Hurrah !!! Ladder Climb " + player + " Your Final Position is " + str(points_final))
            return(points_final)

    # Neighter Snake bite or Ladder Climb
    print(player + " Your Final Position is " + str(points))
    return(points)

# Game board consisting of numbers in List from 1 to 100
game_board = list(range(1, 101))

player1_points = 0
player2_points = 0
manual_play = [str(i) for i in list(range(1,21))]

print("##### UDAY Welcome's You to Snake & Ladder Game #####")
player1_name = input("Player1 enter your name:")
player2_name = input("Player2 enter your name:")

flag =1

print("##### Game Started Hold Tight!!!! #####")
while player1_points < len(game_board) and player2_points < len(game_board):
    dice = 0
    # palyer1 plays
    if flag == 1:     
        turn1 = input(player1_name + " : ")
        if turn1 == 'roll':
            dice = randint(1,6)
            if player1_points + dice <= 100:
                player1_points += dice
            else:
                print('Sorry !!!! Number Out of Board, Chance Aborted !!!!')
                flag = 2
                continue    
            if player1_points == 100:
                print(player1_name + " " + "Won The Game" + "\n" + "##### Game Successfully Finished #####" + "\n" + "Goodbye!!!")
                break
            elif player1_points < 100:
                # fUNCTION TO CHECK LADDER OR SNAKE BITE
                if flag == 1:
                   flag =2
                   player1_points = ladder_snake(player1_name , player1_points)
                
        elif turn1 in manual_play:
            dice = int(turn1)
            if player1_points + dice <= 100:
                player1_points += dice
            else:
                print('Sorry !!!! Number Out of Board, Chance Aborted !!!!')
                flag = 2
                continue    
            if player1_points == 100:
                print(player1_name + " " + "Won The Game" + "\n" + "##### Game Successfully Finished #####" + "\n" + "Goodbye!!!")
                break
            elif player1_points < 100:
                # fUNCTION TO CHECK LADDER OR SNAKE BITE
                if flag == 1 :
                    flag = 2
                    player1_points = ladder_snake(player1_name , player1_points)
                
        elif turn1 == 'quit' and flag == 1:
            print('Game Terminated !' + ' ' + player2_name + ' ' + 'Wins. ') 
            break            
        else:
            print("\nInvalid Input Please Try Again")
            continue
    if flag == 2:
        turn2 = input(player2_name + " : ")
        
        if turn2 == 'roll':
            dice = randint(1,6)
            if player2_points + dice <= 100:
                player2_points += dice
                
            else:
                print('Sorry !!!! Number Out of Board, Chance Aborted !!!!')
                flag = 1
                continue  
            if player2_points == 100:
                print(player2_name + " " + "Won The Game" + "\n" + "##### Game Successfully Finished #####" + "\n" + "Goodbye!!!")
                break
            elif player2_points < 100:
                # fUNCTION TO CHECK LADDER OR SNAKE BITE
                if flag == 2:
                    flag = 1
                    player2_points = ladder_snake(player2_name , player2_points)
                
        elif turn2 in manual_play:
            dice = int(turn2)
            if player2_points + dice <= 100:
                player2_points += dice
            else:
                print('Sorry !!!! Number Out of Board, Chance Aborted !!!!')
                flag = 1
                continue    
            if player2_points == 100:
                print(player2_name + " " + "Won The Game" + "\n" + "##### Game Successfully Finished #####" + "\n" + "Goodbye!!!")
                break
            elif player2_points < 100:
                # fUNCTION TO CHECK LADDER OR SNAKE BITE
                if flag == 2:
                    flag = 1
                    player2_points = ladder_snake(player2_name , player2_points)
                
        elif turn2 == 'quit' and flag == 2:
            print('Game Terminated !' + ' ' + player1_name + ' ' + 'Wins. ') 
            break               
        else:
            print("\nInvalid Input Please Try Again")
            continue




