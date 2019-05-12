from reader import Reader

dispatch_table = {}
dispatch_table.update({ 
    'add': lambda args : int(args[0]) + int(args[1]),
})


def eval(source):
    if isinstance(source, str):
        return dispatch_table[source]
    elif not isinstance(source, list):
        return source
    elif source[0] == 'define':
        (key, value) = source[1:]
        dispatch_table[key] = value
    else:
        target = dispatch_table[source[0]]
        return target(source[1:]) if callable(target) else eval(target)


def main():
    while True:
        source_str  = input("> ")
        source_list = Reader.read(source_str)
        print(source_list)

        result = eval(source_list)
        print("result: {}\n".format(result))


if __name__ == '__main__':
    main()
