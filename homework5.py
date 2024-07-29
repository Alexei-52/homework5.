immutable_var = (['a','b'],1,2)
print("Незменяемый объект 'Кортеж':",immutable_var)
print(type(immutable_var))
mutable_list = ['a','b',1,2]
print("Изменяемый объект 'Список':",mutable_list)
print(type(mutable_list))
mutable_list.append(4)
print(mutable_list)