import re

class Reader(object):
    @staticmethod
    def __tokenize(target):
        try: return int(target)
        except ValueError:
            return target

    @staticmethod
    def __make_list(src, index):
        result = []
        while src[index:]:
            match = re.search(re.compile(r'^[^ ()\n]+'), src[index:])
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
        parse_result= []
        index = 0
        while src[index:]:
            buff = Reader.__make_list(src[index:], 0)
            parse_result.append(buff['list'])
            index = buff['index']
        print("parse_result: {}".format(parse_result[0]))
        return parse_result[0]  # TODO: refactor

    @staticmethod
    def read():
        source_str = ""
        while True:
            source_str += input("> ") + " "
            depth = source_str.count("(") - source_str.count(")")
            if depth > 0:
                print(">>" * depth, end="")
            else:
                break
        return Reader.parse(source_str)
