codes = ["level", "power", "racecar", "deed", "fight", "meme", "run"]
list = []
for i in codes:
    if i == i[::-1]:
        list.append(i)

print(list)