
def two_sum(nums, target):
    chi_so_so = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in chi_so_so:
            return [chi_so_so[complement], i]
        chi_so_so[num] = i

nums1 = [2, 7, 11, 15]
target1 = 9
ket_qua1 = two_sum(nums1, target1)
print(f"Ví dụ 1: {ket_qua1}")
