# python 模块
import sys
from test.testpackage import a

for i in sys.argv:
    print(i)
print(sys.argv)
print('--------------------------')
for p in sys.path:
    print(p)

if __name__ == '__main__':
    print("程序自身在运行")
else:
    print('我来自另一模块')

def say_hello():
    print('hello')

print(dir(sys))
print(dir())

print(dir(a))

a.test3()