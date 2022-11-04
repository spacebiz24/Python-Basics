list1 = [1,2,3,4,5,2,2,3,2,4,1,8,9]
list2 = [1,2,3,3,3,3,5,6,9,1,10,2,1]
sub_list = [2,3,2]
def check_sub_list(list, sub_list):
    flag = 0
    for i in range (len(list) - len(sub_list) + 1):
        if(list[i:i + len(sub_list)] == sub_list):
            flag = 1
    if flag == 1:
        print("The Sublist exists")
    else:
        print("The Sublist does not exist")
check_sub_list(list1, sub_list)
check_sub_list(list2, sub_list)