def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input_string = input("Nhập chuỗi cần kiểm tra palindrome: ")
if is_palindrome(input_string):
    print(f"{input_string} là palindrome.")
else:
    print(f"{input_string} không phải là palindrome.")
