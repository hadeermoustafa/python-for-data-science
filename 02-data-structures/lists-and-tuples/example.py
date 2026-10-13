"""Lists and tuples: runnable examples. Run with: python examples.py
Change values and re-run to see what happens."""

print("--- Lists: indexing and slicing ---")
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0], fruits[-1])          # apple date
print(fruits[1:3])                    # ['banana', 'cherry']
print(fruits[::-1])                   # reversed copy

print("\n--- Lists: changing ---")
fruits[1] = "blueberry"
fruits.append("elderberry")
fruits.insert(0, "avocado")
fruits.remove("date")
print(fruits)

print("\n--- append vs extend ---")
a = [1, 2, 3]
a.append([4, 5])
b = [1, 2, 3]
b.extend([4, 5])
print(a)   # [1, 2, 3, [4, 5]]
print(b)   # [1, 2, 3, 4, 5]

print("\n--- sort vs sorted ---")
nums = [5, 2, 9, 1]
print(sorted(nums), nums)             # original unchanged
nums.sort()
print(nums)                           # now changed
print(sorted(["pear", "fig", "banana"], key=len))

print("\n--- The copying trap ---")
x = [1, 2]
y = x               # same list, two names
z = x.copy()        # independent copy
y.append(3)
print("x:", x, "| z:", z)

print("\n--- Nested list ---")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])                   # 6

print("\n--- Tuples ---")
point = (3, 4)
px, py = point                        # unpacking
px, py = py, px                       # swap
print(px, py)
first, *rest = (1, 2, 3, 4)
print(first, rest)
print(type((5,)), type((5)))          # the comma matters

try:
    point[0] = 10
except TypeError as err:
    print("Tuples can't change:", err)

print("\n--- A function returning a tuple ---")
def min_max(values):
    return min(values), max(values)

low, high = min_max([4, 1, 8])
print(low, high)

print("\n--- Tuple as a dictionary key ---")
places = {(40.7, -74.0): "New York"}
print(places[(40.7, -74.0)])
