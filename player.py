
# GolfPlayer class
class GolfPlayer(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_payer(self):
        print("\n------------------------------" + "\n\t🔔 GOLFER DETAILS \n")
        print("\tName of golfer : {} \n\tScore : {}".format(self.get_name(), self.get_score()))
        print("------------------------------")

    # getter function of name
    def get_name(self):
        """
        Getter of name
        :return: name of golfer
        """
        return str(self.name)

    # setter function of name
    def set_name(self, n):
        """
        Setter of name
        :param n: name of golfer
        """
        self.name = n
        print("Name of golfer changed!")

    # getter function of score
    def get_score(self):
        """
        Getter of score
        :return: score of golfer
        """
        return self.score

    # setter function of score
    def set_score(self, s):
        """
        Setter of name
        :param s: score of golfer
        """
        self.score = s
        print("Score of golfer changed!")


