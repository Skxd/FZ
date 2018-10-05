import easygui as g
#yes = 'show create table bird_wing_shapes;'
#noo = 'show creata table bird_wing_shapes;
yes = g.enterbox('请输入第一个字符串','字符串对比')
noo = g.enterbox('请输入第二个字符串','字符串对比')
for count in range(len(yes)):
    if yes[count] == noo[count] :
        print(count+1,' :',yes[count],noo[count])
        #pass
    else:
        print('\n这里错了 : 第%s号字符,是%s和%s' % (count + 1, yes[count], noo[count]))
        g.textbox(msg='同异处', title='对比结果', text='第一句 : %s.\n\n第二句 : %s'
                                                '\n\n这里错了 : 第%s个字符不同,分别是%s和%s'
                                                % (yes,noo,count + 1, yes[count], noo[count]))
input('\nEnter键退出')

