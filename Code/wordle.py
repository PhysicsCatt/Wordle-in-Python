#Logic file where I store my main code
from letter_state import LetterState
class Wordle:

    Max_Attempts=6
    Word_Length=5

    def __init__(self, secret: str):
        self.secret: str=secret.upper()
        self.attempts=[]
#        pass

    def attempt(self, word:str):
        word=word.upper()
        self.attempts.append(word)

    def guess(self, word:str):
        word=word.upper()
        result = []

        for i in range(self.Word_Length):
            character=word[i]
            letter=LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position=character==self.secret[i]
            result.append(letter)
        return result


    @property
    def is_solved(self):
        return len(self.attempts)>0 and self.attempts[-1]==self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.Max_Attempts - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
