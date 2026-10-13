# Lists and tuples

These are the two most common ways to hold a sequence of items in Python. Almost every data task starts with one of them: a column of numbers, a row of a table, a batch of file names.

The one-sentence difference: **a list can be changed after you create it; a tuple cannot.**

Think of a list as a shopping list written in pencil (you can add, cross out, and reorder), and a tuple as a printed ticket (what is written stays written).

> Every code block below is runnable. Copy it into a Python shell, a Jupyter notebook, or [Google Colab](https://colab.research.google.com) and change things to see what happens. Lines starting with `#` show the output.

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

### Useful built-in functions

```python
print(len(fruits))            # 4
print(max([3, 7, 2]))         # 7
print(sum([3, 7, 2]))         # 12
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

You can sort by a rule with `key`:

```python
words = ["pear", "fig", "banana"]
print(sorted(words, key=len))   # ['fig', 'pear', 'banana']   (shortest first)
```

> **Common mistake:** `nums = nums.sort()` sets `nums` to `None`, because `sort()` changes the list in place and returns nothing. Write `nums.sort()` on its own line, or use `sorted()`.

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

---

*Written by me while studying. Examples are my own.*
