import re

class Reader(object):
    @staticmethod
    def __make_list(src, index):
        result = []
        while src[index:]:
            match = re.search(re.compile(r'^[\w\d]+'), src[index:])
            if match != None:
                detected_token = match.group(0)
                result.append(detected_token)
                index += len(detected_token)
            elif src[index] == "(":
                sub_result = Reader.__make_list(src, index + 1)
                result.append(sub_result['list'])
                index = sub_result['index']
            elif src[index] == ")":
                break
            else:
                index += 1
        return {'list': result, 'index': index + 1}

    @staticmethod
    def read(src):
        result = Reader.__make_list(src, src.find("(") + 1)
        return result['list']

if __name__ == '__main__':
    source_str = "( A B (C D ) E (FG H) I)"
    result = Reader.read(source_str)
    print(result)  # ['A', 'B', ['C', 'D'], 'E', ['FG', 'H', 'I'], 'J']
