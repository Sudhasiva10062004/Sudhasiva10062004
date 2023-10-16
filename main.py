class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects for a Batsman and a Bowler
batsman1 = Batsman()
bowler1 = Bowler()

# Call the play() method for each object
batsman1.play()  # The batsman is batting.
bowler1.play()   # The bowler is bowling.