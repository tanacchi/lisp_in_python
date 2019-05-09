from reader import Reader

dispatch_table = {}
def define(args):
    key, value = args[0], args[1]
    dispatch_table[key] = lambda args : value

dispatch_table.update({ 
    'add': lambda args : int(args[0]) + int(args[1]),
    'define' : define
})

def eval(operand, args):
    return dispatch_table[operand](args)


def main():
    while True:
        source_str  = input("> ")
        source_list = Reader.read(source_str)
        print(source_list)

        operand = source_list[0]
        args = source_list[1:]
        result = eval(operand, args)
        print("result: {}\n".format(result))


if __name__ == '__main__':
    main()
