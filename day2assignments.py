#
# Assignment 1
#
# Use the following list - [1,11,14,5,8,9]

list1 = [1, 11, 14, 5, 8, 9]
list2 = []


def low_nums():
    for num in range(len(list1)):
        if list1[num] not in list2 and list1[num] < 10:
            list2.append(list1[num])
    print(list2)


print(low_nums())


# Assignment 2 - First Option
#
list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 4, 5, 6, 7, 8, 10]


def comb_lists():
    list3 = list1 + list2
    list3.sort()
    print(list3)


print(comb_lists())


# Assignment 2 - Second Option
#
def sort_them():
    list1 = input('Please enter your numbers, separated by space:\n')
    list2 = input(
        'Please enter your second set of numbers, separated by space:\n')
    comb_list = sorted(list1.split() + list2.split())
    for num in range(len(comb_list)):
        comb_list[num] = int(comb_list[num])
    print('Your sorted and combined list is: ' + str(comb_list) + '!')


print(sort_them())
