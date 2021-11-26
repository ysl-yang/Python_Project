# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}×{i}={j * i}', end=' ')
#     print()

# arr = [6, 5, 2, 1, 3, 4]
# for i in range(1, len(arr)):
#     for j in range(0, len(arr) - i):
#         if arr[j] > arr[j + 1]:
#             # arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             temp = arr[j]
#             arr[j] = arr[j + 1]
#             arr[j + 1] = temp
# print(arr)
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
