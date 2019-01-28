class Evaluator(object):
    pass

def add(args):
    return sum(args)

def minus(args):
    return args[0] - sum(args[1:])

def multi(args):
    ans = args[0]
    for elem in args[1:]:
        ans *= elem
    return ans

def div(args):
    ans = args[0]
    for elem in args[1:]:
        ans /= elem
    return ans

def evaluate(arg_list):
    dispatch_table = {
        '+': add,
        '-': minus,
        '*': multi,
        '/': div
    }
    return dispatch_table.get(arg_list[0])(arg_list[1:])
