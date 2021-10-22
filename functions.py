def sayhi():
    print("hello user ")

def sayhiparm(name):
    print(f'hello user parm {name}')

def cude(num):
    return  num*num* num

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num2
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3,2,5))
sayhiparm("bharath")
sayhi()
result=cude(5)
print(result)


