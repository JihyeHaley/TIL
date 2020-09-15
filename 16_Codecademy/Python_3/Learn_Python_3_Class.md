### Types

Python equips us with many different ways to store data. A `float` is a different kind of number from an `int`, and we store different data in a `list` than we do in a `dict`. These are known as different *types*. We can check the type of a Python variable using the `type()` function.

```python
a_string = "Cool String"
an_int = 12

print(type(a_string))
# prints "<class 'str'>"

print(type(an_int))
# prints "<class 'int'>"
```

Above, we defined two variables, and checked the `type` of these two variables. A variable’s type determines what you can do with it and how you can use it. You can’t `.get()` something from an integer, just as you can’t add two dictionaries together using `+`. This is because those operations are defined at the `type` level.





### Class

A *class* is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data. Define a class using the `class` keyword. [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#class-names) recommends capitalizing the names of classes to make them easier to identify.

```python
class CoolClass:
  pass
```

In the above example we created a class and named it `CoolClass`. We used the `pass` keyword in Python to indicate that the body of the class was intentionally left blank so we don’t cause an `IndentationError`. We’ll learn about all the things we can put in the body of a class in the next few exercises.





### Instantiation

A class doesn’t accomplish anything simply by being defined. A class must be *instantiated*. In other words, we must create an *instance* of the class, in order to breathe life into the schematic.

Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined `CoolClass` as follows:

```python
cool_instance = CoolClass()
```

Above, we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable `cool_instance` for safe-keeping so we can access our instance of `CoolClass` at a later time.

```python
class Facade:
  pass

facade_1 = Facade()
```





### Object-Oriented Programming

A class instance is also called an *object*. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as *Object Oriented Programming* or OOP.

Instantiation takes a class and turns it into an object, the `type()` function does the opposite of that. When called with an object, it returns the class that the object is an instance of.

```py
print(type(cool_instance))
# prints "<class '__main__.CoolClass'>"
```

We then print out the `type() of cool_instance` and it shows us that this object is of type `__main__.CoolClass`.

In Python `__main__` means “this current file that we’re running” and so one could read the output from `type()` to mean “the class `CoolClass` that was defined here, in the script you’re currently running.”

```python
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)
```





### Class Variables

When we want the same data to be available to every instance of a class we use a *class variable*. A class variable is a variable that’s the same for every instance of the class.

You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with `object.variable` syntax.

```python
class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints "Rockstar"
```

Above we defined the class `Musician`, then instantiated `drummer` to be an object of type `Musician`. We then printed out the drummer’s `.title` attribute, which is a class variable that we defined as the string “Rockstar”.

If we defined another musician, like `guitarist = Musician()` they would have the same `.title` attribute.

```python
class Grade:
  minimum_passing = 65
```





### Methods

*Methods* are functions that are defined as part of a class. The first argument in a method is always the object that is calling the method. Convention recommends that we name this first argument `self`. Methods always have at least this one argument.

We define methods similarly to functions, except that they are indented to be part of the class.

```python
class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."
```

Above we created a `Dog` class with a `time_explanation` method that takes one argument, `self`, which refers to the object calling the function. We created a `Dog` named `pipi_pitbull` and called the `.time_explanation()` method on our new object for Pipi.

Notice we didn’t pass any arguments when we called `.time_explanation()`, but were able to refer to `self` in the function body. When you call a method it automatically passes the object calling the method as the first argument.



```python
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."
```





### Methods with Arguments

Methods can also take more arguments than just `self`:

```python
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"
```

Above we defined a `DistanceConverter` class, instantiated it, and used it to convert 5 miles into kilometers. Notice again that even though `how_many_kms` takes two arguments in its definition, we only pass `miles`, because `self` is implicitly passed (and refers to the object `converter`).



```python
class Circle:
  pi = 3.14
  def area(self, radius):
    area = self.pi * radius ** 2 
    return area

circle = Circle()
pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)
```





### Constructors

There are several methods that we can define in a Python class that have special behavior. These methods are sometimes called “magic”, because they behave differently from regular methods. Another popular term is *dunder methods*, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

The first dunder method we’re going to use is the `__init__` method (note the two underscores before and after the word “init”). This method is used to *initialize* a newly created object. It is called every time the class is instantiated.

Methods that are used to prepare an object being instantiated are called *constructors*. The word “constructor” is used to describe similar features in other object-oriented programming languages but programmers who refer to a constructor in Python are usually talking about the `__init__` method.

```python
class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"
```

Above we created a class called `Shouter` and every time we create an instance of `Shouter` the program prints out a shout. Don’t worry, this doesn’t hurt the computer at all.

Pay careful attention to the instantiation syntax we use. `Shouter()` looks a lot like a function call, doesn’t it? If it’s a function, can we pass parameters to it? We absolutely can, and those parameters will be received by the `__init__` method.

```python
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"
```

Above we’ve updated our `Shouter` class to take the additional parameter `phrase`. When we created each of our objects we passed an argument to the constructor. The constructor takes the argument `phrase` and, if it’s a string, prints out the all-caps version of `phrase`.



```python
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print(f'New circle with diameter: {diameter}')

teaching_table = Circle(36)
```





### Instance Variables

We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has? This is because each instance of a class can hold different kinds of data.

The data held by an object is referred to as an *instance variable*. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

Let’s say that we have the following class definition:

```python
class FakeDict:
  pass
```

We can instantiate two different objects from this class, `fake_dict1` and `fake_dict2`, and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.

```python
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"
```



```python
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = 'Alternative Rocks'
isabelles_ices.store_name = 'Isabelle\'s Ices'

```







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

```

