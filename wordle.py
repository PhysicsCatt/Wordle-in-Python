#Logic file where I store my main code
class Wordle:

    Max_Attempts=6
    Word_Length=5

    def __init__(self, secret: str):
        self.secret: str=secret
        self.attempts=[]
        pass
