"""Store frequency in dictonary
1.st  create a empty dictionary like freq_dict={}/dict()"""
#method1
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
freq_dict = {}
for i in num:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1
print(freq_dict)


#method2
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
freq_dict = {}
n = len(num)  
for i in range (0,n):
    freq_dict[num[i]] = freq_dict.get(num[i],0)+1  #get() method is used to get the value of the key if the key is not present in the dictionary then it will return the default value which is 0 in this case and then we add 1 to it to get the frequency of the element in the list
print(freq_dict)
   


"""Hashing in python
 restoring value in the same datastructure  like dict/list/set and the fething it""" 
n= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = [1, 2, 3, 4, 5]
for i in m:
    count = 0 
    for j in n:
        if i == j:
            count += 1
print(count)




# use print when you want to display something on the console and use return when you want to send a value back 

