class CanBo:
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        print(f"Tên: {self.ho_ten}, Sinh: {self.nam_sinh}, Giới tính: {self.gioi_tinh}, Địa chỉ: {self.dia_chi}", end="")

class CongNhan(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        # Bậc từ 1 đến 10
        self.bac = bac if 1 <= bac <= 10 else 1

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f", Chức vụ: Công nhân, Bậc: {self.bac}/10")

class KySu(CanBo):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f", Chức vụ: Kỹ sư, Ngành: {self.nganh_dao_tao}")

class NhanVien(CanBo): # Chú ý: Lớp NhanVien này khác BT2
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f", Chức vụ: Nhân viên, Công việc: {self.cong_viec}")

class QLCB:
    def __init__(self):
        self.danh_sach_can_bo = []

    def them_can_bo(self, can_bo):
        self.danh_sach_can_bo.append(can_bo)
        print(f"Đã thêm cán bộ: {can_bo.ho_ten}")

    def tim_kiem(self, ho_ten):
        ket_qua = [cb for cb in self.danh_sach_can_bo if ho_ten.lower() in cb.ho_ten.lower()]
        if not ket_qua:
            print("Không tìm thấy cán bộ!")
        else:
            print(f"--- Kết quả tìm kiếm cho '{ho_ten}' ---")
            for cb in ket_qua:
                cb.hien_thi_thong_tin()

    def hien_thi_danh_sach(self):
        print("--- Danh sách Cán bộ ---")
        for cb in self.danh_sach_can_bo:
            cb.hien_thi_thong_tin()

# TEST BT3
print("\n--- BÀI TẬP 3 ---")
quan_ly = QLCB()
quan_ly.them_can_bo(CongNhan("Nguyễn Công A", 1990, "Nam", "Hà Nội", 5))
quan_ly.them_can_bo(KySu("Trần Kỹ B", 1992, "Nữ", "Hải Phòng", "CNTT"))
quan_ly.them_can_bo(NhanVien("Lê Nhân C", 1995, "Nam", "Đà Nẵng", "Lễ tân"))

print("\n")
quan_ly.hien_thi_danh_sach()
print("\n")
quan_ly.tim_kiem("Trần Kỹ B")