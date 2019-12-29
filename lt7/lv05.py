from reader import read


def evaluate(src):
    #  return src
    return src[1] + src[2]  # Step 2


######## main ########

print("Welcome to lt7 !!\n")

while True:
    result = evaluate(read())  # Modified

    print("-"*10)
    print("  {}  <{}>".format(result, type(result).__name__)) # Modified
    print("-"*10)
    print()
