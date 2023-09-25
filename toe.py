import random
import time
import os

## Autoinstalling termcolor if it is not yet available
try:
    from termcolor import colored
except:
    os.system("pip install termcolor")


GAME = True
WINS = [0,0,0]
GAMEMODE = ["simulation","pvc","pvp"]
EMPTY = "[ ]"
QUICK_MODE = bool
COMPUTER1_STRATEGY = 1
COMPUTER2_STRATEGY = 0
WAIT_TIME = 0
DEBUG = False
PRINT_WAIT_TIME = 0

def clear():
    os.system("cls")

def print_field(field_data):
    if DEBUG == True:
        print("\n",field_data[0],field_data[1],field_data[2],"\n",field_data[3],field_data[4],field_data[5],"\n",field_data[6],field_data[7],field_data[8],"\n")
        time.sleep(PRINT_WAIT_TIME)
    if QUICK_MODE == True:
        pass
    else:
        clear()
        print("\n",field_data[0],field_data[1],field_data[2],"\n",field_data[3],field_data[4],field_data[5],"\n",field_data[6],field_data[7],field_data[8],"\n")
        time.sleep(PRINT_WAIT_TIME)

def check_draw(field=list):
    count = field.count(EMPTY)
    if count == 0:
        print_field(field)
        return True

def strategy_random(field=list):

    while True:    
        
        pos = random.randint(0,8)
        if field[pos] == EMPTY:
            #print(f"Chose {pos}")
            return pos
            
        else:
            pass
            #print(f"Chose: {pos}")

def strategy_corners(field=list):

    while True:

        #   VALUES
        pos = 0

        #   favour positions
        favour = [0,2,6,8]
        wincondition = [[0,2,1],[0,6,3],[0,8,4],
                        [2,6,4],[2,8,5],[6,8,7],
                        [3,5,4],[1,7,4],[0,1,2],
                        [6,7,8],[7,8,6],[4,5,3],
                        [1,2,0],[0,3,6],[1,4,7],
                        [2,5,8],[6,3,0],[7,4,1],
                        [5,8,2],[0,4,8],[4,8,0],
                        [2,4,6],[3,4,5],[6,4,2]]

        #   Check if a favour position is available:
        for y in range(0,len(wincondition)):
            z = wincondition[y]
            if DEBUG == True:
                print(f"[+] DEBUG : z is : {z}\nFIELD[z[0]] is : {field[z[0]]}\nFIELD[z[1]] is : {field[z[1]]}\nFIELD[z[2]] is : {field[z[2]]}\nY is currently at {y}")
                if QUICK_MODE == False:
                    time.sleep(0.3)
            if (field[z[0]] == field[z[1]]) and (field[z[2]] == EMPTY) and not field[z[0]] == EMPTY:
                if DEBUG == True:
                    print(colored(f"[!]\tFOUND A WINNING CONDITION {z}\nGoing for field: {z[2]}","magenta"))
                    if QUICK_MODE == False:
                        time.sleep(1)
                return z[2]
            elif field[4] == EMPTY:
                if DEBUG == True:
                    print(colored("Good condition found, middle is open:","green"))
                    print("[!]\tTOOK MIDDLE POSITION")
                    if QUICK_MODE == False:
                        time.sleep(1)
                return 4
        

        #   Check for open corners:
        for x in range(0,len(favour)):
            x = random.randint(0,3)
            if field[favour[x]] == EMPTY:
                if DEBUG == True:
                    print(colored("No winning condition found:","red"))
                    print("[!]\tTOOK OPEN CORNER")
                    if QUICK_MODE == False:
                        time.sleep(1)
                return favour[x]

        pos = random.randint(0,8)
        if field[pos] == EMPTY:
            if DEBUG == True:
                print(colored("No winning condition found:","red"))
                print("[!]\tTOOK RANDOM POSITION")
                if QUICK_MODE == False:
                    time.sleep(1)
            return pos
        else:
            continue

    
def check_win(field):
    Players = ["[X]","[O]"]
    
    for i in Players:
        #print(f"Test für spieler {i}")
        
        if i in field[0] and i in field[1] and i in field[2]:
            #print("Rule1")
            field[0] = colored(f"{i}","green")
            field[1] = colored(f"{i}","green")
            field[2] = colored(f"{i}","green")
            return colored(f"Player {i} won the game!","green"), True
        
        elif i in field[3] and i in field[4] and i in field[5]:
            #print("Rule2")
            field[3] = colored(f"{i}","green")
            field[4] = colored(f"{i}","green")
            field[5] = colored(f"{i}","green")
            return colored(f"Player {i} won the game!","green"), True
        
        elif i in field[6] and i in field[7] and i in  field[8]:
            #print("Rule3")
            field[6] = colored(f"{i}","green")
            field[7] = colored(f"{i}","green")
            field[8] = colored(f"{i}","green")
            return colored(f"Player {i} won the game!","green"), True
        
        elif i in field[0] and i in field[3] and i in field[6]:
            #print("Rule4")
            field[0] = colored(f"{i}","green")
            field[3] = colored(f"{i}","green")
            field[6] = colored(f"{i}","green")
            return colored(f"Player {i} won the game!","green"), True
        
        elif i in field[1] and i in field[4] and i in field[7]:
            #print("Rule5")
            field[1] = colored(f"{i}","green")
            field[4] = colored(f"{i}","green")
            field[7] = colored(f"{i}","green")
            return colored(f"Player {i} won the game!","green"), True
        
        elif i in field[2] and i in field[5] and i in field[8]:
            #print("Rule6")
            field[2] = colored(f"{i}","green")
            field[5] = colored(f"{i}","green")
            field[8] = colored(f"{i}","green")
            return colored(f"Player {i} won the game!","green"), True
        
        elif i in field[0] and i in field[4] and i in field[8]:
            #print("Rule7")
            field[0] = colored(f"{i}","green")
            field[4] = colored(f"{i}","green")
            field[8] = colored(f"{i}","green")
            return colored(f"Player {i} won the game!","green"), True
        
        elif i in field[2] and i in field[4] and i in field[6]:
            #print("Rule8")
            field[2] = colored(f"{i}","green")
            field[4] = colored(f"{i}","green")
            field[6] = colored(f"{i}","green")            
            return colored(f"Player {i} won the game!","green"), True
        
        else:
            continue
        
    return "",False


def players_turn(players_char,field):
    #   Players turn
        
    while True:
        try:
            player_selection = int(input("Please select a location to put your [X] in (1-9):\t")) -1
            if (player_selection > 9) or (player_selection < 0):
                raise Exception
            else:
                if field[player_selection] == EMPTY:
                    return player_selection
                    
                else:
                    print("Field already occupied!")
                    time.sleep(1)
                    clear()
                    print_field(field)
                    continue
        except:
            print("Please only select numbers from 1 to 9!")    
            time.sleep(1)
            clear()
            print_field(field)
    


def play(field, who_starts, gamemode):
    
    if who_starts == 0:
        start_player = 1
        char1 = colored("[X]","red")
        char2 = colored("[O]","blue")
    else:
        start_player = 2
        char1 = colored("[X]","blue")
        char2 = colored("[O]","red")
    
    while True:
        
        ##  SIMULATION MODE ##
        if gamemode == GAMEMODE[0]:
        
            if start_player == 1:
                draw = check_draw(field)
                if draw == True:
                    print_field(field)
                    print(colored("DRAW","magenta"))
                    if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                    time.sleep(WAIT_TIME)
                    break
                
                else:
                    if COMPUTER1_STRATEGY == 0:
                        player1 = strategy_random(field)
                    else:
                        player1 = strategy_corners(field)
                    
                field[player1] = char1
                player, win = check_win(field)
                if win == True:   
                    print_field(field)
                    print(player)
                    time.sleep(WAIT_TIME)
                    if "X" in player:
                        if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                        return "X"
                    elif "O" in player:
                        if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                        return "O"
                else:
                    print_field(field)

                draw = check_draw(field)
                if draw == True:
                    print_field(field)
                    print(colored("DRAW","magenta"))
                    if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                    time.sleep(WAIT_TIME)
                    break
                
                else:
                    if COMPUTER2_STRATEGY == 0:
                        player2 = strategy_random(field)
                    else:
                        player2 = strategy_corners(field)
                    
                field[player2] = char2
                #print(f"Spieler O hat das Kästchen {player2} gewählt")
                player, win = check_win(field)
                
                if win == True:
                    print_field(field)
                    print(player)
                    time.sleep(WAIT_TIME)
                    if "X" in player:
                        if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                        return "X"
                    elif "O" in player:
                        if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                        return "O"
                else:            
                    print_field(field)

            if start_player == 2:

                draw = check_draw(field)
                if draw == True:
                    print_field(field)
                    print(colored("DRAW","magenta"))
                    if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                    time.sleep(WAIT_TIME)
                    break
                
                else:
                    if COMPUTER2_STRATEGY == 0:
                        player2 = strategy_random(field)
                    else:
                        player2 = strategy_corners(field)
                    
                field[player2] = char2
                player, win = check_win(field)
                if win == True:   
                    print_field(field)
                    print(player)
                    time.sleep(WAIT_TIME)
                    if "X" in player:
                        if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                        return "X"
                    elif "O" in player:
                        if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                        return "O"
                else:
                    print_field(field)

                draw = check_draw(field)
                if draw == True:
                    print_field(field)
                    print(colored("DRAW","magenta"))
                    if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                    time.sleep(WAIT_TIME)
                    break
                
                else:
                    if COMPUTER1_STRATEGY == 0:
                        player1 = strategy_random(field)
                    else:
                        player1 = strategy_corners(field)
                    
                field[player1] = char1
                #print(f"Spieler O hat das Kästchen {player2} gewählt")
                player, win = check_win(field)
                
                if win == True:
                    print_field(field)
                    print(player)
                    time.sleep(WAIT_TIME)
                    if "X" in player:
                        if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                        return "X"
                    elif "O" in player:
                        if DEBUG == True:
                            print_field(field)
                            input("Enter to continue:")
                        return "O"
                else:            
                    print_field(field)

        ##  PLAYER VERSUS COMPUTER  ##
        
        elif gamemode == GAMEMODE[1]:
            QUICK_MODE = False
            #print("[+] DEBUG:\tGAMEMODE PVC SELECTED, NOW STARTING GAME.")
            if who_starts == 0:

                #   Players turn
                draw = check_draw(field)
                if draw == True:
                    print_field(field)
                    print(colored("DRAW","magenta"))
                    time.sleep(2)
                    break
                else:
                    print_field(field)
                    
                selection = players_turn(char1,field)
                field[selection] = char1
                
                player, win = check_win(field)
                if win == True:   
                    print_field(field)
                    print(player)
                    time.sleep(1)
                    if "X" in player:
                        return "X"
                    elif "O" in player:
                        return "O"
                else:
                    print_field(field)
                    time.sleep(1)
                
            
                #   Computers turn
                draw = check_draw(field)
                if draw == True:
                    print_field(field)
                    print(colored("DRAW","magenta"))
                    time.sleep(2)
                    break
                else:
                    print_field(field)
                
                if COMPUTER1_STRATEGY == 0:
                    selection = strategy_random(field)
                else:
                    selection = strategy_corners(field)

                field[selection] = char2
                
                player, win = check_win(field)
                if win == True:   
                    print_field(field)
                    print(player)
                    time.sleep(1)
                    if "X" in player:
                        return "X"
                    elif "O" in player:
                        return "O"
                else:
                    print_field(field)
                
            else:
                
                if COMPUTER1_STRATEGY == 0:
                    selection = strategy_random(field)
                else:
                    selection = strategy_corners(field)
                field[selection] = char1

                player, win = check_win(field)
                if win == True:   
                    print_field(field)
                    print(player)
                    time.sleep(1)
                    if "X" in player:
                        return "X"
                    elif "O" in player:
                        return "O"
                else:
                    print_field(field)
                    time.sleep(1)
                
                #   Players turn
                draw = check_draw(field)
                if draw == True:
                    print_field(field)
                    print(colored("DRAW","magenta"))
                    time.sleep(2)
                    break
                else:
                    print_field(field)
                    
                selection = players_turn(char2,field)
                field[selection] = char2
                
                player, win = check_win(field)
                if win == True:   
                    print_field(field)
                    print(player)
                    time.sleep(1)
                    if "X" in player:
                        return "X"
                    elif "O" in player:
                        return "O"
                else:
                    print_field(field)
                    time.sleep(1)
                  
        elif gamemode == GAMEMODE[2]:
            QUICK_MODE = False
            ##  PVP ##
            #   Player1's turn
            draw = check_draw(field)
            if draw == True:
                print_field(field)
                print(colored("DRAW","magenta"))
                time.sleep(2)
                break
            else:
                print_field(field)
                
            selection = players_turn(char1,field)
            field[selection] = char1
            
            player, win = check_win(field)
            if win == True:   
                print_field(field)
                print(player)
                time.sleep(1)
                if "X" in player:
                    return "X"
                elif "O" in player:
                    return "O"
            else:
                print_field(field)
                time.sleep(1)
                
            #   Player2's turn
            draw = check_draw(field)
            if draw == True:
                print_field(field)
                print(colored("DRAW","magenta"))
                time.sleep(2)
                break
            else:
                print_field(field)
                
            selection = players_turn(char2,field)
            field[selection] = char2
            
            player, win = check_win(field)
            if win == True:   
                print_field(field)
                print(player)
                time.sleep(1)
                if "X" in player:
                    return "X"
                elif "O" in player:
                    return "O"
            else:
                print_field(field)
                time.sleep(1)

## START ###

count = 0
gamecount = 1000 #random.randint(1,20)
print(f"Playing {gamecount} rounds.\n\n")
time.sleep(2)

####### GAMEMODE SELECTION #########
print(f"Please select the Gamemode:\n{GAMEMODE[0]} : 1\n{GAMEMODE[1]} : 2\n{GAMEMODE[2]} : 3")
while True:
    try:
        gamemode = int(input("(1,2,3):\t")) -1
        #print(f"[+] DEBUG:\tYOU CHOSE: {GAMEMODE[gamemode]}")
        if gamemode < 0 or gamemode >= 3:
            raise Exception
        else:
            gamemode = GAMEMODE[gamemode]
            break
    except Exception:
        print("Please only select 1,2 or 3 as an option!")


if gamemode == GAMEMODE[0]:
    while True:
        try:
            COMPUTER1_STRATEGY = int(input("Please select the Strategy (0 : RANDOM\t1 : CORNERS) for Computer 1:\t"))
            COMPUTER2_STRATEGY = int(input("Please select the Strategy (0 : RANDOM\t1 : CORNERS) for Computer 2:\t"))
            QUICK_MODE = int(input("Do you want to use quickmode? (0 : No\t1 : Yes):\t"))
            DEBUG = input("Do you want to enable debug mode? (Default: False):\t")
            if DEBUG == None or DEBUG == "":
                DEBUG = False
            else:
                DEBUG = True
            if COMPUTER1_STRATEGY < 0 or COMPUTER1_STRATEGY > 1:
                raise Exception
            elif COMPUTER2_STRATEGY < 0 or COMPUTER2_STRATEGY > 1:
                raise Exception
            elif QUICK_MODE < 0 or QUICK_MODE > 1:
                raise Exception
            else:
                if QUICK_MODE == 1:
                    QUICK_MODE = True
                    WAIT_TIME = 0.05

                elif QUICK_MODE == 0:
                    QUICK_MODE = False
                    WAIT_TIME = 1
                    PRINT_WAIT_TIME = 0.3
                break
        except Exception:
            print("Please only select 0 or 1 as an option!\nOr choose True / False for debug mode")

elif gamemode == GAMEMODE[1]:
    QUICK_MODE = False
    while True:
        try:
            COMPUTER1_STRATEGY = int(input("Please select the Strategy (0 : RANDOM\t1 : CORNERS) for your Computer opponent:\t"))
            if COMPUTER1_STRATEGY < 0 or COMPUTER1_STRATEGY > 1:
                raise Exception
            else:
                break
        except Exception:
            print("Please only select 0 or 1 as an option!")

while GAME == True:
    try:
        count +=1
        field = [EMPTY,EMPTY,EMPTY,
                EMPTY,EMPTY,EMPTY,
                EMPTY,EMPTY,EMPTY]
        #print_field(field)
        
        start = count % 2
        
        try:
            if count % round((gamecount/10)) == 0:
                value = round(count / round((gamecount/100)))
                print(f"Reached {value}%")
                print(f"X\t:\t{WINS[0]}\nO\t:\t{WINS[1]}\nDRAW\t:\t{WINS[2]}\n")
        except:
            pass        
        winner = play(field,start,gamemode)
        if winner == "X":
            WINS[0] += 1
        elif winner == "O":
            WINS[1] += 1
        else:
            WINS[2] += 1
        
        if count >= gamecount:
            exit()
         
    except KeyboardInterrupt:
        clear()
        print("Goodbye!")
        time.sleep(0.5)
        exit()
    
clear()
print(f"\nRESULTS:\nX\t:\t{WINS[0]}\nO\t:\t{WINS[1]}\nDRAW\t:\t{WINS[2]}\n")
input()
exit()