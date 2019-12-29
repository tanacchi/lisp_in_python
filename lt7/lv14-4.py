from reader import read


env = {
    '+': lambda *args: args[0] + args[1],
    '-': lambda *args: args[0] - args[1],
    '#true':  True,
    '#false': False
}

def lambda_content(vargs, args, exprs):
    for varg, arg in zip(vargs, args):
        env[varg] = arg
    return_value = None
    for expr in exprs:
        return_value = evaluate(expr)
    return return_value

def evaluate(src):
    if isinstance(src, str):
        return env[src]
    elif not isinstance(src, list):
        return src
    elif src[0] == 'define':
        key, value = src[1], evaluate(src[2])
        env[key] = value
    elif src[0] == 'lambda':
        vargs, exprs = src[1], src[2:]
        return lambda *args: lambda_content(vargs, args, exprs)
    elif src[0] == 'eq?':
        return evaluate(src[1]) == evaluate(src[2])
    elif src[0] == 'if':
        condition = evaluate(src[1])
        return evaluate(src[2]) if condition else evaluate(src[3])
    elif src[0] == 'quote':
        return src[1]
    elif src[0] == 'car':
        return evaluate(src[1])[0]
    elif src[0] == 'cdr':
        return evaluate(src[1])[1:]
    elif src[0] == 'cons':
        new = evaluate(src[1])  # Added
        lst = evaluate(src[2])
        lst.insert(0, new)
        return lst
    else:
        operator = evaluate(src[0])
        args = [evaluate(arg) for arg in src[1:]]
        return operator(*args)


######## main ########
import traceback


print("Welcome to lt7 !!\n")

while True:
    try:
        result = evaluate(read())
    except Exception as e:
        print(traceback.print_exc())
        continue

    print("-"*10)
    print("  {}  <{}>".format(result, type(result).__name__))
    print("-"*10)
    print()
