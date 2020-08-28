#### Boolean Expressions

In order to build control flow into our program, we want to be able to check if something is true or not. A boolean expression is a statement that can either be `True` or `False`.

Let’s go back to the ‘waking up’ example. The first question, “Is today a weekday?” can be written as a boolean expression:

```
Today is a weekday.
```

This expression can be `True` if today is Tuesday, or it can be `False` if today is Saturday. There are no other options.

Consider the phrase:

```
Friday is the best day of the week.
```

Is this a boolean expression?

No, this statement is an opinion and is not objectively `True` or `False`. Someone else might say that “Wednesday is the best weekday,” and their statement would be no less `True` or `False` than the one above.

How about the phrase:

```
Sunday starts with the letter 'C'.
```

Is this a boolean expression?

Yes! This expression can only be `True` or `False`, which makes it a boolean expression. Even though the statement itself is false (Sunday starts with the letter ‘C’), it is still a boolean expression.



### Instructions

**1.**

Determine if the following statements are boolean expressions or not. If they are, set the matching variable to the right to `"Yes"` and if not set the variable to `"No"`. Here’s an example of what to do:

Example statement:

```
My dog is the cutest dog in the world.
```

This is an opinion and not a boolean expression, so you would set `example_statement` to `"No"` in the editor to the right. Okay, now it’s your turn:

Statement one:

```
Dogs are mammals.
```

Statement two:

```
My dog is named Pavel.
```

Statement three:

```
Dogs make the best pets.
```

Statement four:

```
Cats are femal
```





<hr>

#### Relational Operators: Equals and Not Equals

Now that we understand what boolean expressions are, let’s learn to create them in Python. We can create a boolean expression by using *relational operators*.

Relational operators compare two items and return either `True` or `False`. For this reason, you will sometimes hear them called *comparators*.

The two boolean operators we’ll cover first are:

- Equals: `==`
- Not equals: `!=`

These operators compare two items and return `True` or `False` if they are equal or not.

We can create boolean expressions by comparing two values using these operators:

```py
>>> 1 == 1
True
>>> 2 != 4
True
>>> 3 == 5
False
>>> '7' == 7
False
```

Each of these is an example of a boolean expression. `>>>` is the prompt when you run Python in your terminal, which you can then use to evaluate simple expressions, such as these.

Why is the last statement false? The `''` marks in `'7'` make it a string, which is different from the integer value `7`, so they are not equal. When using relational operators it is important to always be mindful of type.



<hr>

#### Boolean Variables

Before we go any further, let’s talk a little bit about `True` and `False`. You may notice that when you type them in the code editor (with uppercase T and F), they appear in a different color than variables or strings. This is because `True` and `False` are their own special type: `bool`.

`True` and `False` are the only `bool` types, and any variable that is assigned one of these values is called a *boolean variable*. Boolean variables can be created in several ways. The easiest way is to simply assign `True` or `False` to a variable:

```python
set_to_true = True
set_to_false = False
```

You can also set a variable equal to a boolean expression.

```python
bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
```

These variables now contain boolean values, so when you reference them they will only return the `True` or `False` values of the expression they were assigned.

```python
>>>bool_three
True
>>>bool_four
False
>>>bool_five
True
```





<hr>



#### If Statements

“Okay okay okay, boolean variables, boolean expressions, blah blah *blah*, I thought I was learning how to build control flow into my code!”

You are, I promise you!

Understanding boolean variables and expressions is essential because they are the building blocks of *conditional statements*.

Recall the waking-up example from the beginning of this lesson. The decision-making process of “Is it raining? If so, bring an umbrella” is a conditional statement. Here it is phrased in a different way:

```
If it is raining then bring an umbrella.
```

Can you pick out the boolean expression here?

Right, `"it is raining"` is the boolean expression, and this conditional statement is checking to see if it is True.

If `"it is raining" == True` then the rest of the conditional statement will be executed and you will bring an umbrella.

This is the form of a conditional statement:

```python
If [it is raining] then [bring an umbrella]
```

In Python, it looks very similar:

```python
if is_raining:
  bring_umbrella()
```

You’ll notice that instead of “then” we have a colon, `:`. That tells the computer that what’s coming next is what should be executed if the condition is met. Let’s take a look at another conditional statement:

```python
if 2 == 4 - 2: 
  print("apple")
```

Will this code print `apple` to the terminal? Yes, because the condition of the `if` statement, `2 == 4 - 2` is `True`.

Let’s work through a couple more together:





<hr>

#### Relational Operators II

Now that we’ve added conditional statements to our toolkit for building control flow, let’s explore more ways to create boolean expressions. So far we know two relational operators, equals and not equals, but there are a ton (well, four) more:

- Greater than: `>`
- Less than: `<`
- Greater than or equal to: `>=`
- Less than or equal to: `<=`

Let’s say we’re running a movie streaming platform and we want to write a function that checks if our users are over 13 when showing them a PG-13 movie. We could write something like:

```python
def age_check(age):
  if age >= 13:
    return True
```

This function will take the users age and compare it to the number 13. If `age` is greater than or equal to 13 it will return `True`.

Let’s try some more!





<hr>

#### Boolean Operators: and

Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. In these cases, you can build larger boolean expressions using *boolean operators*. These operators (also known as *logical operators*) combine smaller boolean expressions into larger boolean expressions.

There are three boolean operators that we will cover:

- `and`
- `or`
- `not`

Let’s start with `and`.

`and` combines two boolean expressions and evaluates as `True` if both its components are `True`, but `False` otherwise.

Consider the example

```
Oranges are a fruit and carrots are a vegetable.
```

This boolean expression is comprised of two smaller expressions, `oranges are a fruit` and `carrots are a vegetable`, both of which are `True` and connected by the boolean operator `and`, so the entire expression is `True`.

Let’s look at an example of some AND statements in Python:

```python
>>> (1 + 1 == 2) and (2 + 2 == 4)
True
>>> (1 + 1 == 2) and (2 < 1)
False
>>> (1 > 9) and (5 != 6)
False
>>> (0 == 10) and (1 + 1 == 1) 
False
```

Notice that in the second and third examples, even though part of the expression is `True`, the entire expression as a whole is `False` because the other statement is False. The fourth statement is also `False` because both components are `False`.



<hr>

#### Boolean Operators: or

The boolean operator `or` combines two expressions into a larger expression that is `True` if either component is `True`.

Consider the statement

```
Oranges are a fruit or apples are a vegetable.
```

This statement is composed of two expressions: `oranges are a fruit` which is `True` and `apples are a vegetable` which is `False`. Because the two expressions are connected by the `or` operator, the entire statement is `True`. Only one component needs to be `True` for an `or` statement to be `True`.

In English, `or` implies that if one component is `True`, then the other component must be `False`. This is not true in Python. If an `or` statement has two `True` components, it is also `True`.

Let’s take a look at a couple example in Python:

```python
>>> True or (3 + 4 == 7)
True
>>> (1 - 1 == 0) or False
True
>>> (2 < 0) or True
True
>>> (3 == 8) or (3 > 4) 
False
```

Notice that each `or` statement that has at least one `True` component is `True`, but the final statement has two `False` components, so it is `False`.



<hr>

#### Boolean Operators: not

The final boolean operator we will cover is `not`. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a `True` statement and apply a `not` operator we get a `False` statement.

```python
not True == False
not False == True
```

Consider the following statement:

```
Oranges are not a fruit.
```

Here, we took the `True` statement `oranges are a fruit` and added a `not` operator to make the `False` statement `oranges are not a fruit`.

This example in English is slightly different from the way it would appear in Python because in Python we add the `not` operator to the very beginning of the statement. Let’s take a look at some of those:

```python
>>> not 1 + 1 == 2
False
>>> not 7 < 0
True
```





<hr>

#### Else Statements

As you can tell from your work with *Calvin Coolidge’s Cool College*, once you start including lots of `if` statements in a function the code becomes a little cluttered and clunky. Luckily, there are other tools we can use to build control flow.

`else` statements allow us to elegantly describe what we want our code to do when certain conditions are **not** met.

`else` statements always appear in conjunction with `if` statements. Consider our waking-up example to see how this works:

```python
if weekday:
  wake_up("6:30")
else:
  sleep_in()
```

In this way, we can build if statements that execute different code if conditions are or are not met. This prevents us from needing to write `if` statements for each possible condition, we can instead write a blanket `else` statement for all the times the condition is not met.

Let’s return to our `age_check` function for our movie streaming platform. Previously, all it did was check if the user’s age was over `13` and if so return `True`. We can use an `else` statement to return a message in the event the user is too young to watch the movie.

```python
def age_check(age):
  if age >= 13:
    return True
  else:
    return "Sorry, you must be 13 or older to watch this 
```



<hr>