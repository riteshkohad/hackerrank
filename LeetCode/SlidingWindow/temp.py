
str = [1,3,2,5,6,7,8, 5 , 3, 3, 3, 2 ,3,2,4,6,8,8]
print(str)
hash_map = {}

for i in range(len(str)):
    if str[i] in hash_map:
        hash_map[str[i]] += 1
    else:
        hash_map[str[i]] = 1
max_val = 0
max_count = 0
for key, val in hash_map.items():
    if val > max_count:
        max_val = key
        max_count = val

print(hash_map)
print(f"{max_val}: {max_count}") 


# O(n log n)
# O(n)
# O(n)

# O(1)
# str = sorted(str)
# print(str)

# max_count = 0
# max_char = 0
# current_count = 0
# for i in range(len(str)):
#     if i == 0:
#         current_count = 1
#         # max_char = str[i]
#     else:
#         prev_char = str[i-1]
#         # print(f"{prev_char} | {str[i]}")``
#         if prev_char == str[i]:
#             current_count += 1
#             # print(current_count)
#         else:
#             current_count = 1
    
#     # print(current_count)
#     # max_count = max(current_count, max_count)
#     if current_count > max_count:
#         max_char = str[i-1]
#         max_count = current_count
    

# print(f"{max_char}: {max_count}")
#     # if tmp == str[i]:

