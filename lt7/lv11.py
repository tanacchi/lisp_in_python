from reader import read


env = {
    '+': lambda *args: args[0] + args[1],
    '-': lambda *args: args[0] - args[1],
    '#true':  True,   # Step 2
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
        return evaluate(src[1]) == evaluate(src[2])  # Added
    else:
        operator = evaluate(src[0])
        args = [evaluate(arg) for arg in src[1:]]
        return operator(*args)


######## main ########

print("Welcome to lt7 !!\n")

while True:
    result = evaluate(read())

    print("-"*10)
    print("  {}  <{}>".format(result, type(result).__name__))
    print("-"*10)
    print()
