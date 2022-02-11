from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
from typing import List
import random

def main():
    print("Test Wordle")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x=input("\nType your guess: ")

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
        print(f"Game Over")

def display_results(wordle: Wordle):
    print("\nYour answers so far...")
    print(f"You have {wordle.remaining_attempts} attempts left")

    lines=[]

    for word in wordle.attempts:
        result=wordle.guess(word)
        coloured_result_str=convert_results_to_colour(result)
        lines.append(coloured_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"]*wordle.Word_Length))

    draw_border_around(lines)

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
    return " ".join(result_with_colour)

def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)


if __name__ == "__main__":
   main()
