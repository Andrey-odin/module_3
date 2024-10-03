def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(14, {11,3,4})
print_params(b=25)
print_params(c=[1,2,3])

values_list=[[9,3,1], 15, 'значение']
values_dict={'a':1, 'b':"строка", 'c':True}
print_params(values_list)
print_params(*values_list)
print_params(values_dict)
print_params(*values_dict)
print_params(**values_dict)
values_list_2=("Hello", 15)
print_params(*values_list_2, 42)