
class Ivent:

    def __init__(self):
        self.ivent = {}

    def check_ivent(self, id):
        for key in self.ivent:
            if self.ivent[key] == True and self.ivent[key] == id:
                return True
            else:
                return  False

    def add_ivent(self, id):
        self.ivent[id] = True

    def del_ivent(self, id):
        self.ivent[id] = False

    def ivent_us(self, id):
        pass


