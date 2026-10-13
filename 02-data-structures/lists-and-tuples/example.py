"""Lists and tuples: runnable examples. Run with: python examples.py
Change values and re-run to see what happens. Matches notes.md section by section."""

print("=== LISTS ===")

print("\n--- Creating, indexing, len ---")
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0], fruits[-1])          # apple date
print(len(fruits))                    # 4
print(len([]))                        # 0

print("\n--- Slicing ---")
print(fruits[1:3])                    # ['banana', 'cherry']
print(fruits[:2])                     # from the start
print(fruits[2:])                     # to the end
print(fruits[::2])                    # every second item
print(fruits[::-1])                   # reversed copy

print("\n--- Modifying ---")
fruits[1] = "blueberry"
print(fruits)

print("\n--- Adding: append, insert, extend ---")
a = [1, 2, 3]
a.append(4)                           # one item at the end
a.insert(0, 99)                       # at a position
print(a)                              # [99, 1, 2, 3, 4]

b = [1, 2, 3]
b.append([4, 5])                      # goes in as ONE item
c = [1, 2, 3]
c.extend([4, 5])                      # each item added
print(b)                              # [1, 2, 3, [4, 5]]
print(c)                              # [1, 2, 3, 4, 5]

print("\n--- Removing: del, pop, remove ---")
x = [10, 20, 30, 40, 50]
del x[1]                              # by position
print(x)                              # [10, 30, 40, 50]
print(x.pop(0), x)                    # pop with an index
print(x.pop(), x)                     # pop with no index = last item
names = ["a", "b", "c", "b"]
names.remove("b")                     # first match only
print(names)                          # ['a', 'c', 'b']

print("\n--- Searching: count, index, in ---")
l = ["a", "b", "c", "b"]
print(l.count("b"))                   # 2
print(l.index("b"))                   # 1
print("c" in l)                       # True
print("z" in l)                       # False

print("\n--- Sorting and reversing ---")
nums = [5, 2, 9, 1]
print(sorted(nums), nums)             # new list, original unchanged
nums.sort()                           # changes the list itself
print(nums)
nums.sort(reverse=True)               # descending, in place
print(nums)
steps = [1, 2, 3, 4, 5]
steps.reverse()                       # flips the order in place
print(steps)
print(sorted(["pear", "fig", "banana"], key=len))

print("\n--- max, min, sum ---")
scores = [3, 7, 2]
print(max(scores), min(scores), sum(scores))

print("\n--- The copying trap ---")
p = [1, 2]
q = p                                 # same list, two names
r = p.copy()                          # independent copy
q.append(3)
print("p:", p, "| r:", r)             # p changed, r did not

print("\n--- Nested list ---")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])                   # 6
print(len([1, [2, 3], 4]))            # 3, the inner list counts as one

print("\n--- Looping ---")
for i, color in enumerate(["red", "green"], start=1):
    print(i, color)

print("\n=== TUPLES ===")

print("\n--- Creating, indexing, slicing ---")
t = (1, 2, 3)
print(t[0], t[1:])
print(type((5,)), type((5)))          # the comma makes the tuple

print("\n--- Immutability ---")
try:
    t[0] = 9
except TypeError as err:
    print("Tuples can't change:", err)

print("\n--- Unpacking ---")
px, py = (3, 4)
px, py = py, px                       # swap
print(px, py)
first, *rest = (1, 2, 3, 4)
print(first, rest)

print("\n--- count, index ---")
basket = ("apple", "banana", "apple", "orange")
print(basket.count("apple"))          # 2
print(basket.index("apple"))          # 0, first match
print(basket.index("orange"))         # 3

print("\n--- len, sum, min, max ---")
numbers = (10, 20, 5, 30)
print(len(numbers), sum(numbers), min(numbers), max(numbers))
print(sorted(numbers))                # a list, not a tuple

print("\n--- Converting ---")
print(list((1, 2, 3)), tuple([1, 2, 3]))

print("\n--- A function returning a tuple ---")
def min_max(values):
    return min(values), max(values)

low, high = min_max([4, 1, 8])
print(low, high)

print("\n--- Tuple as a dictionary key ---")
places = {(40.7, -74.0): "New York"}
print(places[(40.7, -74.0)])
