#Program 2 set operations
#Rachel Martinez

A = [1,3,5,6,8]
B = [2,3,4,7,9]

C = [1,3,5,6,8] #copy of A for Union

#logic for Union with dup vals
for item in B:
    C.append(item)

print("A U B: {" + str(C)[1:-1] + "}")

#logic for Intersection
Inter = []

for item in A:
    if item in B:
        Inter.append(item)

print("A n B: {" + str(Inter)[1:-1] + "}")

#logic for Difference = array Diff
Diff = []

for item in A:
    if item not in B:
        Diff.append(item) 

print("A - B: {" + str(Diff)[1:-1] + "}")
            

