def calculate_can_chi_calendar(year):
    can = ""
    if year % 10 == 0:
        can = "Canh"
    elif year % 10 == 1:
        can = "Tân"
    elif year % 10 == 2:
        can = "Nhâm"
    elif year % 10 == 3:
        can = "Quý"
    elif year % 10 == 4:
        can = "Giáp"
    elif year % 10 == 5:
        can = "Ất"
    elif year % 10 == 6:
        can = "Bính"
    elif year % 10 == 7:
        can = "Đinh"
    elif year % 10 == 8:
        can = "Mậu"
    elif year % 10 == 9:
        can = "Kỉ"

    chi = ""
    if year % 12 == 0:
        chi = "Thân"
    if year % 12 == 1:
        chi = "Dậu"
    if year % 12 == 2:
        chi = "Tuất"
    if year % 12 == 3:
        chi = "Hợi"
    if year % 12 == 4:
        chi = "Tý"
    if year % 12 == 5:
        chi = "Sửu"
    if year % 12 == 6:
        chi = "Dần"
    if year % 12 == 7:
        chi = "Mẹo"
    if year % 12 == 8:
        chi = "Thìn"
    if year % 12 == 9:
        chi = "Tỵ"
    if year % 12 == 10:
        chi = "Ngọ"
    if year % 12 == 11:
        chi = "Mùi"

    return f"Can chi của bạn là: {can} {chi}"

year = int(input("Vui lòng nhâp năm sinh của bạn:"))
result = calculate_can_chi_calendar(year)
print (result)