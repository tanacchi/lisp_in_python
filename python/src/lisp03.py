import re

class Reader(object):
    def __init__(self):
        self.__data = []

    def read(self, src):
        index, end = 0, len(src)
        while index < end:
            match = re.search(re.compile(r'[\w\d]+'), src[index:])
            if match != None and match.span()[0] == 0:
                detected_word = match.group(0)
                self.__data.append(detected_word)
                index += len(detected_word)

            ch = src[index]
            if ch == " ":
                index += 1
            elif ch == "(":
                index += 1
            elif ch == ")":
                index += 1

        return self.__data


if __name__ == '__main__':
    source_str = "( Hello World)"
    reader = Reader()
    result = reader.read(source_str)
    print(result)
