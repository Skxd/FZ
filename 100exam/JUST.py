# 100exam 30 判断回数
def test(strr) :
    strr = str(strr)
    i=1# 获取字符串
    print((strr[-i:-len(strr)//2]))
    if strr[i-1:(len(strr)//2)-1] == strr[-i:(len(strr)//2)-1] :
        print('h')
    else:
        print('这不是回数')



#for nu in range(1000,10000):
test(978879)