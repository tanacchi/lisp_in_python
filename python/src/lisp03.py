class Reader(object):
    def __init__(self):
        self.__data = []

    def read(self, src):
        for ch in src:
            if ch == " ":
                continue
            elif ch == "(":
                pass
            elif ch == ")":
                pass
            else:
                self.__data.append(ch)
        return self.__data;


if __name__ == '__main__':
    pass
