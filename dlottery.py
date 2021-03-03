import secrets

class Lottery:
    def __init__(self):
        self.pool = 0
        self.entryFee = 100000
        self.participants = []
        # Some may want to fill the pool with n% of their winnings
        self.participantsGiveToPool = {}
    
    # takes name, amount of tickets, percent to give back to pool (from 0 to 1; 0.5 being 50%)
    def addParticipant(self, name, amount = 1, nToPool = 0, fee = -1):
        for i in range(amount):
            self.participants.append(name)
            if fee == -1:
                self.pool = self.pool + self.entryFee
            # if added multiple times, last n counts
            self.participantsGiveToPool[name] = nToPool
    
    def getParticipants(self):
        return self.participants
    
    def getWinner(self):
        winner = secrets.choice(self.participants)
        won = int(self.pool - self.pool * self.participantsGiveToPool[winner])
        self.pool = self.pool - won
        self.clearParticipants()
        return winner, won
        
    def getPool(self):
        return self.pool
        
    def clearParticipants(self):
        self.participants = []
        self.participantsGiveToPool = {}
        
    def setEntryFee(self, fee):
        self.entryFee = fee
    
    def getEntryFee(self):
        return self.entryFee
    
    def countTickets(self):
        return len(self.participants)


if __name__ == "__main__":
    test = Lottery()
    test.addParticipant("alice", 1, 0.5)
    test.addParticipant("bob", 10)
    ls = test.getParticipants()
    for p in ls:
        print (p)
    winner, value = test.getWinner()
    print (winner + " won " + str(value) + "!\nthe pool is now: " + str(test.getPool()))
    