def common_method(array):
    length = len(array)
    sum_max = 0 #  记录最大子序列的总和
    begin_index = 0 # 记录 最大子序列的 起点
    end_index = 0 # 记录 最大子序列的 终点
    for i in range(length): # 从 i 开始
        for j in range(i ,length):# 从 j 结束 的子序列
            sum_sub = 0        # 记录 i 到 j 子序列的总和
            for k in range(i , j + 1): # 为了计算 从 i 开始 到 j 结束的子序列总和
                sum_sub += array[k]
            if sum_max < sum_sub:  # 与 当前最大值进行对比
                sum_max = sum_sub
                begin_index = i
                end_index = j

    print(begin_index , " <-----> " , end_index)
    print(sum_max)

def common_method_change(array):
    length = len(array)
    max_sum = 0
    begin_index = 0
    end_index = 0
    for i in range(length):
        sum_sub = 0
        for j in range(i , length):
            sum_sub += array[j]
            if sum_sub > max_sum:
                max_sum = sum_sub
                begin_index = i
                end_index = j

    print(begin_index , " <-----> " , end_index)
    print(max_sum)

def divide_conquer_method(array , left , right):
    sum = 0

    if left == right:
        if array[left] > 0:
            sum = array[left]
        else:
            sum =  0
    else:
        center = (left + right) // 2
        left_sum = divide_conquer_method(array , left , center) # 左子问题
        right_sum = divide_conquer_method(array , center + 1 , right) # 右子问题

        # 第三个情况的开始
        s1 = 0
        lefts = 0
        i = center
        while i >= left: # 从中间往当前 left 方向找最大，而且是从 center 开始的最大
            lefts += array[i]
            if lefts > s1:
                s1 = lefts
            i -= 1

        s2 = 0
        rights = 0
        i = center + 1
        while i <= right: # 从中间往当前 right 方向找最大，而且是从 center 开始的最大
            rights += array[i]
            if rights > s2:
                s2 = rights
            i += 1
        sum = s1 + s2

        if sum < left_sum:
            sum = left_sum
        if sum < right_sum:
            sum = right_sum
    return sum

def dynastic_method(array):
    length = len(array)
    sum_sub = 0
    b = 0
    for j in range(length):
        if b > 0:
            b = b + array[j]
        else:
            b = array[j]
        if b > sum_sub:
            sum_sub = b
    return sum_sub

if __name__ == '__main__':
    array = [-1 , 11 , -4 , 13 , 1  , -3 , 4 , -5 , -2]
    print('solution in common method(暴力解法) -> ')
    common_method(array)
    print('solution in changed common method -> ')
    common_method_change(array)
    max_sub = divide_conquer_method(array , 0 , 8)
    print('solution in divide-conquer -> ' , max_sub)
    max_sub = dynastic_method(array)
    print('solution in dynastic -> ' ,max_sub)