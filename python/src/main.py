from reader import Reader

dispatch_table = {}
dispatch_table.update({ 
    'add': lambda args : args[0] + args[1],
})


def evaluate(source):
    if isinstance(source, str):
        return dispatch_table[source]
    elif not isinstance(source, list):
        return source
    elif source[0] == 'define':
        key, value = source[1], evaluate(source[2])
        dispatch_table[key] = value
    elif source[0] == 'quote':
        return source[1]
    else:
        operator = dispatch_table[source[0]]
        args = [evaluate(expr) for expr in source[1:]]
        return operator(args) if callable(operator) else evaluate(operator)


def main():
    while True:
        source_str  = input("> ")
        source_list = Reader.read(source_str)
        print(source_list)

        try:
            print("result: {}\n".format(result))
        except Exception as e:
            print("ERR: ")
            print(e)


if __name__ == '__main__':
    main()
