def list_of_list(nums):
    result = []
    for num in nums:
        if isinstance(num, list):
            result.extend(list_of_list(num))
        else:
            result.append(num)
    return result



nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(list_of_list(nice_list))
