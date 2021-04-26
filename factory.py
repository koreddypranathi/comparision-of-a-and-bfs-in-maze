# A simple factory class that imports and returns a relevant solver when provided a string
# Not hugely necessary, but reduces the code in solve.py, making it easier to read.

class SolverFactory:
    def __init__(self):
        self.Default = "breadthfirst"
        self.Choices = ["breadthfirst","astar"]

    def createsolver(self, type):
        if type == "astar":
            import astar
            return ["A-star Search", astar.solve]
        else:
            import breadthfirst
            return ["Breadth first search", breadthfirst.solve]
