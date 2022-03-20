import random

class Player():
    def __init__(self):
        self.total_score = 90

    def accum(self, score):
        self.total_score += score

        
def referee(player_name, score):
    if score >= 100:
        print(f"The winner is {player_name} with {score}.")
        exit()


def roll_the_die() -> int:
    Die = random.randint(1,6)
    return Die


def turn_control(Player_1,Player_2):
    someone_won = False
    Player_1_End = False
    Player_2_End = False
    current_turn = 1
    player_1_temp_score = 0
    player_2_temp_score = 0
    print("First turn starts with Player 1.\n")

    while someone_won == False:
        while Player_1_End == False:
            print("Player 1")
            current_die_num = roll_the_die()
            print(f"Die result is {current_die_num}.")
            if current_die_num == 1:
                print("No score accumulated.\n")
                player_1_temp_score = 0
                break
            else:
                player_1_temp_score += current_die_num
                user_input = input('Do you wish to roll or hold? r/h: \n')
                print(f"Player 1 score of this turn: {player_1_temp_score}\n\n")
                if user_input == 'r':
                    Player_1_End = False
                elif user_input == 'h':
                    Player_1.accum(player_1_temp_score)
                    player_1_temp_score = 0
                    referee("Player 1",Player_1.total_score)
                    break
     
        while Player_2_End == False:
            print("Player 2")
            current_die_num = roll_the_die()
            print(f"Die result is {current_die_num}.")
            if current_die_num == 1:
                print("No score accumulated.\n")
                print("End of turn.\n")
                player_2_temp_score = 0
                break
            else:
                player_2_temp_score += current_die_num
                user_input = input('Do you wish to roll or hold? r/h: \n')
                print(f"Player 2 score of this turn: {player_2_temp_score}\n")
                if user_input == 'r':
                    Player_2_End = False
                elif user_input == 'h':
                    Player_2.accum(player_2_temp_score)
                    player_2_temp_score = 0
                    referee("Player 2",Player_2.total_score)
                    break
        print(f"Player 1 score: {Player_1.total_score}")
        print(f"Player 2 score: {Player_2.total_score}\n\n")
        current_turn += 1
        print(f"Turn: {current_turn}\n")
        

def main():
    Player_1 = Player()
    Player_2 = Player()

    turn_control(Player_1, Player_2)


if __name__ == "__main__":
    main()
    
