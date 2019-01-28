class Evaluator(object):
    pass


def evaluate(arg_list):
    dispatch_table = {
        '+': lambda args: sum(args),
        '-': lambda args: args[0] - sum(args[1:])
    }
    return dispatch_table.get(arg_list[0])(arg_list[1:])
