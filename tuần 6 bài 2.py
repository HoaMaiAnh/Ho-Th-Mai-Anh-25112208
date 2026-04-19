from abc import ABC, abstractmethod

# Custom Exceptions
class TuoiKhongHopLe(Exception): pass
class BacKhongHopLe(Exception): pass

class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi  # Gọi setter
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(f"Tuổi {value} không hợp lệ (Phải từ 18-65) cho {self.ho_ten}!")
        self._tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.ho_ten} ({self.tuoi} tuổi, {self.gioi_tinh}, {self.dia_chi})"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.ho_ten}>"

    # __eq__: bằng nhau nếu cùng tên và tuổi
    def __eq__(self, other):
        if isinstance(other, CanBo):
            return self.ho_ten == other.ho_ten and self.tuoi == other.tuoi
        return False

    # __lt__: sắp xếp theo tên ABC
    def __lt__(self, other):
        if isinstance(other, CanBo):
            return self.ho_ten < other.ho_ten
        return NotImplemented

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac  # Gọi setter

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(f"Bậc {value} không hợp lệ. Phải từ 1 đến 10.")
        self._bac = value

    def mo_ta(self):
        return f"Công nhân: {self} - Bậc {self.bac}/10"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dt):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dt = nganh_dt

    def mo_ta(self):
        return f"Kỹ sư: {self} - Ngành {self.nganh_dt}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhân viên: {self} - Công việc: {self.cong_viec}"

# --- TEST BÀI 2 ---
if __name__ == "__main__":
    print("\n--- TEST BÀI 2 ---")
    try:
        ds_can_bo = [
            CongNhan("Tran Van B", 30, "Nam", "HN", 5),
            KySu("Nguyen Anh A", 28, "Nữ", "HCM", "CNTT"),
            NhanVien("Le Thi C", 25, "Nữ", "DN", "Kế toán"),
            # Uncomment dòng dưới để test lỗi Tuổi
            # NhanVien("Loi Tuoi", 17, "Nam", "HN", "Thực tập")
            # Uncomment dòng dưới để test lỗi Bậc
            # CongNhan("Loi Bac", 30, "Nam", "HN", 15)
        ]

        # Sắp xếp danh sách (dựa vào __lt__ theo tên ABC)
        print("Danh sách cán bộ (đã sort theo tên):")
        for cb in sorted(ds_can_bo):
            print(cb.mo_ta())

        # Ghi và đọc với context manager (with)
        with open("canbo.txt", "w", encoding="utf-8") as fw:
            for cb in ds_can_bo:
                fw.write(f"{cb.mo_ta()}\n")

        print("\nĐọc lại từ file canbo.txt:")
        with open("canbo.txt", "r", encoding="utf-8") as fr:
            print(fr.read().strip())

    except (TuoiKhongHopLe, BacKhongHopLe) as e:
        print(f"Bắt lỗi Validation: {e}")