import secrets

class Lottery:
    def __init__(self):
        self.pot = 0
        self.entryFee = 100000
        self.participants = []
        # Some may want to fill the pot with n% of their winnings
        self.participantsGiveToPot = {}
    
    # takes name, amount of tickets, percent to give back to the pot (from 0 to 1; 0.5 being 50%)
    def addParticipant(self, name, amount = 1, nToPot = 0, fee = -1):
        if nToPot != 0:
            nToPot = nToPot / 100
        for i in range(amount):
            self.participants.append(name)
            if fee == -1:
                self.pot = self.pot + self.entryFee
            elif fee > 0:
                self.pot = self.pot + fee
            # if added multiple times, last n counts
            self.participantsGiveToPot[name] = nToPot
    
    def getParticipants(self):
        return self.participants
    
    def getWinner(self):
        winner = secrets.choice(self.participants)
        won = int(self.pot - self.pot * self.participantsGiveToPot[winner])
        self.pot = self.pot - won
        self.clearParticipants()
        return winner, won
        
    def getPot(self):
        return self.pot
        
    def clearParticipants(self):
        self.participants = []
        self.participantsGiveToPot = {}
        
    def setEntryFee(self, fee):
        self.entryFee = fee
    
    def getEntryFee(self):
        return self.entryFee
    
    def countTickets(self):
        return len(self.participants)


if __name__ == "__main__":
    test = Lottery()
    test.addParticipant("alice", 11, 50)
    test.addParticipant("bob", 10)
    ls = test.getParticipants()
    for p in ls:
        print (p)
    winner, value = test.getWinner()
    print (winner + " won " + str(value) + "!\nthe pot is now: " + str(test.getPot()))
    