def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

def main():
    try:
        n = int(input("Nhập một số nguyên > 0: "))
        if n <= 0:
            print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
            return
        num_digits = count_digits(n)
        print(f"Số chữ số trong số {n} là: {num_digits}")
    except ValueError:
        print("Đây không phải là một số nguyên. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()
