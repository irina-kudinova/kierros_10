"""
# Ohjelmointi - mölkky game points by class
# Tekijä: Irina Kudinova
# Opiskelijanumero: 154058513
"""

# TODO:
# a) Implement the class Player here.
class Player:
    """Class Player: implements some players (2) that play mölkky and counts their points"""

    def __init__(self, name):

        self.__name = name
        self.__points = 0
        self.__avg_points = []

    def get_name(self):
        """gets name of player"""
        return self.__name

    def get_points(self):
        """gets points of player"""
        return self.__points

    def has_won(self):
        """checks if player has won"""
        if self.__points == 50:
            return True
        else:
            return False

    def add_points(self, points):
        """adds points to players list of points, even if reducted points"""

        if self.__points + points > 50:
            self.__points = 25
            print(f"{self.__name} gets penalty points!")
        else:
            self.__points += points

        self.__avg_points.append(points)

        if (self.__points >= 40) and (self.__points <= 49):
            print(f"{self.__name} needs only {50 - self.__points} points. It's better to avoid knocking down the pins with higher points.")

    def average_points(self, points):
        """averages points of players all points"""

        average = sum(self.__avg_points) / len(self.__avg_points)
        if average < points:
            return True
        else:
            return False

    def percentages(self):
        """hit percentages of players"""
        hits = 0
        for turn in self.__avg_points:
            if turn > 0:
                hits += 1
        if len(self.__avg_points) == 0:
            return 0
        else:
            return hits / len(self.__avg_points) *100


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)
        cheers = in_turn.average_points(pts)
        if cheers:
            print(f"Cheers {in_turn.get_name()}!")


        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.percentages():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.percentages():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
