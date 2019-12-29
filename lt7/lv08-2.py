from reader import read


env = {}

def evaluate(src):
    if isinstance(src, str):  # Added
        return env[src]
    elif not isinstance(src, list):
        return src
    elif src[0] == '+':
        return evaluate(src[1]) + evaluate(src[2])
    elif src[0] == '-':
        return evaluate(src[1]) - evaluate(src[2])
    elif src[0] == 'define':
        key, value = src[1], evaluate(src[2])
        env[key] = value
    else:
        return src


######## main ########

print("Welcome to lt7 !!\n")

while True:
    result = evaluate(read())

    print("-"*10)
    print("  {}  <{}>".format(result, type(result).__name__))
    print("-"*10)
    print()
