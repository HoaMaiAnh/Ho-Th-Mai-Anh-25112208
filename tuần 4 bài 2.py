import copy

class Point:
    """Lớp Point phụ trợ để tạo d1, d2 cho LineSegment"""
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
        
    # Getter & Setter cho Point
    def get_x(self): return self.__x
    def set_x(self, x): self.__x = x
    def get_y(self): return self.__y
    def set_y(self, y): self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class LineSegment:
    def __init__(self, p1=None, p2=None):
        """
        Constructor gộp xử lý 3 trường hợp: 
        1. Mặc định (không truyền tham số)
        2. Copy Constructor (truyền vào 1 LineSegment)
        3. Có đối số (truyền vào 2 Point)
        """
        # Trường hợp Copy constructor (Sao chép sâu từ 1 đoạn thẳng khác)
        if isinstance(p1, LineSegment):
            self.__d1 = copy.deepcopy(p1.get_d1())
            self.__d2 = copy.deepcopy(p1.get_d2())
            
        # Trường hợp Constructor có đối số (2 Point) hoặc Mặc định (None)
        else:
            # Dùng deepcopy để đảm bảo tính đóng gói an toàn (không bị ảnh hưởng bởi tham chiếu bên ngoài)
            self.__d1 = copy.deepcopy(p1) if p1 is not None else Point(0, 0)
            self.__d2 = copy.deepcopy(p2) if p2 is not None else Point(0, 0)

    # --- Getter & Setter ---
    def get_d1(self):
        return self.__d1

    def set_d1(self, p):
        self.__d1 = copy.deepcopy(p)

    def get_d2(self):
        return self.__d2

    def set_d2(self, p):
        self.__d2 = copy.deepcopy(p)

    def inTTin(self):
        print(f"Đoạn thẳng: Điểm bắt đầu d1={self.__d1}, Điểm kết thúc d2={self.__d2}")


# Ví dụ sử dụng:
if __name__ == "__main__":
    print("\n--- TEST BÀI 2 ---")
    
    # Tạo 2 điểm
    pA = Point(1, 2)
    pB = Point(4, 6)
    
    # 1. Test Constructor có đối số
    line1 = LineSegment(pA, pB)
    print("Line 1 (Có đối số):", end=" ")
    line1.inTTin()
    
    # 2. Test Constructor mặc định
    line2 = LineSegment()
    print("Line 2 (Mặc định):", end=" ")
    line2.inTTin()
    
    # 3. Test Constructor sao chép sâu
    line3 = LineSegment(line1)
    print("Line 3 (Copy từ Line 1):", end=" ")
    line3.inTTin()
    
    # Chứng minh sao chép sâu: Thay đổi pA ban đầu sẽ không làm ảnh hưởng tới line1
    pA.set_x(999)
    print("\nSau khi thay đổi Point pA gốc:")
    print("Tọa độ pA hiện tại:", pA)
    print("Line 1 không bị thay đổi:", end=" ")
    line1.inTTin()