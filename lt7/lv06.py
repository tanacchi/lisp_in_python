from reader import read


def evaluate(src):
    if not isinstance(src, list):  # Step 3
        return src
    elif src[0] == '+':
        return src[1] + src[2]
    elif src[0] == '-':
        return src[1] - src[2]  # Step 2
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
