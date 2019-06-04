class AVLNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)