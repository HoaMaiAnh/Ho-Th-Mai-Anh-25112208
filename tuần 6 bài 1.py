from abc import ABC, abstractmethod

# 1. Custom Exception
class GiaKhongHopLe(Exception):
    def __init__(self, message="Giá hàng hóa phải lớn hơn hoặc bằng 0."):
        super().__init__(message)

# 2. Lớp cha trừu tượng (ABC)
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.gia = gia  # Sẽ gọi setter của @property

    # @property để encapsulate thuộc tính giá
    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(f"Lỗi: {value} không phải mức giá hợp lệ cho {self.ten_hang}!")
        self._gia = value

    # @abstractmethod bắt buộc lớp con phải triển khai
    @abstractmethod
    def xuat_thong_tin(self):
        pass

    # Magic method __str__
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.ma_hang} - {self.ten_hang} - {self.gia:,.0f}đ"

    # Magic method __eq__ (Toán tử ==)
    def __eq__(self, other):
        if isinstance(other, HangHoa):
            return self.gia == other.gia
        return False

    # Magic method __lt__ (Toán tử <)
    def __lt__(self, other):
        if isinstance(other, HangHoa):
            return self.gia < other.gia
        return NotImplemented

# 3. Các lớp con
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, thoi_gian_bh):
        super().__init__(ma_hang, ten_hang, gia)
        self.thoi_gian_bh = thoi_gian_bh

    # Override abstract method
    def xuat_thong_tin(self):
        return f"{self} | Bảo hành: {self.thoi_gian_bh} tháng"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, nguyen_lieu):
        super().__init__(ma_hang, ten_hang, gia)
        self.nguyen_lieu = nguyen_lieu

    def xuat_thong_tin(self):
        return f"{self} | Nguyên liệu: {self.nguyen_lieu}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, ngay_het_han):
        super().__init__(ma_hang, ten_hang, gia)
        self.ngay_het_han = ngay_het_han

    def xuat_thong_tin(self):
        return f"{self} | HSD: {self.ngay_het_han}"

# --- TEST BÀI 1 ---
if __name__ == "__main__":
    print("--- TEST BÀI 1 ---")
    danh_sach = [
        HangDienMay("DM01", "Tủ lạnh", 15000000, 24),
        HangSanhSu("SS01", "Bình gốm", 500000, "Gốm Bát Tràng"),
        HangThucPham("TP01", "Sữa tươi", 35000, "12/2026")
    ]

    # Kiểm tra __lt__ (Sắp xếp theo giá)
    print("Danh sách tăng dần theo giá:")
    for h in sorted(danh_sach):
        print(h.xuat_thong_tin())

    # Demo Custom Exception
    try:
        loi_hang = HangThucPham("TP02", "Bánh mì", -5000, "Hôm nay")
    except GiaKhongHopLe as e:
        print(f"\nBắt lỗi: {e}")

    # Demo with statement (Ghi vào file)
    with open("hanghoa.txt", "w", encoding="utf-8") as f:
        for item in danh_sach:
            f.write(item.xuat_thong_tin() + "\n")
    print("\nĐã xuất danh sách ra file 'hanghoa.txt' sử dụng 'with' statement.")