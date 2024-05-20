f = open("przyklad.txt", "r")

# res = ""
# i = 1
#
# for row in f:
#     row = row.strip()
#     if i!= 1 and i%40 == 0:
#         res += row[9]
#     i += 1
#
# print(res)

# max_length = 0
# max_word = ""
#
# for row in f:
#     dict = {}
#     row = row.strip()
#     for element in row:
#         if element not in dict:
#             dict[element] = "a"
#     if len(dict) > max_length:
#         max_length = len(dict)
#         max_word = row
#
# print(max_word, max_length)

words = []

for row in f:
    row = row.strip()
    check = False
    for x in row:
        currentIndex = ord(x)
        for y in row:
            if ord(y) - currentIndex > 10:
                check = True
                break
            else:
                continue
    if check == False:
        words.append(row)



