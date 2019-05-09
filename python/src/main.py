from reader import Reader

def main():
    source_str  = input("> ")
    source_list = Reader.read(source_str)
    print(source_list)


if __name__ == '__main__':
    main()
