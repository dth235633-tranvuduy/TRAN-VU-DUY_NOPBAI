import math

so = float(input("Nhập vào một số: "))
if so < 0:
    print("Không thể tính căn bậc 2 của số âm.")
else:
    can_bac_2 = math.sqrt(so)
    print(f"Căn bậc 2 của {so} là {can_bac_2}")