def tong(arr, target_sum):
    cap_so = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                cap_so.append([arr[i], arr[j]])
    
    return cap_so

nums = [2, 6, 3, 9, 11]
target = 9
ket_qua = tong(nums, target)
print(ket_qua)
