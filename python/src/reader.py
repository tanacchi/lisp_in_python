import re

class Reader(object):  # TODO: Get more accuracy
    @staticmethod
    def __tokenize(target):
        try: return int(target)
        except ValueError:
            return target

    @staticmethod
    def __make_list(src, index):
        result = []
        while src[index:]:
            match = re.search(re.compile(r'^[\w\d]+'), src[index:])
            if match != None:
                detected_token = match.group(0)
                index += len(detected_token)
                result.append(Reader.__tokenize(detected_token))
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
    def parse(src):
        result = Reader.__make_list(src, src.find("(") + 1)
        return result['list']

    @staticmethod
    def read():
        source_str = ""
        while True:
            source_str += input("> ") + " "
            if source_str.count("(") == source_str.count(")"):
                break
        return Reader.parse(source_str)
