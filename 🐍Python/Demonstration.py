a = 26

def area(Width, Length=2):
    area = Width * Length

    return area, (1, 2, 3)

area_a = area(5, 6)
print(area_a)
print(a)

a,b = area(5,6)
