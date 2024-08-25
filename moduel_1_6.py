my_dict = {'Masha' : 16052000, 'Edic' : 8102002 }
print(my_dict)
print(my_dict['Masha']) # По существующему ключу
print(my_dict.get('Sasha' , 'Данный ключ не найден')) #По не существующему ключу
my_dict.update({'Vanya' : 71223, 'Bob' : 1233441123})
m = my_dict.pop('Masha')
print(m)
print(my_dict)


my_set = {1,1,1,4,5,6, 'Ultimate' , 'Ultimate' , 'tiger'}
print(my_set)
print(my_set.add(3 and 7))
print(my_set)
print(my_set.remove(1))
print(my_set)
