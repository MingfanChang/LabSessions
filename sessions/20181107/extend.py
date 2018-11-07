"""

Extend versus append

Both are methods defined for lists and both take one argument and both add to the
end of the list. But append(x) adds just x as one element at the end and extend(x)
adds all elements of x to the end (so x needs to be a sequence).

Note that the following two are the same

    lst.append(0)
    lst.extend([0])

"""


list1 = [1, 2]
list2 = [3, 4]

extend = True

if extend:
    # after this list1 is "[1, 2, [3, 4]]"
    list1.extend(list2)
else:
    # after this list1 is "[1, 2, 3, 4]"
    list1.append(list2)
