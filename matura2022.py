f = open("przyklad.txt", "r")

# counter = 0
# firstNumber = ""
#
# for row in f:
#     row = row.strip()
#     if row[0] == row[-1]:
#         if counter == 0:
#             firstNumber = row
#         counter += 1
#
# print(firstNumber)
# print(counter)



# primeFactors = []
# def getPrimeFactors(number):
#     counter = 0
#     for i in range(2, number+1):
#         for j in range(2, number+1):
#             if i%j == 0:
#                 counter+=1
#         if counter <= 1:
#             primeFactors.append(i)
#         counter = 0
#     return primeFactors
#
# mostDifferentFactorsCount = 0
# mostDifferentFactorsNumber = 0
# mostFactorsNumber = 0
# mostFactorsCount = 0
#
# for row in f:
#     row = row.strip()
#     row = int(row)
#     factors = []
#     tempNumber = row
#     while tempNumber != 1:
#         tempFactors = getPrimeFactors(tempNumber)
#         for i in range(0, len(tempFactors)):
#             if tempNumber % tempFactors[i] == 0:
#                 tempNumber /= tempFactors[i]
#                 factors.append(tempFactors[i])
#
#         if(len(factors) > mostFactorsCount):
#             mostFactorsCount = len(factors)
#             mostFactorsNumber = row
#
#         dict = {}
#         for x in factors:
#             if x not in dict:
#                 dict[x] = 1
#             else:
#                 dict[x] += 1
#
#         if len(dict) > mostDifferentFactorsCount:
#             mostDifferentFactorsCount = len(dict)
#             mostDifferentFactorsNumber = row
#         factors = []
#
# print(mostFactorsNumber)
# print(mostFactorsCount)
#
# print(mostDifferentFactorsNumber)
# print(mostDifferentFactorsCount)


numbers = []
for row in f:
    row = row.strip()
    numbers.append(int(row))
threeCounter = 0
threes = []

for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            if numbers[i] != numbers[j] and numbers[j] != numbers[k] and numbers[j]%numbers[i] == 0 and numbers[k]%numbers[j] == 0:
                threeCounter += 1
                three = str(numbers[i]) + " " + str(numbers[j]) + " " + str(numbers[k])
                threes.append(three)

fives = 0

for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        for k in range(len(numbers)):
            for l in range(len(numbers)):
                for m in range(len(numbers)):
                    if numbers[i] != numbers[j] and numbers[j] != numbers[k] and numbers[k] != numbers[l] and numbers[l] != numbers[m] and numbers[m] % numbers[l] == 0 and numbers[l] % numbers[k] == 0 and numbers[k] % numbers[j] == 0 and numbers[j] % numbers[i] == 0:
                        fives += 1

print(threeCounter, threes)
print(fives)



