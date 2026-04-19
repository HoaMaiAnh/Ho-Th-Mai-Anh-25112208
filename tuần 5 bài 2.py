class NhanVienBase:
    """Lớp cha chung cho các loại nhân viên"""
    def __init__(self, ma_nv, ten_nv):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv

    def hien_thi(self):
        print(f"Mã NV: {self.ma_nv} | Tên: {self.ten_nv}", end=" | ")

class CongTacVien(NhanVienBase):
    def __init__(self, ma_nv, ten_nv, thoi_han_hd, phu_cap_ld):
        super().__init__(ma_nv, ten_nv)
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap_ld = phu_cap_ld

    def hien_thi(self):
        super().hien_thi()
        print(f"Loại: CTV | Thời hạn HĐ: {self.thoi_han_hd} | Phụ cấp LĐ: {self.phu_cap_ld}")

class NhanVienChinhThuc(NhanVienBase):
    def __init__(self, ma_nv, ten_nv, vi_tri_cv):
        super().__init__(ma_nv, ten_nv)
        self.vi_tri_cv = vi_tri_cv

    def hien_thi(self):
        super().hien_thi()
        print(f"Loại: NV Chính thức | Vị trí: {self.vi_tri_cv}")

class TruongPhong(NhanVienBase):
    def __init__(self, ma_nv, ten_nv, ngay_bd_quan_ly, phu_cap_ql):
        super().__init__(ma_nv, ten_nv)
        self.ngay_bd_quan_ly = ngay_bd_quan_ly
        self.phu_cap_ql = phu_cap_ql

    def hien_thi(self):
        super().hien_thi()
        print(f"Loại: Trưởng phòng | Ngày bắt đầu QL: {self.ngay_bd_quan_ly} | Phụ cấp QL: {self.phu_cap_ql}")

# TEST BT2
print("\n--- BÀI TẬP 2 ---")
nv1 = CongTacVien("CTV01", "Lê Văn B", "6 tháng", 500000)
nv2 = NhanVienChinhThuc("NV02", "Trần Thị C", "Chuyên viên Marketing")
nv3 = TruongPhong("TP01", "Phạm Văn D", "01/01/2025", 3000000)

nv1.hien_thi()
nv2.hien_thi()
nv3.hien_thi()