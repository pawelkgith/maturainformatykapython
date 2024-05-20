import functools

f = open("przyklad.txt", "r")

# counter = 0
#
# for row in f:
#     row = row.strip()
#     row = int(row)
#     for i in range(0, row):
#         if 3**i == row:
#            counter+=1
#
# print(counter)

wartosciSilni = []
silnia = 1
rozwiazania = []
j = 1

for row in f:
    row = row.strip()
    silnia = 1
    wartosciSilni = []
    sumaSilni = 0
    for x in row:
        for i in range(0, int(x)):
            silnia *= j
            j+=1
        j = 1
        wartosciSilni.append(silnia)
    sumaSilni = functools.reduce(lambda x,y: x+y, wartosciSilni)
    print(sumaSilni)
print(rozwiazania)
