todos = open('tos.txt','a')
print('First is test...\nSecond are twins...\nThird no loser...',file=todos)
                                # print 的额外参数 file 用来指定要写的文件流
todos.close()                   # 关闭文件
