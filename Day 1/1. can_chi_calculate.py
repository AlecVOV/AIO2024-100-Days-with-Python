def calculate_can_chi_calendar(year):
    if Input_year % 10 == 0:
        can = "Canh"
    elif Input_year % 10 == 1:
        can = "Tân"
    elif Input_year % 10 == 2:
        can = "Nhâm"
    elif Input_year % 10 == 3:
        can = "Quý"
    elif Input_year % 10 == 4:
        can = "Giáp"
    elif Input_year % 10 == 5:
        can = "Ất"
    elif Input_year % 10 == 6:
        can = "Bính"
    elif Input_year % 10 == 7:
        can = "Dinh"
    elif Input_year % 10 == 8:
        can = "Mậu"
    elif Input_year % 10 == 9:
        can = "Kỷ"
    
    if Input_year % 12 == 0:
        chi = "Thân"
    elif Input_year % 12 == 1:
        chi = "Dậu"
    elif Input_year % 12 == 2:
        chi = "Tuất"
    elif Input_year % 12 == 3:
        chi = "Hợi"
    elif Input_year % 12 == 4:
        chi = "Tý"
    elif Input_year % 12 == 5:
        chi = "Sửu"
    elif Input_year % 12 == 6:
        chi = "Dần"
    elif Input_year % 12 == 7:
        chi = "Mẹo"
    elif Input_year % 12 == 8:
        chi = "Thìn"
    elif Input_year % 12 == 9:
        chi = "Tỵ"
    elif Input_year % 12 == 10:
        chi = "Ngọ"
    elif Input_year % 12 == 11:
        chi = "Mùi"

    result = can + " " + chi
    return result

Input_year = int(input("Please enter the year you want to check!!!"))
result = calculate_can_chi_calendar(Input_year)
print(result)

