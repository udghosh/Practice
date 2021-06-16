from random import randint
# dictionary for Snakes
snakes = { 17:7, 54:34, 62:19, 98:79 }

#dictionary for Ladder
ladder = { 3:38, 24:33, 42:93, 72:84 }


# Game board consisting of numbers in List from 1 to 100
game_board = list(range(1, 101))

player1_points = 0
player2_points = 0
manual_play = [str(i) for i in list(range(1,21))]

print("##### Welcome to Snake & Ladders Game #####")
player1_name = input("Player1 enter your name:")
player2_name = input("Player2 enter your name:")
flag = 1

print("##### Let us Start #####")
while player1_points < len(game_board) and player2_points < len(game_board):
    dice = 0
    # palyer1 plays
    if flag == 1:     
        turn1 = input(player1_name + ":")
        if turn1 == 'roll':
            dice = randint(1,6)
            if player1_points + dice <= 100:
                player1_points += dice
            else:
                print('Out of Board')
                flag = 2
                continue    
            if player1_points == 100:
                print(player1_name + " " + "won the game" + "\n" + "##### Game Successfuly Fnished #####")
                break
            elif player1_points < 100:
                for key in snakes:
                    if player1_points == key and flag == 1:#snake bite
                        player1_points = snakes[key]
                        print(" Snake bite " + player1_name + " Your Final Position is " + str(player1_points))
                        flag = 2
                        break
                for key in ladder:
                    if player1_points == key and flag == 1:#ladder climb
                        player1_points = ladder[key]
                        print(" Ladder Climb " + player1_name + " Your Final Position is " + str(player1_points))
                        flag = 2
                        break  
                if flag == 1:
                    print(player1_name + "Your Final Position is " + str(player1_points))
                    flag = 2      
        elif turn1 in manual_play:
            dice = int(turn1)
            if player1_points + dice <= 100:
                player1_points += dice
            else:
                print('Out of Board')
                flag = 2
                continue    
            if player1_points == 100:
                print(player1_name + ' ' + "won the game" + "\n" + "##### Game Successfuly Fnished #####")
                break
            elif player1_points < 100:
                for key in snakes:
                    if player1_points == key and flag == 1:#snake bite
                        player1_points = snakes[key]
                        print(" Snake bite " + player1_name + " Your Final Position is " + str(player1_points))
                        flag = 2
                        break
                for key in ladder:
                    if player1_points == key and flag == 1:#ladder climb
                        player1_points = ladder[key]
                        print(" Ladder Climb " + player1_name + " Your Final Position is " + str(player1_points))
                        flag = 2
                        break  
                if flag == 1:
                    print(player1_name + " Your Final Position is " + str(player1_points))
                    flag = 2
        elif turn1 == 'quit' and flag == 1:
            print('Game Terminated !' + ' ' + player2_name + ' ' + 'Wins. ') 
            break            
        else:
            print("\nInvalid Input Please Try Again")
    if flag == 2:
        turn2 = input(player2_name + ":")
        if turn2 == 'roll':
            dice = randint(1,6)
            if player2_points + dice <= 100:
                player2_points += dice
            else:
                print('Out of Board')
                flag = 1
                continue    
            if player2_points == 100:
                print(player2_name + ' ' + "won the game" + "\n" + "##### Game Successfuly Fnished #####")
                break
            elif player2_points < 100:
                for key in snakes:
                    if player2_points == key and flag == 2:#snake bite
                        player2_points = snakes[key]
                        print(" Snake bite " + player2_name + " Your Final Position is " + str(player2_points))
                        flag = 1
                        break
                for key in ladder:
                    if player2_points == key and flag == 2:#ladder climb
                        player2_points = ladder[key]
                        print(" Ladder Climb " +  player2_name + " Your Final Position is " + str(player2_points))
                        flag = 1
                        break  
                if flag == 2:
                    print(player2_name + " Your Final Position is " + str(player2_points))
                    flag = 1      
        elif turn2 in manual_play:
            dice = int(turn2)
            if player2_points + dice <= 100:
                player2_points += dice
            else:
                print('Out of Board')
                flag = 1
                continue    
            if player2_points == 100:
                print(player2_name + ' ' + "won the game" + "\n" + "##### Game Successfuly Fnished #####")
                break
            elif player2_points < 100:
                for key in snakes:
                    if player2_points == key and flag == 2:#snake bite
                        player2_points = snakes[key]
                        print("Snake bite " + player2_name + " Your Final Position is " + str(player2_points))
                        flag = 1
                        break
                for key in ladder:
                    if player2_points == key and flag == 2:#ladder climb
                        player2_points = ladder[key]
                        print(" Ladder Climb " + player2_name + " Your Final Position is " + str(player2_points))
                        flag = 1
                        break  
                if flag == 2:
                    print(player2_name + " Your Final Position is " + str(player2_points))
                    flag = 1 
        elif turn2 == 'quit' and flag == 2:
            print('Game Terminated !' + ' ' + player1_name + ' ' + 'Wins. ') 
            break               
        else:
            print("\nInvalid Input Please Try Again")





