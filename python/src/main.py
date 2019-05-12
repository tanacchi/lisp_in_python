from reader import Reader

dispatch_table = {}
dispatch_table.update({ 
    'add': lambda args : int(args[0]) + int(args[1]),
})

def eval(operand, args):
    if operand == 'define':
        (key, value) = args
        dispatch_table[key] = value
    else:
        target = dispatch_table[operand]
        return target(args) if callable(target) else target


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
