class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart2')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

print(lisa.name)

te = ['22','docs','谢']
if input('input : ') not in te :
    print('不在')
else:
    print('在')

print(type(te[1]))