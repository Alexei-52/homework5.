immutable_var = (['a','b'],1,2)
print("Незменяемый объект 'Кортеж':",immutable_var)
#immutable_var[2] = 55
print('Попробовал изменить, выводит ошибку так как в уроке было уже сказано что "кортежи" неизменяемые списки')
print(type(immutable_var))
mutable_list = ['a','b',1,2]
print("Изменяемый объект 'Список':",mutable_list)
print(type(mutable_list))
mutable_list.append(4)
print(mutable_list)
