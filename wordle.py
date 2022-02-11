#Logic file where I store my main code
class Wordle:

    Max_Attempts=6
    Word_Length=5

    def __init__(self, secret: str):
        self.secret: str=secret
        self.attempts=[]
        pass

    def attempt(self, word:str):
        self.attempts.append(word)


    @property
    def is_solved(self):
        return len(self.attempts)>0 and self.attempts[-1]==self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.Max_Attempts - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
