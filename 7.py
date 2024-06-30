def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    arr = [5, 1, 8, 92, -1, 30]
    bubble_sort(arr)
    print("Danh sách sau khi sắp xếp từ bé đến lớn:")
    print(arr)

if __name__ == "__main__":
    main()
