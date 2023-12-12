
class Node:

    def __init__(self, x, y, id) -> None:
        self.x = x
        self.y = y
        self.id = id


    def get_pos(self):
        return (self.x, self.y)
        