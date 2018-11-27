def sorted(a):
    for index in range(1,len(a)):
        temp = a[index]
        i = index -1
        while i >= 0:
            if temp < a[i]:
                a[i + 1] = a[i]
                a[i]= temp
                i = i -1
            else:
                break


lst = [12,4,4,1,12,5,445,9,7,3,9,1,9,78,12,99,42,78,99,102,8,1,4,8415,48,51,56,648,4,81,68,456,4,81,68,415,4,8,8,1,845,4,4,84,5,18,4,1564,8,45,1,584,8,45,1,84,81,65]
print(lst)
sorted(lst)
print(lst)


def insertionsort(alist):
    for index in range(1, len(alist)):

        currentval= alist[index]
        position = index

        while position > 0 and alist[position-1]> currentval:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentval

lst = [12,4,4,1,12,5,445,9,7,3,9,1,9,78,12,99,42,78,99,102,8,1,4,8415,48,51,56,648,4,81,68,456,4,81,68,415,4,8,8,1,845,4,4,84,5,18,4,1564,8,45,1,584,8,45,1,84,81,65]
print('second',lst)
insertionsort(lst)
print('second',lst)
