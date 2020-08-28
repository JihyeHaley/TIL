* #### What is a Function?

  Let’s imagine that we are creating a program that greets customers as they enter a grocery store. We want a big screen at the entrance of the store to say:

  ```
  Welcome to Engrossing Grocers.
  Our special is mandarin oranges.
  Have fun shopping!
  ```

  We have learned to use print statements for this purpose:

  ```python
  print("Welcome to Engrossing Grocers.")
  print("Our special is mandarin oranges.")
  print("Have fun shopping!")
  ```

  Every time a customer enters, we call these three lines of code. Even if only 3 or 4 customers come in, that’s a lot of lines of code required.

  In Python, we can make this process easier by assigning these lines of code to a *function*. We’ll name this function `greet_customer`. In order to call a function, we use the syntax `function_name()`. The parentheses are important! They make the code inside the function run. In this example, the function call looks like:

  ```python
  greet_customer()
  ```

  Every time we call `greet_customer()`, we would see:

  ```python
  Welcome to Engrossing Grocer's.
  Our special is mandarin oranges.
  Have fun shopping!
  ```

  Having this functionality inside `greet_customer()` is better form, because we have isolated this behavior from the rest of our code. Once we determine that `greet_customer()` works the way we want, we can reuse it anywhere and be confident that it greets, without having to look at the implementation. We can get the same output, with less repeated code. Repeated code is generally more error prone and harder to understand, so it’s a good goal to reduce the amount of it.





<hr>

#### Write a Function

We have seen the value of simple functions for modularizing code. Now we need to understand how to write a function. To write a function, you must have a heading and an indented block of code. The heading starts with the keyword `def` and the name of the function, followed by parentheses, and a colon. The indented block of code performs some sort of operation. This syntax looks like:

```python
def function_name():
  some code
```

For our `greet_customer()` example, the function definition looks like:

```python
def greet_customer():
  print("Welcome to Engrossing Grocers.")
  print("Our special is mandarin oranges.")
  print("Have fun shopping!")

greet_customer()
# prints greeting lines
```

The keyword `def` tells Python that we are defining a function. This function is called `greet_customer`. Everything that is indented after the `:` is what is run when `greet_customer()` is called. So every time we call `greet_customer()`, the three `print` statements run.





<hr>



#### Whitespace

Consider this function:

```python
def greet_customer():
  print("Welcome to Engrossing Grocers.")
  print("Our special is mandarin oranges.")
  print("Have fun shopping!")
```

The three `print` statements are all executed together when `greet_customer()` is called. This is because they have the same level of indentation. In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function. If we wanted to write another line outside of `greet_customer()`, we would have to unindent the new line:

```python
def greet_customer():
  print("Welcome to Engrossing Grocers.")
  print("Our special is mandarin oranges.")
  print("Have fun shopping!")
print("Cleanup on Aisle 6")
greet_customer()
greet_customer()
```

When we run this program, the message `"Cleanup on Aisle 6"` will be printed once, while the messages in `greet_customer()` will all be printed twice. This is because we call the function twice, and `"Cleanup on Aisle 6"` is not part of the function. Notice also that `"Cleanup on Aisle 6"` will be printed before the `greet_customer()` messages since we call the function after it. We would see the following output from this program:

```
Cleanup on Aisle 6
Welcome to Engrossing Grocers.
Our special is mandarin oranges.
Have fun shopping!
Welcome to Engrossing Grocers.
Our special is mandarin oranges.
Have fun shopping!
```

Here at Codecademy, we use 2 spaces for our default indentation. Anything other than that will throw an error when you try to run the program. Many other platforms use 4 spaces. Some people even use tabs! These are all fine. What is important is being consistent throughout the project.

```python
def about_this_computer():
  print("This computer is running on version Everest Puma")
print("This is your desktop")

about_this_computer()
```



* it returns 

  ```python
  This is your desktop
  This computer is running on version Everest Puma
  ```



Here at Codecademy, we use 2 spaces for our default indentation. Anything other than that will throw an error when you try to run the program. Many other platforms use 4 spaces. Some people even use tabs! These are all fine. What is important is being consistent throughout the project.



<hr>





#### Parameters

Let’s return to Engrossing Grocers. The special of the day will not always be mandarin oranges, it will change every day. What if we wanted to call these three print statements again, except with a variable special? We can use *parameters*, which are variables that you can pass into the function when you call it.

```python
def greet_customer(special_item):
  print("Welcome to Engrossing Grocers.")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")
```

In the definition heading for `greet_customer()`, the `special_item` is referred to as a *formal parameter*. This variable name is a placeholder for the name of the item that is the grocery’s special today. Now, when we call `greet_customer`, we have to provide a `special_item`:

```python
greet_customer("peanut butter")
```

That item will get printed out in the second print statement:

```python
Welcome to Engrossing Grocers.
Our special is peanut butter.
Have fun shopping!
```

The value between the parentheses when we call the function (in this case, `"peanut butter"`) is referred to as an argument of the function call. The argument is the information that is to be used in the execution of the function. When we then call the function, Python assigns the formal parameter name `special_item` with the actual parameter data, `"peanut_butter"`. In other words, it is as if this line was included at the top of the function:

```python
special_item = "peanut butter"
```

Every time we call `greet_customer()` with a different value between the parentheses, `special_item` is assigned to hold that value.





<hr>





#### Multiple Parameters

Our grocery greeting system has gotten popular, and now other supermarkets want to use it. As such, we want to be able to modify both the special item and the name of the grocery store in a greeting like this:

```python
Welcome to [grocery store].
Our special is [special item].
Have fun shopping!
```

We can make a function take more than one parameter by using commas:

```python
def greet_customer(grocery_store, special_item):
  print("Welcome to "+ grocery_store + ".")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")
```

The variables `grocery_store` and `special_item` must now both be provided to the function upon calling it:

```python
greet_customer("Stu's Staples", "papayas")
```

which will print:

```python
Welcome to Stu's Staples.
Our special is papayas.
Have fun shopping!
```





<hr>



#### Keyword Arguments

In our `greet_customer()` function from the last exercise, we had two arguments:

```python
def greet_customer(grocery_store, special_item):
  print("Welcome to "+ grocery_store + ".")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")
```

Whichever value is put into `greet_customer()` first is assigned to `grocery_store`, and whichever value is put in second is assigned to `special_item`. These are called *positional arguments* because their assignments depend on their positions in the function call.

We can also pass these arguments as *keyword arguments*, where we explicitly refer to what each argument is assigned to in the function call.

```python
greet_customer(special_item="chips and salsa", grocery_store="Stu's Staples")
Welcome to Stu's Staples.
Our special is chips and salsa.
Have fun shopping!
```

We can use keyword arguments to make it explicit what each of our arguments to a function should refer to in the body of the function itself.

We can also define default arguments for a function using syntax very similar to our keyword-argument syntax, but used during the function definition. If the function is called without an argument for that parameter, it relies on the default.

```python
def greet_customer(special_item, grocery_store="Engrossing Grocers"):
  print("Welcome to "+ grocery_store + ".")
  print("Our special is " + special_item + ".")
  print("Have fun shopping!")
```

In this case, `grocery_store` has a default value of `"Engrossing Grocers"`. If we call the function with only one argument, the value of `"Engrossing Grocers"` is used for `grocery_store`:

```python
greet_customer("bananas")
Welcome to Engrossing Grocers.
Our special is bananas.
Have fun shopping!
```

Once you give an argument a default value (making it a keyword argument), no arguments that follow can be used positionally. For example:

```python
def greet_customer(special_item="bananas", grocery_store): # this is not valid
  ...

def greet_customer(special_item, grocery_store="Engrossing Grocers"): # this is valid
  ...
```







<hr>

#### Returns

So far, we have only seen functions that print out some result to the console. Functions can also return a value to the user so that this value can be modified or used later. When there is a result from a function that can be stored in a variable, it is called a *returned* function value. We use the keyword `return` to do this.

Here’s an example of a function `divide_by_four` that takes an integer argument, divides it by four, and `return`s the result:

```python
def divide_by_four(input_number):
  return input_number/4
```

The program that calls `divide_by_four` can then use the result later:

```python
result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")
```

This would print out:

```
16 divided by 4 is 4!
4 divided by 4 is 1!
```

In this example, we returned a number, but we could also return a String:

```python
def create_special_string(special_item):
  return "Our special is " + special_item + "."

special_string = create_special_string("banana yogurt")

print(special_string)
Our special is banana yogurt.
```





<hr>

#### Multiple Return Values

Sometimes we may want to return more than one value from a function. We can return several values by separating them with a comma:

```python
def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2
```

This function takes in an x value and a y value, and returns them both, squared. We can get those values by assigning them both to variables when we call the function:

```python
x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)
```

This will print:

```
1
9
```





<hr>



#### Scope

Let’s say we have our function from the last exercise that creates a string about a special item:

```python
def create_special_string(special_item):
  return "Our special is " + special_item + "."
```

What if we wanted to access the variable `special_item` outside of the function? Could we use it?

```python
def create_special_string(special_item):
  return "Our special is " + special_item + "."

print("I don't like " + special_item)
```

If we try to run this code, we will get a NameError, telling us that `'special_item' is not defined`. The variable `special_item` has only been defined inside the space of a function, so it does not exist outside the function. We call the part of a program where `special_item` can be accessed its *scope*. The *scope* of `special_item` is only the `create_special_string` function.

Variables defined outside the scope of a function may be accessible inside the body of the function:

```python
header_string = "Our special is " 

def create_special_string(special_item):
  return header_string + special_item + "."
print(create_special_string("grapes"))
```

There is no error here. `header_string` can be used inside the `create_special_string` function because the scope of `header_string` is the whole file. This file would produce:

```python
Our special is grapes.
```



<hr>

#### Review

Great! So far you have learned:

- How to write a function
- How to give a function inputs
- How to return values from a function
- What scope means

Let’s practice these concepts again so that you won’t forget them!

