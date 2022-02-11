from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
from typing import List

def main():
    print("Test Wordle")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x=input("Type your guess: ")

        if len(x) != wordle.Word_Length:
            print(Fore.RED
                  +f"Word must be {wordle.Word_Length} characters long!!"
                  +Fore.RESET
            )
            continue
        wordle.attempt(x)
        display_results(wordle)


    if wordle.is_solved:
        print("Congrats!! You found the correct answer")
    else:
        print("Game Over")

def display_results(wordle: Wordle):
    for word in wordle.attempts:
        result=wordle.guess(word)
        coloured_result_str=convert_results_to_colour(result)
        print(coloured_result_str)
    pass

def convert_results_to_colour(result: List[LetterState]):
    result_with_colour = []
    for letter in result:
        if letter.is_in_position:
            colour=Fore.GREEN
        elif letter.is_in_word:
            colour=Fore.YELLOW
        else:
            colour=Fore.WHITE
        coloured_letter=colour+letter.character+Fore.RESET
        result_with_colour.append(coloured_letter)
    return "".join(result_with_colour)




if __name__ == "__main__":
   main()
