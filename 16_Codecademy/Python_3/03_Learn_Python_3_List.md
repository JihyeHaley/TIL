#### Range I

Often, we want to create a list of consecutive numbers. For example, suppose we want a list containing the numbers 0 through 9:

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Typing out all of those numbers takes time and the more numbers we type, the more likely it is that we have a typo.

Python gives us an easy way of creating these lists using a function called range. The function range takes a single input, and generates numbers starting at 0 and ending at the number before the input. So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

my_range = range(10)
Just like with zip, the range function returns an object that we can convert into a list:

```python
print(my_range)
range(0, 10)
print(list(my_range))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



<hr>
#### Length of a List

Often, we’ll need to find the number of items in a list, usually called its *length*.

We can do this using the function `len`. When we apply `len` to a list, we get the number of elements in that list:

```py
my_list = [1, 2, 3, 4, 5]
print(len(my_list))
```

This would yield:

```
5
```



<hr>



#### Selecting List Elements II

What if we want to select the last element of a list?

We can use the index `-1` to select the last item of a list, even when we don’t know how many elements are in a list.

Consider the following list with 5 elements:

```python
list1 = ['a', 'b', 'c', 'd', 'e']
```

If we select the `-1` element, we get the final element, `'e'`:

```python
>>> print(list1[-1])
'e'
```

This is the same as selecting the element with index `4`:

```python
>>> print(list1[4])
'e'
```





<hr>



#### Slicing Lists

Suppose we have a list of letters:

```py
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

Suppose we want to select from `b` through `f`.

We can do this using the following syntax: `letters[start:end]`, where:

- `start` is the index of the first element that we want to include in our selection. In this case, we want to start at `b`, which has index `1`.

- ```
  end
  ```

   

  is the index of

   

  one more than

   

  the last index that we want to include. The last element we want is

   

  ```
  f
  ```

  , which has index

   

  ```
  5
  ```

  , so

   

  ```
  end
  ```

   

  needs to be

   

  ```
  6
  ```

  .

  ```python
  sublist = letters[1:6]
  print(sublist)
  ```

  This example would yield:

  ```python
  ['b', 'c', 'd', 'e', 'f']
  ```

  Notice that the element at index

   

  ```
  6
  ```

   

  (which is

   

  ```
  g
  ```

  ) is

   

  not

   

  included in our selection.

Creating a selection from a list is called *slicing*.



<hr>





#### Slicing Lists II

If we want to select the first 3 elements of a list, we could use the following code:

```python
>>> fruits = ['apple', 'banana', 'cherry', 'date']
>>> print(fruits[0:3])
['apple', 'banana', 'cherry']
```

When starting at the beginning of the list, it is also valid to omit the `0`:

```python
>>> print(fruits[:3])
['apple', 'banana', 'cherry']
```

We can do something similar when selecting the last few items of a list:

```python
>>> print(fruits[2:])
['cherry' , 'date']
```

We can omit the final index when selecting the final elements from a list.

If we want to select the last 3 elements of `fruits`, we can also use this syntax:

```python
>>> print(fruits[-3:])
['banana', 'cherry', 'date']
```

We can use *negative* indexes to count backward from the last element.



```python
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

start = suitcase[0:3]

end = suitcase[-2:]
```



<hr>

#### Counting elements in a list

Suppose we have a list called `letters` that represents the letters in the word “Mississippi”:

```python
letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
```

If we want to know how many times `i` appears in this word, we can use the function `count`:

```python
num_i = letters.count('i')
print(num_i)
```

This would print out:

```python
4
```





<hr>

#### Sorting Lists I

Sometimes, we want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

We can sort a list *in place* using `.sort()`. Suppose that we have a list of names:

```py
names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
print(names)
```

This would print:

```python
['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
```

Now we apply `.sort()`:

```python
names.sort()
print(names)
```

And we get:

```python
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

Notice that `sort` goes *after* our list, `names`. If we try `sort(names)`, we will get a `NameError`.

`sort` does not return anything. So, if we try to assign `names.sort()` to a variable, our new variable would be `None`:

```python
sorted_names = names.sort()
print(sorted_names)
```

This prints:

```
None
```

Although `sorted_names` is `None`, the line `sorted_names = names.sort()` still edited `names`:

```python
>>> print(names)
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```





<hr>

#### Sorting Lists II

A second way of sorting a list is to use `sorted`. `sorted` is different from `.sort()` in several ways:

1. It comes *before* a list, instead of after.
2. It generates a new list.

Let’s return to our list of names:

```python
names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
```

Using `sorted`, we can create a new list, called `sorted_names`:

```python
sorted_names = sorted(names)
print(sorted_names)
```

This yields the list sorted alphabetically:

```python
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

Note that using `sorted` did not change `names`:

```python
>>> print(names)
['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
```





<hr>





