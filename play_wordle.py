from wordle import Wordle

def main():
    print("Test Wordle")
    wordle = Wordle("APPLE")

    while True:
        x=input("Type your guess: ")
        if x == wordle.secret:
            print("Congrats!! You guessed the word correctly")
            break
        print("Your guess is incorrect. The correct answer was", Wordle)


if __name__ == "__main__":
   main()
