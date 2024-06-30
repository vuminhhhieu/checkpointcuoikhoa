def print_fibo(n):
    fibo_list = [1, 1]
    if n == 1:
        print(1)
    elif n == 2:
        print("1, 1")
    else:
        print("1, 1", end=", ")
        for i in range(2, n):
            next_fibo = fibo_list[-1] + fibo_list[-2]
            fibo_list.append(next_fibo)
            print(next_fibo, end=", ")
def main():
    try:
        n = int(input("Nhập số phần tử của dãy Fibonacci: "))
        if n <= 0:
            print("Số phần tử phải lớn hơn 0.")
        else:
            print("Dãy Fibonacci gồm", n, "phần tử là:")
            print_fibo(n)
    except ValueError:
        print("Bạn đã nhập không phải số nguyên. Vui lòng nhập lại.")
main()
