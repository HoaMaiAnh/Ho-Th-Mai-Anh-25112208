class HangHoa:
    def __init__(self, ma_hang, ten_hang, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.gia = gia

    def xuat_thong_tin(self):
        print(f"[{self.__class__.__name__}] Mã: {self.ma_hang} | Tên: {self.ten_hang} | Giá: {self.gia:,.0f} VNĐ")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, thoi_gian_bh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, gia)
        self.thoi_gian_bh = thoi_gian_bh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"    -> Bảo hành: {self.thoi_gian_bh} tháng | Điện áp: {self.dien_ap}V | Công suất: {self.cong_suat}W")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"    -> Nguyên liệu: {self.loai_nguyen_lieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, ngay_san_xuat, ngay_het_han):
        super().__init__(ma_hang, ten_hang, gia)
        self.ngay_san_xuat = ngay_san_xuat
        self.ngay_het_han = ngay_het_han

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"    -> NSX: {self.ngay_san_xuat} | HSD: {self.ngay_het_han}")

# TEST BT1
print("--- BÀI TẬP 1 ---")
h1 = HangDienMay("DM01", "Tủ lạnh", 15000000, 24, 220, 150)
h2 = HangSanhSu("SS01", "Bình hoa", 500000, "Gốm Bát Tràng")
h3 = HangThucPham("TP01", "Sữa tươi", 35000, "01/05/2026", "01/11/2026")

h1.xuat_thong_tin()
h2.xuat_thong_tin()
h3.xuat_thong_tin()