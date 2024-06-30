phone_inventory = {
    "Iphone12": 28000000,
    "SamsungN10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000,
}
brand = input("Nhập tên hãng điện thoại: ")
if brand in phone_inventory:
    print("Giá tiền của", brand, "là:", phone_inventory[brand])
else:
    print("Không có thông tin về hãng máy tính này trong kho.")


def get_phones_within_budget():
    budget = int(input("Số tiền dự tính: "))
    print("Điện thoại phù hợp: ")
    found_any = False
    for phone, price in phone_inventory.items():
        if price <= budget:
            print(f"- {phone}: {price}")
            found_any = True
    if not found_any:
        print("Không có điện thoại nào phù hợp.")
print()  
get_phones_within_budget()