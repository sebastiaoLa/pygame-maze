class Batch(object):
    def __init__(self):
        self.rects = []
    
    def add_to_batch(self,rect):
        self.rects.append(rect)

    def draw(self):
        rects = []
        rects += self.rects
        self.rects = []
        return rects
