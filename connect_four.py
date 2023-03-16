import os
import sys

needed_for_win = 3
player_chars = ['o', 'x']

def make_art_bigger(character):
    if character == 'x':
        return_lst = [
            ['\\', " ", "/"],
            [' ', 'X', ' '],
            ['/', " ", "\\"]
        ]
        return return_lst
    
    elif character == 'o':
        return_lst = [
            [" ", "_", " "],
            ["|", " ", "|"],
            [" ", "‾", " "]
        ]
        return return_lst
    else:
        return_lst = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        return return_lst
    

def check_if_win(char, main_lst):
    opponents_char = 'x' if char == 'o' else 'o'

    for lst_counter, lst in enumerate(main_lst):
        for element_counter, element in enumerate(lst):
            if element == char:
                row_right = [lst[element_counter + i] for i in range(needed_for_win)] if element_counter <= len(lst) - needed_for_win else ['-']
                if '-' not in row_right and opponents_char not in row_right:
                    return True
                column_up = [main_lst[lst_counter + i][element_counter] for i in range(needed_for_win)] if lst_counter <= len(main_lst) - needed_for_win else ['-']
                if '-' not in column_up and opponents_char not in column_up:
                    return True
                diagonal_right_up = [main_lst[lst_counter + i][element_counter + i] for i in range(needed_for_win)] if element_counter <= len(lst) - needed_for_win and lst_counter <= len(main_lst) - needed_for_win else ['-']
                if '-' not in diagonal_right_up and opponents_char not in diagonal_right_up:
                    return True
                diagonal_left_up = [main_lst[lst_counter + i][element_counter - i] for i in range(needed_for_win)] if element_counter >= needed_for_win - 1 and lst_counter <= len(main_lst) - needed_for_win else ['-']
                if '-' not in diagonal_left_up and opponents_char not in diagonal_left_up:
                    return True
    return False

def show_game_state(main_list):
    for i in range(21):
        print("-", end="")
    print("")
    for i in range(len(main_list)):
        for p in range(3):
            print("|", end="")
            for k in range(len(main_list[i])):
                the_row = make_art_bigger(main_list[len(main_list) - (1 + i)][k])[p]
                for symbol in the_row:
                    print(symbol, end="")
                print("|", end="")
            print("")
        for i in range(21):
            print("-", end="")
        print("")

def main():
    main_lst = [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']] #each sublist is a row, first sublist is bot row
    print("Lets play some Connect-3!")
    print("Player 1 starts")
    player_turn = 1
    while True:
        show_game_state(main_lst)
        user_input = input("Input a value (1-5) to drop your mark into corresponding column: ")
        while True:
            try:
                user_input = int(user_input)
            except ValueError:
                user_input = input("Uhhoh, thats not an integer. Try putting in an integer value between 1 and 5: ")
            else:
                if main_lst[-1][user_input - 1] != '-':
                    user_input = input("Oopsie, that column is full. Try another one: ")
                elif user_input > 5 or user_input < 1:
                    user_input = input("Oh no, we don't have that many columns... try again: " if user_input > 5 else "Let's start the counting from 1, shall we? " if user_input == 0 else "No negative values allowed! Try again: ")
                else:
                    break

        for i in range(len(main_lst)):
            if main_lst[i][user_input - 1] == '-':
                main_lst[i][user_input - 1] = player_chars[player_turn]
                break
            
        if check_if_win(player_chars[player_turn], main_lst):
            show_game_state(main_lst)
            print("Congratulations player {}, you won!".format(2 - player_turn))
            play_again = input("Would you like to play again (y/n)? ")
            while play_again.lower() != 'y' and play_again.lower() != 'n':
                play_again = input("Please input either the letter y for yes or letter n for no: ")
            if play_again == 'y':
                main()
            else:
                print("Ok then, goodbye!")
                sys.exit()
        
        for counter, i in enumerate(main_lst):
            if '-' not in i:
                if counter == len(main_lst) - 1:
                    print("Wow, looks like you two filled out the board and ended it with a tie! You sure are a good match for each other.")
                    play_again = input("Would you like to play again (y/n)? ")
                    while play_again.lower() != 'y' and play_again.lower() != 'n':
                        play_again = input("Please input either the letter y for yes or letter n for no: ")
                    if play_again == 'y':
                        main()
                    else:
                        print("Ok then, goodbye!")
                        sys.exit()

        player_turn = 1 - player_turn
        print("Player {}s turn".format(2 - player_turn))

main()