from reader import Reader
from env import Env
from evaluator import evaluate

def main():
    global_env = Env()
    global_env.update({ 
        'add1': lambda args : args[0] + 1,
        'sub1': lambda args : args[0] - 1
    })

    while True:
        print(global_env)
        source_list = Reader.read()
        for target in source_list:
            print("---------")
            print(target)

            try:
                result = evaluate(target, global_env)
                print("result: {}\n".format(result))
            except Exception as e:
                print("ERR: ")
                print(e)


if __name__ == '__main__':
    main()
