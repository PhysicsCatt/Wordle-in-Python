from wordle import Wordle

def main():
    print("Test Wordle")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x=input("Type your guess: ")
        wordle.attempt(x)

    if wordle.is_solved:
        print("Congrats!! You found the correct answer")
    else:
        print("Game Over")


if __name__ == "__main__":
   main()
