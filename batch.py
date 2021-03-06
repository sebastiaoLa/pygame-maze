class Batch(object):
    def __init__(self):
        self.rects = []

    def add_to_batch(self, rect):
        if isinstance(rect, list):
            self.rects += rect
        else:
            self.rects.append(rect)

    def draw(self):
        rects = []
        rects += self.rects
        self.rects = []
        return rects
