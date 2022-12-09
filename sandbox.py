def converter(*args):
    length = len(args)
    string = ''
    for i in range(length):
        string += args[i]
        if length-i == 1:
            break
        string += ','
    return string
'''
def abc(*args):
    print(len(args))
    return args

print(abc(1,3,4))
'''