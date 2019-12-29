import re

def __lex(target):
    try: 
        return int(target)
    except ValueError:
        try:
            return float(target)
        except:
            return target

def __make_list(src, index):
    result = []
    while src[index:]:
        match = re.search(re.compile(r'^[^ ()\n]+'), src[index:])
        if match != None:
            detected_token = match.group(0)
            index += len(detected_token)
            result.append(__lex(detected_token))
        elif src[index] == "(":
            sub_result = __make_list(src, index + 1)
            result.append(sub_result['list'])
            index = sub_result['index']
        elif src[index] == ")":
            break
        else:
            index += 1
    return {'list': result, 'index': index + 1}

def parse(src):
    parse_result= []
    index = 0
    while src[index:]:
        buff = __make_list(src[index:], 0)
        parse_result.append(buff['list'])
        index = buff['index']
    return parse_result[0][0]  # TODO: refactor

def read():
    source_str = ""
    while True:
        source_str += input("> ") + " "
        depth = source_str.count("(") - source_str.count(")")
        if depth > 0:
            print(">>" * depth, end="")
        elif source_str.strip() is "":
            continue
        elif depth < 0:
            raise RuntimeError("Syntax Error")
        else:
            break
    return parse(source_str)
