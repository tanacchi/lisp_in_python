class Evaluator(object):
    pass

def calc(func, args):
    ans = args[0]
    for elem in args[1:]:
        ans = func(ans, elem)
    return ans

def evaluate(arg_list):
    dispatch_table = {
        '+': int.__add__,
        '-': int.__sub__,
        '*': int.__mul__,
        '/': int.__floordiv__
    }
    return calc(dispatch_table.get(arg_list[0]), arg_list[1:])
