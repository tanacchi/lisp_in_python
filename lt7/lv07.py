from reader import read


env = {}  # Added

def evaluate(src):
    if not isinstance(src, list):
        return src
    elif src[0] == '+':
        return src[1] + src[2]
    elif src[0] == '-':
        return src[1] - src[2]
    elif src[0] == 'define':
        key   = src[1]
        #  value = src[2]  # Step 1
        #  value = evaluate(src[2])  # Step 2
        key, value = src[1], evaluate(src[2])  # Step 3
        env[key] = value
    else:
        return src


######## main ########

print("Welcome to lt7 !!\n")

while True:
    result = evaluate(read())

    print("-"*10)
    print("  {}  <{}>".format(result, type(result).__name__))
    print("[Debug] env: ", env)  # Added
    print("-"*10)
    print()
