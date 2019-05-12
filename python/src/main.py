from reader import Reader

dispatch_table = {}
dispatch_table.update({ 
    'add': lambda args : args[0] + args[1],
})


def eval(source):
    if isinstance(source, str):
        return dispatch_table[source]
    elif not isinstance(source, list):
        return source
    elif source[0] == 'define':
        (key, value) = source[1:]
        dispatch_table[key] = value
    elif source[0] == 'quote':
        return source[1]
    else:
        operator = dispatch_table[source[0]]
        args = [eval(expr) for expr in source[1:]]
        return operator(args) if callable(operator) else eval(operator)


def main():
    while True:
        source_str  = input("> ")
        source_list = Reader.read(source_str)
        print(source_list)

        result = eval(source_list)
        print("result: {}\n".format(result))


if __name__ == '__main__':
    main()
