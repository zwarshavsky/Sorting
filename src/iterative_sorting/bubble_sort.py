# import random 

# l = []
# for i in range(1,21):
#     l.append(random.randrange(1, 20))



l = [11, 3, 17, 15, 5]

print(l)

swapped = True
while swapped == True:
    swapped = False 
    for index in range(len(l)-1):
        print(index)
        if l[index] > l[index+1]:
            print("before:",l[index],l[index+1])
            l[index],l[index+1] = l[index+1],l[index] 
            swapped = True
            print("after:",l[index],l[index+1])
            print("bigger:",index)
        else:
            print("smaller:",index)

print(l)
