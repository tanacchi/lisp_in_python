class Env(dict):
    def __init__(self, keys=[], values=[], outer=None):
        self.update(zip(keys, values))
        self.outer = outer
    
    def find(self, key):
        return self if key in self else self.outer.find(key)
