from reader import Reader

dispatch_table = { 'add': lambda a, b : int(a) + int(b) }

def eval(operand, a, b):
    return dispatch_table[operand](a, b)


def main():
    while True:
        source_str  = input("> ")
        source_list = Reader.read(source_str)
        print(source_list)

        operand = source_list[0]
        a = source_list[1]
        b = source_list[2]
        result = eval(operand, a, b)
        print("result: {}\n".format(result))


if __name__ == '__main__':
    main()
