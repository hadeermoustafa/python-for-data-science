# Lists and tuples

These are the two most common ways to hold a sequence of items in Python. Almost every data task starts with one of them: a column of numbers, a row of a table, a batch of file names.

The one-sentence difference: **a list can be changed after you create it, a tuple cannot.**

Think of a list as a shopping list written in pencil (you can add, cross out and reorder), and a tuple as a printed ticket (what is written stays written).

> Every code block below is runnable. Copy it into a Python shell, a Jupyter notebook or [Google Colab](https://colab.research.google.com) and change things to see what happens. Lines starting with `#` show the output.

---

## 1. Lists

### Creating a list

Use square brackets and commas. Items can be any type, and types can be mixed.

```python
fruits = ["apple", "banana", "cherry", "date"]
mixed = [42, "hello", 3.14, True]
empty = []
```

### Indexing: getting one item

Positions start at **0**, not 1. Negative numbers count from the end.

| item | apple | banana | cherry | date |
|---|---|---|---|---|
| index | 0 | 1 | 2 | 3 |
| negative index | -4 | -3 | -2 | -1 |

```python
print(fruits[0])    # apple
print(fruits[3])    # date
print(fruits[-1])   # date   (last item)
print(fruits[-2])   # cherry
```

Asking for a position that doesn't exist raises an error:

```python
fruits[10]
# IndexError: list index out of range
```

### Slicing: getting a range

`list[start:stop]` returns items from `start` up to, **but not including**, `stop`. A third number sets the step.

```python
print(fruits[1:3])    # ['banana', 'cherry']
print(fruits[:2])     # ['apple', 'banana']      (start omitted = from the beginning)
print(fruits[2:])     # ['cherry', 'date']       (stop omitted = to the end)
print(fruits[::2])    # ['apple', 'cherry']      (every second item)
print(fruits[::-1])   # ['date', 'cherry', 'banana', 'apple']   (reversed)
```

A slice always gives you a **new list** and never raises an `IndexError`, even if the numbers go past the end.

### Changing items

Because lists are mutable, you can replace an item directly:

```python
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'cherry', 'date']
```

### Adding items

```python
a = [1, 2, 3]
a.append(4)         # add ONE item at the end
a.insert(0, 99)     # add at position 0
print(a)            # [99, 1, 2, 3, 4]
```

**`append` vs `extend`** is a classic beginner trap:

```python
a = [1, 2, 3]
a.append([4, 5])
print(a)   # [1, 2, 3, [4, 5]]     the whole list went in as ONE item

b = [1, 2, 3]
b.extend([4, 5])
print(b)   # [1, 2, 3, 4, 5]       each item was added separately
```

You can also join lists with `+`, which makes a new list:

```python
print([1, 2] + [3, 4])   # [1, 2, 3, 4]
```

### Removing items

```python
x = [10, 20, 30, 40]
del x[1]            # delete by position
print(x)            # [10, 30, 40]

print(x.pop(0))     # 10   (pop removes AND returns the item)
print(x)            # [30, 40]

print(x.pop())      # 40   (no index given = the last item)
print(x)            # [30]

names = ["a", "b", "c", "b"]
names.remove("b")   # removes only the FIRST "b"
print(names)        # ['a', 'c', 'b']
```

| Want to remove... | Use |
|---|---|
| the item at a position | `del lst[i]` or `lst.pop(i)` |
| the last item | `lst.pop()` |
| the first item with a given value | `lst.remove(value)` |

### Searching and counting

```python
l = ["a", "b", "c", "b"]
print(l.index("b"))   # 1     position of the first match
print(l.count("b"))   # 2     how many times it appears
print("c" in l)       # True  is it in the list?
```

`index()` raises a `ValueError` if the value isn't there, so check with `in` first when you're not sure:

```python
if "z" in l:
    print(l.index("z"))
else:
    print("not found")   # not found
```

### Length: `len()`

`len()` tells you how many items are in a list. It's also the safe way to find the last index: it's always `len(lst) - 1`.

```python
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))        # 4
print(len([]))            # 0     an empty list has length 0
print(fruits[len(fruits) - 1])   # date   (same as fruits[-1])
```

`len()` counts only the **top-level** items. A nested list counts as one item:

```python
print(len([1, [2, 3], 4]))   # 3
```

### Other useful built-in functions

These work on lists of numbers:

```python
scores = [3, 7, 2]
print(max(scores))   # 7     largest
print(min(scores))   # 2     smallest
print(sum(scores))   # 12    total
```

### Sorting

`sort()` changes the list itself. `sorted()` leaves it alone and gives you a new one.

```python
nums = [5, 2, 9, 1]
print(sorted(nums))                 # [1, 2, 5, 9]
print(nums)                         # [5, 2, 9, 1]   (unchanged)
print(sorted(nums, reverse=True))   # [9, 5, 2, 1]

nums.sort()
print(nums)                         # [1, 2, 5, 9]   (now changed)
```

Both `sort()` and `sorted()` accept `reverse=True` for descending order. The in-place version looks like this:

```python
scores = [5, 2, 8, 1, 9]
scores.sort(reverse=True)
print(scores)   # [9, 8, 5, 2, 1]
```

You can sort by a rule with `key`:

```python
words = ["pear", "fig", "banana"]
print(sorted(words, key=len))   # ['fig', 'pear', 'banana']   (shortest first)
```

> **Common mistake:** `nums = nums.sort()` sets `nums` to `None`, because `sort()` changes the list in place and returns nothing. Write `nums.sort()` on its own line, or use `sorted()`.

### Reversing

`reverse()` flips the order of the list itself, in place. It does **not** sort, it just reverses whatever order is there.

```python
steps = [1, 2, 3, 4, 5]
steps.reverse()
print(steps)   # [5, 4, 3, 2, 1]
```

| Want to... | Use |
|---|---|
| reverse the list itself | `lst.reverse()` |
| get a reversed copy and keep the original | `lst[::-1]` |

### Looping over a list

```python
for fruit in ["apple", "banana"]:
    print(fruit)

# need the position too? use enumerate
for i, color in enumerate(["red", "green"], start=1):
    print(i, color)
# 1 red
# 2 green
```

### Nested lists

A list can hold other lists. This is how you represent a small table or grid.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0])      # [1, 2, 3]       first row
print(matrix[1][2])   # 6               row 1, column 2
```

Read `matrix[1][2]` from left to right: take row 1, then take item 2 of that row.

### The copying trap

`b = a` does **not** copy a list. It gives the same list a second name.

```python
a = [1, 2]
b = a
b.append(3)
print(a)   # [1, 2, 3]   a changed too!

c = a.copy()   # a real, independent copy (a[:] works as well)
c.append(99)
print(a)   # [1, 2, 3]   a is untouched
```

This surprises almost everyone once. Remember: variables point to a list, they don't hold their own copy of it.

---

## 2. Tuples

### Creating a tuple

Use parentheses, or just commas.

```python
point = (3, 4)
colors = ("red", "green", "blue")
```

Indexing and slicing work exactly like lists:

```python
t = (1, 2, 3)
print(t[0])    # 1
print(t[1:])   # (2, 3)
```

### The one-item tuple

The **comma** makes the tuple, not the parentheses.

```python
print(type((5,)))   # <class 'tuple'>
print(type((5)))    # <class 'int'>   just the number 5 in brackets
```

### Immutability

```python
t[0] = 9
# TypeError: 'tuple' object does not support item assignment
```

You can't change, add or remove items. If you need a changed version, build a new tuple.

> **Subtle point:** a tuple is only immutable on the surface. If it *contains* a list, that inner list can still change.
> ```python
> tt = (1, [2, 3])
> tt[1].append(4)
> print(tt)   # (1, [2, 3, 4])
> ```

### Unpacking

Split a tuple into separate variables in one line:

```python
x, y = (3, 4)
print(x, y)   # 3 4

# a neat trick: swap two variables without a temporary one
x, y = y, x
print(x, y)   # 4 3

# star (*) collects the leftovers
first, *rest = (1, 2, 3, 4)
print(first, rest)   # 1 [2, 3, 4]
```

### Tuple methods and functions

Because tuples can't change, they have only two methods, `count()` and `index()`. Both work like their list versions.

```python
fruits = ("apple", "banana", "apple", "orange")
print(fruits.count("apple"))   # 2     how many times it appears
print(fruits.index("apple"))   # 0     position of the FIRST match
print(fruits.index("orange"))  # 3
```

Like a list, `index()` raises a `ValueError` if the value isn't in the tuple.

The built-in functions all work on tuples too:

```python
numbers = (10, 20, 5, 30)
print(len(numbers))   # 4     how many items
print(sum(numbers))   # 65    add them up (items must be numbers)
print(min(numbers))   # 5     smallest
print(max(numbers))   # 30    largest
```

`sorted(numbers)` also works, but it returns a **list**, not a tuple:

```python
print(sorted(numbers))   # [5, 10, 20, 30]
```

### Converting between the two

```python
print(list((1, 2, 3)))    # [1, 2, 3]
print(tuple([1, 2, 3]))   # (1, 2, 3)
```

### Where tuples show up in real code

**Functions that return several values** actually return a tuple:

```python
def min_max(values):
    return min(values), max(values)

result = min_max([4, 1, 8])
print(result, type(result))   # (1, 8) <class 'tuple'>

low, high = min_max([4, 1, 8])
print(low, high)              # 1 8
```

**Dictionary keys**: tuples can be keys, lists cannot (keys must be unchangeable).

```python
places = {(40.7, -74.0): "New York"}
print(places[(40.7, -74.0)])   # New York
```

---

## 3. Which one should I use?

| Question | List | Tuple |
|---|---|---|
| Will the contents grow, shrink or change? | yes | no |
| Is it a fixed record (coordinates, an RGB color, a database row)? | | yes |
| Do I need it as a dictionary key? | | yes |
| Do I want protection from accidental changes? | | yes |

Rule of thumb: **start with a list. Switch to a tuple when the data is a fixed bundle that shouldn't change.**

---

## 4. Common mistakes (a quick checklist)

1. Expecting indexes to start at 1. They start at 0.
2. Forgetting that a slice stops **before** the end index.
3. Using `append` when you meant `extend`.
4. Writing `nums = nums.sort()` and ending up with `None`.
5. Thinking `b = a` makes a copy.
6. Writing `(5)` and expecting a tuple. You need `(5,)`.
7. Trying to change a tuple item.

---

## 5. Try it yourself

Attempt each one before opening the answer.

**1.** Given `nums = [10, 20, 30, 40, 50]`, print the middle three items.

<details>
<summary>Answer</summary>

```python
print(nums[1:4])   # [20, 30, 40]
```
</details>

**2.** Reverse `["a", "b", "c"]` without using `.reverse()`.

<details>
<summary>Answer</summary>

```python
print(["a", "b", "c"][::-1])   # ['c', 'b', 'a']
```
</details>

**3.** What does this print, and why?
```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

<details>
<summary>Answer</summary>

`[1, 2, 3]`. `b = a` doesn't copy the list. Both names point to the same list, so appending through `b` also changes what `a` sees.
</details>

**4.** Make a list of your five favourite foods, sort it alphabetically, and print the last one.

<details>
<summary>Answer</summary>

```python
foods = ["rice", "pasta", "falafel", "pizza", "soup"]
foods.sort()
print(foods[-1])   # soup
```
</details>

**5.** Write a function that takes a list of numbers and returns the smallest and largest as a tuple. Then unpack the result into two variables.

<details>
<summary>Answer</summary>

```python
def min_max(values):
    return min(values), max(values)

low, high = min_max([7, 3, 9])
print(low, high)   # 3 9
```
</details>

**6.** Why does this fail, and how would you fix it?
```python
point = (3, 4)
point[0] = 10
```

<details>
<summary>Answer</summary>

Tuples can't be changed, so this raises a `TypeError`. Make a new tuple instead: `point = (10, point[1])`. Or use a list if the value really needs to change.
</details>

**7.** For `t = (4, 8, 4, 1, 4)`, find how many times 4 appears, where the first 8 is, and the total of all items.

<details>
<summary>Answer</summary>

```python
t = (4, 8, 4, 1, 4)
print(t.count(4))   # 3
print(t.index(8))   # 1
print(sum(t))       # 21
```
</details>

---

## 6. Quick reference

| Task | List | Tuple |
|---|---|---|
| Add one item | `append(x)`, `insert(i, x)` | not possible |
| Add many items | `extend(iterable)` | not possible |
| Remove | `remove(x)`, `pop(i)`, `del lst[i]` | not possible |
| Change an item | `lst[i] = x` | not possible |
| Count / find | `count(x)`, `index(x)` | `count(x)`, `index(x)` |
| Sort | `sort()`, `sorted(lst)` | `sorted(t)` (returns a list) |
| Reverse | `reverse()`, `lst[::-1]` | `t[::-1]` |
| Copy | `copy()`, `lst[:]` | not needed (can't change) |
| Length, sum, min, max | `len(lst)`, `sum(lst)`, `min(lst)`, `max(lst)` | `len(t)`, `sum(t)`, `min(t)`, `max(t)` |

---

*Written by me while studying. Examples are my own.*
