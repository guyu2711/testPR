#somecode
import numpy
import pandas

class MyStruct:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

# 使用这个结构体
my_struct_instance = MyStruct(1, 'data', True)

# 访问和修改属性
print(my_struct_instance.field1)  # 输出 1
my_struct_instance.field2 = 'new data'
print(my_struct_instance.field2)  # 输出 'new data'
