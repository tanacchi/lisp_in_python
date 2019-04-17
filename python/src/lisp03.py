import re

class Reader(object):
    def __make_list(self, src, index):
        result = []
        while src[index:]:
            match = re.search(re.compile(r'^[\w\d]+'), src[index:])
            if match != None:
                detected_word = match.group(0)
                result.append(detected_word)
                index += len(detected_word)
            elif src[index] == "(":
                sub_result = self.__make_list(src, index + 1)
                result.append(sub_result['list'])
                index = sub_result['index']
            elif src[index] == ")":
                break
            else:
                index += 1
        return {'list': result, 'index': index + 1}

    def read(self, src):
        result = self.__make_list(src, src.find("(") + 1)
        return result['list']

if __name__ == '__main__':
    source_str = "( A B (C D ) E)"
    reader = Reader()
    result = reader.read(source_str)
    print(result)
