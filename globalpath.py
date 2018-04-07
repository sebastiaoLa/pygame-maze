
class GlobalPath(object):
    def __init__(self):
        self.path = []

    def add_to_global(self,pos):
        self.path.append(pos)

    def pos_in_global(self,pos):
        pass