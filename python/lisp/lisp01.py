class Evaluator(object):
    pass


def evaluate(arg_list):
    ans = 0
    if arg_list[0] == '+':
        add = lambda args: sum(args)
        return add(arg_list[1:])
    if arg_list[0] == '-':
        minus = lambda args: args[0] - sum(args[1:])
        return minus(arg_list[1:])
