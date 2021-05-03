num_list = [1, 2, 3, 4, 5]
for i in range(len(num_list)):
    num_list[i] *= num_list[i]
print(num_list)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
for i in range(len(list1)):
    list1[i] += list2[i]
print(list1)

sum_of_elements = 0
list12 = [1, 2, 3, 4, 5]
for member in range(0, len(list12)):
    sum_of_elements += list12[member]
print(sum_of_elements)

def remove(duplicate):
    listik = []
    for number in duplicate:
        if number not in listik:
            listik.append(number)
    return listik
duplicate = [1, 2, 3, 3, 5, 6, 8, 8, 9]
print(remove(duplicate))

num = [1, 2, 3, 3, 5, 6, 8, 8, 9]
list22=[]
for i in num:
    if num.count(i) == 1:
        list22.append(i)
print(list22)