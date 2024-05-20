f = open("instrukcje.txt", "r")

# length = 0
#
# for row in f:
#     row = row.strip()
#
#     instruction = row.split()[0]
#     if instruction == "DOPISZ":
#         length+=1
#     elif instruction == "USUN":
#         length -= 1
# print(length)



# maxLength = 0
# currentLength = 0
# longestSequence = ""
# previousInstruction = f.readline().split()[0]
#
# for row in f:
#     row = row.strip()
#
#     instruction = row.split()[0]
#     if previousInstruction == instruction:
#         currentLength += 1
#     else:
#         previousInstruction = instruction
#         currentLength = 1
#     if currentLength > maxLength:
#         maxLength = currentLength
#         longestSequence = instruction
#
# print(longestSequence)
# print(maxLength)



# dict = {}
#
# for row in f:
#     row = row.strip()
#     instruction = row.split()[0]
#     letter = row.split()[1]
#
#     if instruction == "DOPISZ":
#         if letter in dict:
#             dict[letter] += 1
#         else:
#             dict[letter] = 1
# print(dict)



# output = []
#
# for row in f:
#     row = row.strip()
#     instruction = row.split()[0]
#     letter = row.split()[1]
#
#     if instruction == "DOPISZ":
#         output.append(letter)
#     elif instruction == "ZMIEN":
#         output[len(output)-1] = letter
#     elif instruction == "USUN":
#         output.pop(len(output)-1)
#     elif instruction == "PRZESUN":
#         for i in range(0, len(output)):
#             if letter == output[i]:
#                 if letter != "Z":
#                     output[i] = chr(ord(output[i])+1)
#                 else:
#                     output[i] = "A"
#                 break
#
# print(''.join(output))
