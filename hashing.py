"""Store frequency in dictonary
1.st  create a empty dictionary like freq_dict={}/dict()"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
freq_dict = {}
for i in num:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1
print(freq_dict)