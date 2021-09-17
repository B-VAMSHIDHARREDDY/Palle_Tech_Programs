class Player:
    def __init__(self,name):
        self.name=name
        self.score=0
    def hit_runs(self,runs):
        self.score = self.score + runs
p1 = Player("Sachin")
p2 = Player("Dhoni")
p1.hit_runs(4)
p1.hit_runs(3)
p2.hit_runs(2)
print(p1.__dict__)
print(p2.__dict__)

