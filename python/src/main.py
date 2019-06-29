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
    elif source[0] == 'cons':
        new = evaluate(source[1])
        lst = [evaluate(expr) for expr in source[2:]][0]
        #  lst = evaluate(source[2:])
        lst.insert(0, new)
        return lst
    elif source[0] == 'car':
        return evaluate(evaluate(source[1])[0])
    elif source[0] == 'cdr':
        return evaluate(source[1])[1:]
    elif source[0] == 'is_null':
        return evaluate(source[1]) == []
    elif source[0] == 'cond':
        for statement in source[1:]:
            print("statement: {}".format(statement))
            cond, expr = statement[0], statement[1]
            if cond == "else" or evaluate(cond):
                return evaluate(expr)
        raise SyntaxError( "Invalid syntax of 'cond'")
    elif source[0] == 'lambda':
        def gen_body_of_lamda(exps, vargs, args):
            print("varg: {}, arg: {}".format(vargs, args))
            for varg, arg in zip(vargs, args):
                dispatch_table[varg] = arg
            for exp in exps:
                result = evaluate(exp)
            print(result)
            return result

        vargs, expr = source[1], source[2:]
        return lambda args: gen_body_of_lamda(expr, vargs, args)
    elif source[0] == 'is_zero':
        return evaluate(source[1]) == 0
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
            result = evaluate(source_list)
            print("result: {}\n".format(result))
        except Exception as e:
            print("ERR: ")
            print(e)


if __name__ == '__main__':
    main()
