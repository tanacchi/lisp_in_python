def lex(input_str):
    try:
        return int(input_str)
    except:
        return input_str


def parse(input_str):
    result = []
    new_token = ""
    for ch in input_str:
        if ch == ' ':  # Modified
            new_token = lex(new_token) # Step 2
            result.append(new_token)
            new_token = ""
        elif ch == '(':
            pass
        elif ch == ')':
            pass
        else:
            new_token += ch
    else:
        result.append(lex(new_token)) # Step 2
        return result


######## main ########

print("Welcome to lt7 !!\n")

while True:
    input_str = input("> ")
    src = parse(input_str)

    print("-"*10)
    print("  {} <{}>".format(src, type(src).__name__))
    print("-"*10)
    print()
