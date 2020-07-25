import sys 

# filter user input
user_input_nums = sys.argv[1:]
for i, v in enumerate(user_input_nums):
    user_input_nums[i] = int(v)
user_input_nums.sort()

# calc summation
summation = 0
for v in user_input_nums:
    summation += v
# or, 
# >>> summation = sum(user_input_nums)
# 既然都知道有 min() 與 max() 了，其實內建也有 sum() 啦~

# calc mean
mean = summation / len(user_input_nums)

print("your input (in ascending order):", user_input_nums)
print("sum------", summation)
print("mean------", mean)
print("med-------") #還沒做
print("min-------", min(user_input_nums))
print("max-------", max(user_input_nums))

'''
修訂重點：
1. 變數使用有含意的命名
2. 逐漸拋棄使用 index 迭代物件的思維，若你確實需要 index 的資訊使用 enumerate() 最有效率
3. 再熟悉一下 list slice 的用法，很方便
'''
