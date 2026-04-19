import math

# Custom Exception
class MauSoBangKhong(Exception):
    def __init__(self):
        super().__init__("Mẫu số không được bằng 0!")

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise MauSoBangKhong()
        # Chuẩn hóa dấu (nếu mẫu âm thì chuyển dấu lên tử)
        if mau < 0:
            tu, mau = -tu, -mau
        self.__tu = tu
        self.__mau = mau

    # Thuộc tính private
    @property
    def tu(self): return self.__tu
    @property
    def mau(self): return self.__mau

    # Kiểm tra tối giản
    def is_toi_gian(self):
        return math.gcd(self.__tu, self.__mau) == 1

    # Trả về một phân số mới đã tối giản
    def toi_gian(self):
        ucln = math.gcd(self.__tu, self.__mau)
        return PhanSo(self.__tu // ucln, self.__mau // ucln)

    # --- Operator Overloading ---
    def __add__(self, other):
        # a/b + c/d = (ad + bc) / (bd)
        tu_moi = self.tu * other.mau + other.tu * self.mau
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi).toi_gian()

    def __sub__(self, other):
        # a/b - c/d = (ad - bc) / (bd)
        tu_moi = self.tu * other.mau - other.tu * self.mau
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi).toi_gian()

    def __mul__(self, other):
        # a/b * c/d = ac / bd
        return PhanSo(self.tu * other.tu, self.mau * other.mau).toi_gian()

    def __truediv__(self, other):
        # a/b / c/d = ad / bc
        if other.tu == 0:
            raise MauSoBangKhong()
        return PhanSo(self.tu * other.mau, self.mau * other.tu).toi_gian()

    # --- Comparisons ---
    # So sánh dựa trên quy đồng (a*d vs b*c) để tránh sai số thập phân (float)
    def __eq__(self, other):
        return self.tu * other.mau == other.tu * self.mau

    def __lt__(self, other):
        return self.tu * other.mau < other.tu * self.mau

    def __gt__(self, other):
        return self.tu * other.mau > other.tu * self.mau

    def __str__(self):
        if self.__mau == 1:
            return f"{self.__tu}"
        elif self.__tu == 0:
            return "0"
        return f"{self.__tu}/{self.__mau}"

    def __repr__(self):
        return self.__str__()

# --- CHƯƠNG TRÌNH ỨNG DỤNG BÀI 3 ---
if __name__ == "__main__":
    print("\n--- TEST BÀI 3 (PHÂN SỐ) ---")
    
    # Tạo danh sách các phân số
    ds_ps = [
        PhanSo(2, 4),    # Sẽ là 1/2
        PhanSo(5, 3), 
        PhanSo(-10, 20), # Sẽ là -1/2
        PhanSo(3, 1),    # Sẽ in ra 3
        PhanSo(7, 2)
    ]
    
    print("Danh sách gốc (đã ép về dạng string):", ds_ps)
    
    print("\nDạng tối giản của các phân số:")
    ds_ps_toigian = [ps.toi_gian() for ps in ds_ps]
    for ps in ds_ps_toigian:
        print(f" - {ps} (Là tối giản? {ps.is_toi_gian()})")

    # Thử tính toán
    ps1 = PhanSo(1, 2)
    ps2 = PhanSo(1, 3)
    print(f"\nPhép tính: {ps1} + {ps2} = {ps1 + ps2}")
    print(f"Phép tính: {ps1} - {ps2} = {ps1 - ps2}")
    print(f"Phép tính: {ps1} * {ps2} = {ps1 * ps2}")
    print(f"Phép tính: {ps1} / {ps2} = {ps1 / ps2}")

    # Sắp xếp dãy phân số nhờ __lt__
    ds_sorted = sorted(ds_ps_toigian)
    print(f"\nDãy phân số sắp xếp tăng dần: {ds_sorted}")