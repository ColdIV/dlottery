import secrets

class Lottery:
    def __init__(self):
        self.pool = 0
        self.entryFee = 100000
        self.participants = []
    
    def addParticipant(self, name, amount = 1):
        for i in range(amount):
            self.participants.append(name)
            self.pool = self.pool + self.entryFee
    
    def getParticipants(self):
        return self.participants
    
    def getWinner(self):
        return secrets.choice(self.participants)
    
    def getPool(self):
        return str(self.pool)


if __name__ == "__main__":
    test = Lottery()
    test.addParticipant("alice")
    test.addParticipant("bob", 10)
    ls = test.getParticipants()
    for p in ls:
        print (p)
    print(test.getWinner() + " won " + test.getPool())
  