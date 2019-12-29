from reader import read
from copy import deepcopy  # Added


class Env(dict):
    def __init__(self, keys=[], values=[], outer=None):
        self.update(zip(keys, values))
        self.outer = outer

    def find(self, key):
        if key in self:
            return self
        elif self.outer != None:
            return self.outer.find(key)
        else:
            raise KeyError(f'{key} is not found.')  # Added

        
global_env = Env()
global_env.update({
    '+': lambda *args: args[0] + args[1],
    '-': lambda *args: args[0] - args[1],
    '#true':  True,
    '#false': False
})

def lambda_content(vargs, args, exprs, env):  # Modified
    new_env = Env(vargs, args, outer=env)
    for expr in exprs:
        return_value = evaluate(deepcopy(expr), new_env)
    return return_value

def evaluate(src, env):  # Modified
    if isinstance(src, str):
        return env.find(src)[src]  # Modified
    elif not isinstance(src, list):
        return src
    elif src[0] == 'define':
        key, value = src[1], evaluate(src[2], env)
        env[key] = value  # Modified
    elif src[0] == 'lambda':
        vargs, exprs = src[1], src[2:]
        return lambda *args: lambda_content(vargs, args, exprs, env)  # Modified
    elif src[0] == 'eq?':
        return evaluate(src[1], env) == evaluate(src[2], env)
    elif src[0] == 'if':
        condition = evaluate(src[1], env)
        return evaluate(src[2], env) if condition else evaluate(src[3], env)
    elif src[0] == 'quote':
        return src[1]
    elif src[0] == 'car':
        return evaluate(src[1], env)[0]
    elif src[0] == 'cdr':
        return evaluate(src[1], env)[1:]
    elif src[0] == 'cons':
        new = evaluate(src[1], env)
        lst = evaluate(src[2], env)
        lst.insert(0, new)
        return lst
    else:
        operator = evaluate(src[0], env)
        args = [evaluate(arg, env) for arg in src[1:]]
        return operator(*args)


######## main ########
import traceback


print("Welcome to lt7 !!\n")

while True:
    try:
        result = evaluate(read(), global_env)  # Attention
    except Exception as e:
        print(traceback.print_exc())
        continue

    print("-"*10)
    print("  {}  <{}>".format(result, type(result).__name__))
    print("-"*10)
    print()
