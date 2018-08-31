import time                                             # 100example 9
tup = {1:'one',2:'two',3:'three',4:'four','99':'52'}
for key,value in dict.items(tup) :                      # items() 函数以列表返回可遍历的(键, 值) 元组数组,用法 ：dict.items()
    print(key,value)
    time.sleep(2)