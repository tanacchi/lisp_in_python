def evaluate(source, env):
    if isinstance(source, str):
        return env.find(source)[source]
    elif not isinstance(source, list):
        return source
    elif source[0] == 'define':
        key, value = source[1], evaluate(source[2], env)
        env[key] = value
    elif source[0] == 'quote':
        return source[1]
    elif source[0] == 'cons':
        new = evaluate(source[1], env)
        lst = [evaluate(expr, env) for expr in source[2:]][0]
        #  lst = evaluate(source[2:], env)
        lst.insert(0, new)
        return lst
    elif source[0] == 'car':
        return evaluate(evaluate(source[1], env)[0], env)
    elif source[0] == 'cdr':
        return evaluate(source[1], env)[1:]
    elif source[0] == 'cond':
        for statement in source[1:]:
            #  print("statement: {}".format(statement))
            cond, expr = statement[0], statement[1]
            if cond == "else" or evaluate(cond, env):
                return evaluate(expr, env)
        raise SyntaxError( "Invalid syntax of 'cond'")
    elif source[0] == 'lambda':
        def gen_body_of_lamda(exps, vargs, args):
            print("varg: {}, arg: {}".format(vargs, args))
            inner_env = Env(vargs, args, env)
            for exp in exps:
                result = evaluate(exp, inner_env)
            print(result)
            return result

        vargs, expr = source[1], source[2:]
        return lambda args: gen_body_of_lamda(expr, vargs, args)
    elif source[0] == 'load':
        match = re.search(re.compile(r'(?<=\").*(?=\")'), source[1])
        file_path = match.group(0)
        print("file_path: {}".format(file_path))
        with open(file_path) as f:
            module_content = f.read()
            return evaluate(Reader.parse(module_content), env)
    elif source[0] == 'eq?':
        return evaluate(source[1], env) == evaluate(source[2], env)
    else:
        operator = env.find(source[0])[source[0]]
        args = [evaluate(expr, env) for expr in source[1:]]
        return operator(args) if callable(operator) else evaluate(operator, env)
