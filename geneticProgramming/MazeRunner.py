
class MazeRunner(object):
    def __init__(self):
        # an array of left or right turns to go through the maze.
        # i.e., ['left', 'right', 'left', 'left', 'right']
        self.runner = None
        self.turns = []
        # each dead end will have a number 1-99 assigned. When the runner
        # hits a dead end, it will receive that position. The end of the maze is
        # position 100
        # The closer the dead end to maze exit, the high the number
        self.position = 0
        self.correct_position = 100


    # High fitness is 100 (the correct solution), low fitness is 0 meaning it solution
    # failed.
    def get_fitness(self):
        return self.position - self.correct_position
