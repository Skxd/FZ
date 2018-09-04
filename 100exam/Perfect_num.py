# 100exam 19 找出10000以内的所有完数。find Perfect number
#lis = []
def Perfect_number (f) :        # 函数用来测试一个数字是否是完数
    s = 0
    for k in range(1,f) :
        if f%k == 0 :
            #lis.append(k)
            #print('测试数字  :',f,'\tk  :',k,'\t',lis)
            s += k                  # 累计约数
    if s == f :                     # 如果约数累计后与测试数字相同，测试数字为完数
        #print('is fin :',f)
        return f

for i in range(2,10000) :
    if i == Perfect_number(i):
        print('Find a Perfect number  : ',i,'\n')
