class Goals:
    def __init__(self,name,prev_goals):
        self.name= name
        self.prev_goals = prev_goals
        self.current_goals = 0
        self.total_goals = self.prev_goals + self.current_goals
    def make_goal(self):
        self.current_goals = self.current_goals + 1
        self.total_goals = self.total_goals + 1
p1 = Goals("messi",102)
p2 = Goals("ronaldo",87)
p1.make_goal()
p1.make_goal()
p1.make_goal()
p2.make_goal()
print(p1.__dict__)
print(p2.__dict__)
