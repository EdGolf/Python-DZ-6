#Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный.


test_str = "(45 + 55)-(45 + 55)+10"
print("The original string is : " + test_str)
res = eval(test_str)
print("The evaluated result is : " + str(res))