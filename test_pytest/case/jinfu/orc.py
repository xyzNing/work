import pytesseract
from PIL import Image
from datetime import datetime

# image=Image.open(r'C:\Users\ning\Desktop\1.gif')
# text=pytesseract.image_to_string(image)
# print(text)
print(datetime.now().strftime("%Y-%m-%d"))
a=['HT190904002','HT190904003','HT190711006']
b=[1,11,22,44,65,4,7,9,46,99]
n=10
# def test(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[i]
#             if b[j]>b[j+1]:
#                 b[j],b[j+1]=b[j+1],b[j]




def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))
print(bubbleSort(b))
print(bubbleSort(a))
print(bubbleSort(a)[::-1])
print(bubbleSort(a)[::-1][0:1])
aaa=[1]
print(aaa[0:1])

