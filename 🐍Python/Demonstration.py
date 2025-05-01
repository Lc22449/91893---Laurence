a = 26

def area(Width, Length=2):
    area = Width * Length
    global a
    a = 25
    return area, a

area_a = area(5, 6)
print(area_a)
print(a)

a,b = area(5,6)
