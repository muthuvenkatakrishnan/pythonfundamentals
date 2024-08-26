list1 = [1,2,3,4,2,5,6,7]
list2 = [11,11,12,13,14]
list3 = [16,17,18]

combined_set = set(list1+list2+list3)
print(combined_set)

unique_list = list(combined_set)
print(f"my unique list is :{unique_list}")
