import random
import argparse

class Player():
    def __init__(self):
        self.total_score = 0

    def accum(self, score):
        self.total_score += score

        
def referee(player_name, score):
    if score >= 100:
        print(f"The winner is {player_name}.")
        return 1
    
    else:
        return 0
    

def roll_the_die() -> int: #Rolls the die and send score to computer, return score to accum if not 1.
    Die = random.randint(1,6)
    return Die


def turn_control(Player_1,Player_2):
    someone_won = False
    Player_1_End = False
    Player_2_End = False
    Turn = 1
    temp_score = 0
    print("First turn starts with Player 1.\n")

    while someone_won == False:
        print(f"Turn {Turn}")
        while Player_1_End == False:
            print("Player 1")
            current_die_num = roll_the_die()
            print(f"Die result is {current_die_num}.")
            if current_die_num == 1:
                print("Die result is 1. No score accumulated.\n")
                print("End of turn.\n")
                Player_1_End = True
            else:
                temp_score += current_die_num
                user_input = input('Do you wish to continue? Y/N: \n')
                print(f"Temp score: {temp_score}")
                if user_input == 'Y' and user_input == 'y':
                    Player_1_End = False
                else:
                    Player_1.accum(temp_score)
                    Player_1_End = True
            if referee("Player 1",Player_1.total_score) == 1:
                print("Winner is Player 1!")
                someone_won = True

        temp_score = 0
        while Player_2_End == False:
            print("Player 2")
            current_die_num = roll_the_die()
            print(f"Die result is {current_die_num}.")
            if current_die_num == 1:
                print("Die result is 1. No score accumulated.\n")
                print("End of turn.\n")
                Player_1_End = True
            else:
                temp_score += current_die_num
                user_input = input('Do you wish to continue? Y/N: \n')
                print(f"Temp score: {temp_score}")
                if user_input == 'Y' and user_input == 'y':
                    Player_2_End = False
                else:
                    Player_2.accum(temp_score)
                    Player_2_End = True
            if referee("Player 1",Player_2.total_score) == 1:
                print("Winner is Player 2!")
                someone_won = True
        
        Turn += 1
        
               

def main():
    Player_1 = Player()
    Player_2 = Player()

    turn_control(Player_1, Player_2)


        

if __name__ == "__main__":
    main()
    
