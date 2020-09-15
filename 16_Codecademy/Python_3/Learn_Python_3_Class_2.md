### Attribute Functions

Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both considered *attributes* of an object. If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an `AttributeError`.

```python
class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"
```

What if we aren’t sure if an object has an attribute or not? `hasattr()` will return `True` if an object has a given attribute and `False` otherwise. If we want to get the actual value of the attribute, `getattr()` is a Python function that will return the value of a given object and attribute. In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.

The syntax and parameters for these functions look like this:

`hasattr(object, “attribute”)` has two parameters:

- *object* : the object we are testing to see if it has a certain attribute
- *attribute* : name of attribute we want to see if it exists

`getattr(object, “attribute”, default)` has three parameters (one of which is optional):

- *object* : the object whose attribute we want to evaluate
- *attribute* : name of attribute we want to evaluate
- *default* : the value that is returned if the attribute does not exist (note: this parameter is **optional**)

Calling those functions looks like this:

```python
hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value
```

Above we checked if the `attributeless` object has the attribute `fake_attribute`. Since it does not, `hasattr()` returned `False`. After that, we used `getattr` to attempt to retrieve `other_fake_attribute`. Since `other_fake_attribute` isn’t a real attribute on `attributeless`, our call to `getattr()` returned the supplied default value `800`, instead of throwing an `AttributeError`.



```python
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")
```

```
<class 'dict'> does not have the count attribute :(
<class 'str'> has the count attribute!
<class 'int'> does not have the count attribute :(
<class 'list'> has the count attribute!
```

* **This is because dictionaries and integers both do not have a `count` attribute,** while ***strings and lists do***. 

  In this exercise, we have iterated through `can_we_count_it` and used `hasattr()` to determine which elements have a `count` attribute. We never actually used the count method, but you can read more about it [here](https://www.w3schools.com/python/ref_list_count.asp) if you are curious about what it is.

  * `type(dict)`, `type(int)` <u>*do not have*</u> **'count' attribute**
  * `type(str)`, `type(list)` *<u>do have</u>* **'count' attribute**





### Self

Since we can already use dictionaries to store key-value pairs, using objects for that purpose is not really useful. Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.

This convenience is most apparent when the constructor creates the instance variables, using the arguments passed in to it. If we were creating a search engine, and we wanted to create classes for each separate entry we could return. We’d do that like this:

```python
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"
```

Since the `self` keyword refers to the object and not the class being called, we can define a `secure` method on the `SearchEngineEntry` class that returns the secure link to an entry.

```python
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"
```

Above we define our `secure()` method to take just the one required argument, `self`. We access both the class variable `self.secure_prefix` and the instance variable `self.url` to return a secure URL.

This is the strength of writing object-oriented programs. We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.



```python
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print(f"Creating circle with diameter {diameter}")
    # Add assignment for self.radius here:
    self.radius = diameter / 2
  

  def circumference(self):
    circumference = 2 * self.pi * self.radius
    return circumference


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference(), teaching_table.circumference(), round_room.circumference())
```





### Everything is an Object

Attributes can be added to user-defined objects after instantiation, so it’s possible for an object to have some attributes that are not explicitly defined in an object’s constructor. We can use the `dir()` function to investigate an object’s attributes at runtime. `dir()` is short for *directory* and offers an organized presentation of object attributes.

```python
class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

dir(fake_dict)
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']
```

That’s certainly a lot more attributes than we defined! Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually indicated by double-underscores. But sure enough, `attribute` is in that list.

Do you remember being able to use `type()` on Python’s native data types? This is because they are also objects in Python. Their classes are `int`, `float`, `str`, `list`, and `dict`. These Python classes have special syntax for their instantiation, `1`, `1.0`, `"hello"`, `[]`, and `{}` specifically. But these instances are still full-blown objects to Python.

```python
fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

dir(fun_list)
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

Above we define a new list. We check it’s type and see that’s an instantiation of class `list`. We use `dir()` to explore its attributes, and it gives us a large number of internal Python dunder attributes, but, afterward, we get the usual list methods.

```python
print(dir(5))

def this_function_is_an_object(hello):
  return hello

print(dir(this_function_is_an_object))
```



```python
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2


  def area(self):
    return self.pi * self.radius ** 2
  

  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return f'Circle with radius {self.radius}'
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)
```



```python
# 1
class Student:
  # 2
  def __init__(self, name, year):
    self.name = name
    self.year = year
    # 6
    self.grades = []
  

  def add_grade(self, grade):
    self.grade = grade
    if type(grade) == Grade:
      self.grades.append(grade) 
      
  def get_average(self):
    


# 3
roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

# 4
class Grade:
  minimum_passing = 65
  # 5
  def __init__(self, score):
    self.score = score
    
 	def is_passing(self):
    return f'Grade {self.score}'
  
  
```

