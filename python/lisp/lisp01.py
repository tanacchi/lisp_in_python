def evaluate(arg_list):
    ans = 0
    if arg_list[0] == '+':
        for elem in arg_list[1:]:
            ans += elem
        return ans
    if arg_list[0] == '-':
        ans += arg_list[1]
        for elem in arg_list[2:]:
            ans -= elem
        return ans
