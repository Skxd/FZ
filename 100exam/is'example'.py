# www.runoob.com/python/att-string-isalnum.html
# 判断字符串是否是某类型，是返回 TRUE ，否返回 FLASE。
import string
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
i=0
while i < len(s):
    c = s[i]                                       # islower isupper 甄别出大小写字母
    i += 1
    if c.islower() or c.isupper():                 # isalpha() 方法检测字符串是否只由字母组成
        letters += 1
        print(letters,c)
    elif c.isspace():               # isspace() 方法检测字符串是否只由空格组成
        space += 1
    elif c.isdigit():               #  isdigit() 方法检测字符串是否只由数字组成
        digit += 1
    else:
        others += 1                 # 目前无法计算中文字符
print (' char = %d\n space = %d\n digit = %d\n others = %d\n' % (letters,space,digit,others))