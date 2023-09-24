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


def clear():
    os.system("cls")

def print_field(field_data):
    clear()
    print("\n",field_data[0],field_data[1],field_data[2],"\n",field_data[3],field_data[4],field_data[5],"\n",field_data[6],field_data[7],field_data[8],"\n")
    time.sleep(0.1)

def check_draw(field=list):
    count = field.count(EMPTY)
    if count == 0:
        print_field(field)
        return True

def get_valid_pos_autoselect(field=list):

    while True:    
        
        pos = random.randint(0,8)
        if field[pos] == EMPTY:
            #print(f"Chose {pos}")
            return pos
            
        else:
            pass
            #print(f"Chose: {pos}")
            

    
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
        char1 = colored("[X]","red")
        char2 = colored("[O]","blue")
    else:
        char1 = colored("[O]","red")
        char2 = colored("[X]","blue")
    
    while True:
        
        ##  SIMULATION MODE ##
        if gamemode == GAMEMODE[0]:
        
            draw = check_draw(field)
            if draw == True:
                print_field(field)
                print(colored("DRAW","magenta"))
                time.sleep(2)
                break
            
            else:
                player1 = get_valid_pos_autoselect(field)
                
            field[player1] = char1
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

            draw = check_draw(field)
            if draw == True:
                print_field(field)
                print(colored("DRAW","magenta"))
                time.sleep(1)
                break
            
            else:
                player2 = get_valid_pos_autoselect(field)
                
            field[player2] = char2
            #print(f"Spieler O hat das Kästchen {player2} gewählt")
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


        ##  PLAYER VERSUS COMPUTER  ##
        
        elif gamemode == GAMEMODE[1]:
            print("[+] DEBUG:\tGAMEMODE PVC SELECTED, NOW STARTING GAME.")

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
                
                selection = get_valid_pos_autoselect(field)
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
                
                selection = get_valid_pos_autoselect(field)
                field[selection] = char1
                
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
gamecount = random.randint(1,20)
print(f"Playing {gamecount} rounds.\n\n")
time.sleep(2)
print(f"Please select the Gamemode:\n{GAMEMODE[0]} : 1\n{GAMEMODE[1]} : 2\n{GAMEMODE[2]} : 3")

while True:
    try:
        gamemode = int(input("(1,2,3):\t")) -1
        print(f"[+] DEBUG:\tYOU CHOSE: {GAMEMODE[gamemode]}")
        if gamemode < 0 or gamemode >= 3:
            raise Exception
        else:
            gamemode = GAMEMODE[gamemode]
            break
    except Exception:
        print("Please only select 1,2 or 3 as an option!")


while GAME == True:
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
        GAME = False
        
clear()
print(f"\nRESULTS:\nX\t:\t{WINS[0]}\nO\t:\t{WINS[1]}\nDRAW\t:\t{WINS[2]}\n")