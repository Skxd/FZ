# 100exam 25  求1+2!+3!+...+的和
anwser = 0                                      # 储存累加结果
number = int(input('Input number : '))           # 用户输入求到多少的阶乘

def jiec(a) :                                   # 定义函数用来计算阶乘(100exam 26)
    ann = 1
    for n in range(1,a+1):
        ann = ann*n
    return ann

for num in range(1,number+1) :                  # 开始进行循环累加
    if number == 1 :                                # 用户输入 1 时，输出 1 并结束循环
        print(num)
        break
    else:                                       # 其它情况时，开始累加阶乘
        anwser = anwser + jiec(num)                 # 每循环一次，都把阶乘结果与上次结果相加

print('这是%s到%s的阶乘和 :'%((num-num+1),num),anwser)                                   # 输出所求结果
