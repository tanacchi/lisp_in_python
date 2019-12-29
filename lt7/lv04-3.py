from reader import read  # Modified


######## main ########

print("Welcome to lt7 !!\n")

while True:
    src = read()  # Modified

    print("-"*10)
    print("  {} <{}>".format(src, type(src).__name__))
    print("-"*10)
    print()
