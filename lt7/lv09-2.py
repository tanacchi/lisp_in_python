from reader import read


env = {
    '+': lambda *args: args[0] + args[1],
    '-': lambda *args: args[0] - args[1]
}

def evaluate(src):
    if isinstance(src, str):
        return env[src]
    elif not isinstance(src, list):
        return src
    elif src[0] == 'define':
        key, value = src[1], evaluate(src[2])
        env[key] = value
    else:
        operator = evaluate(src[0])  # Modified
        args = src[1:]
        return operator(*args)


######## main ########

print("Welcome to lt7 !!\n")

while True:
    result = evaluate(read())

    print("-"*10)
    print("  {}  <{}>".format(result, type(result).__name__))
    print("-"*10)
    print()
