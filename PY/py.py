num = [1,4,9,16,25]


# # list
# print(num[2:])      # [9, 16, 25]
# print(num[-3:])     # [9, 16, 25]
# print(num[::-1])    # [25, 16, 9, 4, 1]
# print(list(range(0, 10, 3))) # [0, 3, 6, 9]
# for i in range(len(num)):
#     print(i, num[i])
# print(sum(range(4))) # 6 (0 + 1 + 2 + 3)
"""
    list - dynamic
    touple - static (like array - continuous and fast) - only .index() & .count()
"""
# emptyTuple = ()
# singleTuple = "Hi", # <-- note trailing comma
# print(len(emptyTuple), len(singleTuple), emptyTuple, singleTuple)


# # Data Structures
# num.append(-1) # adds at end
# newList = [300, 200, 100]
# num.extend(newList) # adds iterable elements at end and flattens it
# num.insert(0, -1); # inserts ele at given pos
# num.remove(-1) # removes first item, raises valueErr if couldn't find
# x = num.pop(5) # removes last ele by default or ele at given index, raises indexErr if arr is empty or pos is out of bound
# print(x)
# del num[0]
# # num.clear() # removes all items, similar to del num[:]
# ind = num.index(16, 0, len(num)) # returns ind of target else valueErr
# print(ind)
# print(num.count(25)) # returns the #times val have appeared
# num.sort() # sorts in-place
# num.reverse()
# arr = num.copy() # returns the shallow copy(changes do not affect the original)
# arr[0] = 700
# print(arr)
# print(num)


# # function
# # f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2)
# # places no restrictions on the calling convention and arguments may be passed by position or keyword
# def sayHi1(person):
#     print(f"Hi {person}")
    
# def sayHi2(person, /): # restricted to only use positional parameters
#     print(f"Hi {person}")
    
# def sayHi3(*, person, title): # only allows keyword arguments
#     print(f"Hi {person} - {title}")

# sayHi3(person="Satyajit", title="Patel")

# # any para/args comes afrer *args are "keyword-only" args
# def concat(*args, separator='/'):
#     return separator.join(args)
#     # join -> combines ele of an iterable(list, tuple, set) into a single string

# print(concat("MSD", "ABD", "VK"))
# print(concat("MSD", "ABD", "VK", separator="+"))


# # lamda function -> (anonymous(noName)-singleLine-autoReturn)
# # lambda arguments : expression
# addTen = lambda ele: ele + 10
# print(addTen(10))
# map(): Applies calc to every item in an iterable
# filter(): Selects items from an iterable that meet a condition
# filter(func, iterable)
# print(list(filter(lambda ele: ele%2 == 0, [1,2,3,4,5])))
# print(list(map(lambda ele: ele * 2, [1,2,3,4,5])))
# pairs = [(2, 'two'), (1, 'one'), (3, 'three'), (4, 'four')]
# print(pairs)
# for ele in pairs[0]:
#     print(ele, end=" ")
# print()
# pairs.sort()
# print(pairs)
# pairs.sort(key=lambda pair: pair[1]) # sort by 2nd ele of array
# print(pairs)

# def f(a: int, b: int = 10) -> int:
#     """
#         returns addition of 2 nums.
#         Incase one para is given then adds 10 by default
#     """
#     print(f.__doc__)
#     print(f.__annotations__)
#     return a + b;
# print(f(10))


# # using list as a stack(LIFO)
# stack = num
# print(stack)
# stack.append(4)
# print(stack)
# stack.pop()
# print(stack)

# # queue(FIFO)
# # however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
# from collections import deque
# queue = deque(num)
# print(queue)
# queue.rotate(1)
# print(queue)
"""
    deque
        .append()
        .appendleft()
        .extend()
        .extendleft()
        
        .index()
        .insert()
        
        .remove()
        .pop()
        .popleft()
        
        .reverse()
        .rotate(n=1)
            +ve -> rotates n step to right
            -ve -> rotates n step to left
        
        .clear()
        .copy()
            copy1 = num # assignment copy - creates reference(changes affect the original)
            copy2 = num.copy() # shallow copy - creates new independent object in memory containing same value
        .count()
"""
# copy1 = num
# print(num, "\n", copy1, sep="")
# copy1[0] = -1
# print(f"{num}\n{copy1}")


# # map/dict
# ipl = [('csk', 'msd'), ('rcb', 'vk'), ('mi', 'rs')]
# print(ipl)
# from collections import defaultdict
# mapIpl = defaultdict(list)
# for k, v in ipl:
#     mapIpl[k] = v
# print(mapIpl)
# mapIpl["kkr"].append("rahane")
# print(sorted(mapIpl.items()))
# name = "SATYAJIT"
# m = defaultdict(int)
# for k in name:
#     m[k] += 1
# print(sorted(m.items()))


# # list comprehension
# squares1 = list(map(lambda k: k**2, range(6)))
# # or
# squares2 = [k**2 for k in range(6)]
# print(f"{squares1}\n{squares2}")
# makePair = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(makePair)
# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# n = len(matrix[0])
# m = len(matrix)
# print(n, m)
# print(matrix)
# transposed = []
# for i in range(n):
#     temp = []
#     for j in range(m):
#         # print(j,i,"-", matrix[j][i],",", end=" ")
#         temp.append(matrix[j][i])
#     transposed.append(temp)
#     # print()
# # or
# # for i in range(n):
# #     transposed.append([row[i] for row in matrix])
# print(transposed)


# # string
# s = "satyajit"
# print(s.upper())
# print(s.split('y')) # ['sat', 'ajit'] - iterable.split(separator)
# print("->".join(s)) # separator.join(iterable)
# print("  Hi".strip())
# print("I Like Java and Java".replace("Java", "Python")) # (old, new)
# flag = s.startswith("sat") and s.endswith("jit")
# print(flag) # True
# print("Python".isalpha()) # True


# # set (an unordered collection with no duplicate elements)
# emptySet = set()
# emptyDict = {}
# print(len(emptySet), len(emptyDict))
# s1 = set("satyajit")
# s2 = {'p','a','t','e','l'}
# print(s1)
# print(s2)
# intersection = s1 & s2
# print(intersection)
# flag = 's' in intersection # False
# print(flag)
# s1.update([1,2,3], {10, 20})
# print(s1)
"""
    set
        .add(ele)
        .update(iterable)
        
        .remove(ele) # raises keyErr if ele not present
        .discard(ele) # no err even if ele doesn't present
        
        .pop() # removes and return an random ele
        .copy() # shallow copy
        .clear()
"""


































