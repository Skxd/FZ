# 100exam 24 求分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前 n 项和
member = 2
denominator = 1                                           # member,denominator为初始值
answer = 0                                                # 求和的初始值
number = []                                               # 用来存储每次迭代出的分数
count = int(input('多少项 :',))                            # 输入所求项数
#print(type(count))
for co in range(count) :
    result = member/denominator                                 # 所需分数值
    number.append(result)                                       # 添加进列表
    member ,denominator= member + denominator ,member           # 根据序列项数规则给 member,denominator 赋值
for fin in number :                                        # 求和的循环
    answer = answer + fin                                  # 累加列表中的元素
print(answer)
print(number)
