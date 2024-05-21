f = open("pi.txt", "r")



# rozwiazania = []
# para = ""
# tablica = []
#
# for row in f:
#     row = row.strip()
#     tablica.append(row)
#
# for i in range(0, len(tablica)-1):
#     para = tablica[i] + "" + tablica[i+1]
#     para = int(para)
#     if para > 90:
#         rozwiazania.append(para)
#
# print(len(rozwiazania))



# dict = {}
# para = ""
# tablica = []
#
# for row in f:
#     row = row.strip()
#     tablica.append(row)
#
# for i in range(0, 10):
#     for j in range(0, 10):
#         pair = str(i)+""+str(j)
#         dict[pair] = 0
#
# for i in range(0, len(tablica)-1):
#     para = tablica[i] + "" + tablica[i+1]
#
#     if para in dict:
#         dict[para] += 1
#
# print(dict)



tablica = []
ciag = ""
ciagi = []

for row in f:
    row = row.strip()
    tablica.append(row)

for i in range(0, len(tablica)-5):
    ciag = tablica[i]+""+tablica[i+1]+""+tablica[i+2]+""+tablica[i+3]+""+tablica[i+4]+""+tablica[i+5]

    if (int(ciag[0]) < int(ciag[1]) and int(ciag[1]) < int(ciag[2])) and (int(ciag[2]) >= int(ciag[3]) and int(ciag[3]) > int(ciag[4]) and int(ciag[4]) > int(ciag[5])):
        ciagi.append(ciag)

print(len(ciagi))
