myList = [10, 20, 30, 'apple', True, 8.10]
myList.append(30)
myList.append(40)
reversedList = myList[::-1]
print("Reversed List:", reversedList)

my_dict = {1: 'data', 2: 'information', 3: 'text'}
my_dict.pop(3)
my_dict[4] = 'features'
print("Value with key 1:", my_dict[1])


my_tuple = (1, 2, 3, 'apple', 'mango')


numeric_tuple = (10, 20, 30, 40, 50)
print("Minimum in numeric_tuple:", min(numeric_tuple))
r1 = my_tuple + numeric_tuple
print("Concatenated Tuple (r1):", r1)
newdupli = my_tuple * 2
print("Duplicated my_tuple:", newdupli)

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 7, 6, 1}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
