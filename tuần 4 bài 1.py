class NhanVien:
    def __init__(self, ma_nv="", ten="", luong_co_ban=0.0):
        # Đóng gói: Thuộc tính private với hai dấu gạch dưới __
        self.__ma_nv = ma_nv
        self.__ten = ten
        self.__luong_co_ban = luong_co_ban

    # --- Getter ---
    def get_ma_nv(self):
        return self.__ma_nv

    def get_ten(self):
        return self.__ten

    def get_luong_co_ban(self):
        return self.__luong_co_ban

    # --- Setter ---
    def set_ma_nv(self, ma_nv):
        self.__ma_nv = ma_nv

    def set_ten(self, ten):
        self.__ten = ten

    def set_luong_co_ban(self, luong_co_ban):
        if luong_co_ban >= 0:
            self.__luong_co_ban = luong_co_ban
        else:
            print("Lương không hợp lệ!")

    # --- Các phương thức nghiệp vụ ---
    def tinhLuong(self):
        # Tùy theo hệ số hoặc phụ cấp, ở đây trả về lương cơ bản
        return self.__luong_co_ban

    def tangLuong(self, so_tien_tang):
        if so_tien_tang > 0:
            self.__luong_co_ban += so_tien_tang
            print(f"Đã tăng {so_tien_tang} cho nhân viên {self.__ten}.")
        else:
            print("Mức tăng lương phải lớn hơn 0.")

    def inTTin(self):
        print(f"Mã NV: {self.__ma_nv} | Tên: {self.__ten} | Tổng lương: {self.tinhLuong():.2f}")


# Ví dụ sử dụng:
if __name__ == "__main__":
    print("--- TEST BÀI 1 ---")
    nv = NhanVien("NV01", "Hoà Thị Mai Anh", 10000)
    nv.inTTin()
    nv.tangLuong(2000)
    nv.inTTin()