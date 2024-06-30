def main():
    ordered_items = []  

    while True:
        item = input("Nhập tên món bạn muốn đặt (nhập 'xong' để kết thúc): ").strip().lower()

        if item == 'xong':
            break

        if item in ordered_items:
            print(f"Món '{item}' đã được đặt rồi.")
        else:
            ordered_items.append(item)
            print(f"Đã thêm món '{item}' vào danh sách đặt món.")

    print("\nDanh sách các món đã đặt:")
    for item in ordered_items:
        print(item)

if __name__ == "__main__":
    main()
