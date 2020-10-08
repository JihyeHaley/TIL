### Dunder Methods II

Python offers a whole suite of magic methods a class can implement that will allow us to use the same syntax as Python’s built-in data types. You can write functionality that allows custom defined types to behave like lists:

```py
class UserGroup:
  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions

  def __iter__(self):
    return iter(self.user_list)

  def __len__(self):
    return len(self.user_list)

  def __contains__(self, user):
    return user in self.user_list
```

In our `UserGroup` class above we defined three methods:

- `__init__`, our constructor, which sets a list of users to the instance variable `self.user_list` and sets the group’s `permissions` when we create a new `UserGroup`.
- `__iter__`, the iterator, we use the `iter()` function to turn the list `self.user_list` into an *iterator* so we can use `for user in user_group` syntax. For more information on iterators, review [Python’s documentation of Iterator Types](https://docs.python.org/3/library/stdtypes.html#typeiter).
- `__len__`, the length method, so when we call `len(user_group)` it will return the length of the underlying `self.user_list` list.
- `__contains__`, the check for containment, allows us to use `user in user_group` syntax to check if a `User` exists in the `user_list` we have.

These methods allow `UserGroup` to act like a list using syntax Python programmers will already be familiar with. If all you need is something to act like a list you could absolutely have used a list, but if you want to bundle some other information (like a group’s permissions, for instance) having syntax that allows for list-like operations can be very powerful.

We would be able to use the following code to do this, for example:

```py
class User:
  def __init__(self, username):
    self.username = username

diana = User('diana')
frank = User('frank')
jenn = User('jenn')

can_edit = UserGroup([diana, frank], {'can_edit_page': True})
can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})

print(len(can_edit))
# Prints 2

for user in can_edit:
  print(user.username)
# Prints "diana" and "frank"

if frank in can_delete:
  print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")
```

Above we created a set of users and then added them to `UserGroup`s with specific permissions. Then we used Python built-in functions and syntax to calculate the length of a `UserGroup`, to iterate through a `UserGroup` and to check for a `User`‘s membership in a `UserGroup`.



```python
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  
  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, laywer):
    return laywer in self.lawyers


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
```



<hr>



**1.**

Create a class `SortedList` that inherits from the built-in type `list`.

Checkpoint 2 Passed



**2.**

Recall that lists have a `.append()` method that takes a two arguments, `self` and `value`. We’re going to have `SortedList` perform a sort after every `.append()`.

Overwrite the `append` method, leave it blank for now with the `pass` keyword.

Checkpoint 3 Passed



**3.**

First, we want our new `.append()` to actually add the item to the list.

Write the code that would get `SortedList` to behave like a normal `list` when calling the `.append()` method.



**4.**

After you’ve appended the new value, sort the list.



```python
class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()
```

