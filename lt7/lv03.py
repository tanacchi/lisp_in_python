def lex(input_str):
    try:
        return int(input_str)
    except:
        return input_str


######## main ########

print("Welcome to lt7 !!\n")

while True:
    input_str = input("> ")
    token = lex(input_str)

    print("-"*10)
    print("  {} <{}>".format(token, type(token).__name__))
    print("-"*10)
    print()
