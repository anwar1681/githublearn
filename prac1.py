import os
# flashcard program
class Flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word +'('+ self.meaning +')'

flash = []
print("Welcome to Flashcard Program")
with open("flashcard.txt",'a') as wf:
    while True:
        word = input("Enter word:  ")
        meaning = input("Enter meaning of the word:  ")
        flash.append(Flashcard(word,meaning))
        option = int(input("0 to continue adding word and meaning 1 to break: "))
        if option:
            break
    print("\n your flashcard")
    
    session = int(input("enter 1 if session break or 2 to add to existing session:  "))
    if session == 1:
        wf.write("\tFlash Card\n\n")
        for i in flash:
            print(">", i)
            wf.write(f"> {i}\n")
    else:
        for i in flash:
            print(">", i)
            wf.write(f"> {i}\n")    
wf.close()
os.system('start flashcard.txt')

# random number
import random
# def rand(start, end, num):
#     res = []
#     for i in range(num):
#         res.append(random.randint(start,end))
#     return res
# start = 10
# end = 40
# num = 10
# print(rand(start,end,num))

# we can also use numpy  res.append(np.random.randint(start,end))

# numbers in a list of a given range
# def count(l1,l,r):
#     c = 0
#     for x in l1:
#         if x <= r and x>=l:
#             c +=1
#     return c           # in one line also  return len(list(x for x in l1 if l <= x <= r))
# l1 = [3,6,13,11,15,67,55,41]
# l = 13
# r = 55
# print(count(l1,l,r))

# in a list, a given range elements are replaced by a given number
# test_list = [3,6,4,8,9,12,11,32,54,43,21,31]
# print("original test_list: ", test_list)
# i,j = 5,9
# k = 11
# test_list[i:j] = [k]*(j-i)  # or can be   repeat(k,(j-i))
# print("updated test_list is: "+ str(test_list))

# replace elm in a list with given two elms if greater or lesser than given elm
# orig_list = [3,6,8,2,9,11,31,22,54]
# print("original list: ",orig_list)
# res = []
# k=6
# i,j=4,7
# for ele in orig_list:
#     if ele>k:
#         res.append(j)
#     else:
#         res.append(i)
# print("updated list:", res)

# replace elm of sec list with index of same elm in ist list
# lst1 = ['pass','fail','tass']
# lst2 = ['pass','tass','fail','pass','tass','fail']
# lst3 = []
# for x in lst2:
#     for y in lst1:
#         if x == y:
#             lst3.append(lst1.index(y))
# print("initial list1 and list2 are: ")
# print(lst1,"\n",lst2)
# print("lst3 after replacement is: ",lst3)

# same by list comprehension
# lst1 = ['pass','fail','tass']
# lst2 = ['pass','tass','fail','pass','tass','fail']
# temp = {y:x for x,y in enumerate(lst1)}
# lst3 = [temp.get(elem) for elem in lst2]

# print("initial list1 and list2 are: ")
# print(lst1,"\n",lst2)
# print("lst3 after replacement is: ",lst3)

#  using map
lst1 = ['pass','fail','tass']
lst2 = ['pass','tass','fail','pass','tass','fail']
elem = {k:i for i, k in enumerate(lst1)}
lst3 = list(map(elem.get,lst2))

print("initial list1 and list2 are: ")
print(lst1,"\n",lst2)
print("lst3 after replacement is: ",lst3)


