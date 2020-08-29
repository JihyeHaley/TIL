#### Break

We often want to use a for loop to search through a list for some value:

```python
items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

# we want to check if the item with ID "knit_dress" is on sale:
for item in items_on_sale:
  if item == "knit_dress":
    print("Knit Dress is on sale!")
```

This code goes through each `item` in `items_on_sale` and checks for a match. After we find that `"knit_dress"` is in the list `items_on_sale`, we don’t need to go through the rest of the `items_on_sale` list. Since it’s only 5 elements long, iterating through the entire list is not a big deal in this case. But what if `items_on_sale` had 1000 items after `"knit_dress"`? What if it had 100,000 items after `"knit_dress"`?

You can stop a for loop from inside the loop by using `break`. When the program hits a `break` statement, control returns to the code outside of the for loop. For example:

```python
items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")
```

This would produce the output:

```python
Checking the sale list!
blue_shirt
striped_socks
knit_dress
End of search!
```

We didn’t need to check `"red_headband"` or `"dinosaur_onesie"` at all!



<hr>



#### Continue

When we’re iterating through lists, we may want to skip some values. Let’s say we want to print out all of the numbers in a list, unless they’re negative. We can use `continue` to move to the next `i` in the list:

```python
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
  if i < 0:
    continue
  print(i)
```

This would produce the output:

```py
1
2
4
5
2
```

Every time there was a negative number, the `continue` keyword moved the index to the next value in the list, without executing the code in the rest of the for loop.





```python
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in range(0, len(ages)):
  if ages[i] < 21:
    continue 
  print(ages[i])
```



<hr>



#### While Loops

We now have seen and used a lot of examples of for loops. There is another type of loop we can also use, called a *while loop*. The *while loop* performs a set of code until some condition is reached.

While loops can be used to iterate through lists, just like for loops:

```python
dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1
```

Every time the condition of the while loop (in this case, `index < len(dog_breeds)`) is satisfied, the code inside the while loop runs.

While loops can be useful when you don’t know how many iterations it will take to satisfy a condition.





<hr>



#### Nested Loops

We have seen how we can go through the elements of a list. What if we have a list made up of multiple lists? How can we loop through all of the individual elements?

Suppose we are in charge of a science class, that is split into three project teams:

```python
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
```

If we want to go through each student, we have to put one loop inside another:

```python
for team in project_teams:
  for student in team:
    print(student)
```

This results in:

```python
Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel
```





<hr>



#### List Comprehensions

Let’s say we have scraped a certain website and gotten these words:

```py
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
```

We want to make a new list, called `usernames`, that has all of the strings in `words` with an `'@'` as the first character. We know we can do this with a for loop:

```python
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)
```

First, we created a new empty list, `usernames`, and as we looped through the `words` list, we added every `word` that matched our criterion. Now, the `usernames` list looks like this:

```python
>>> print(usernames)
["@coolguy35", "@kewldawg54", "@matchamom"]
```

Python has a convenient shorthand to create lists like this with one line:

```python
usernames = [word for word in words if word[0] == '@']
```

This is called a *list comprehension*. It will produce the same output as the for loop did:

```python
["@coolguy35", "@kewldawg54", "@matchamom"]
```

This list comprehension:

1. Takes an element in `words`
2. Assigns that element to a variable called `word`
3. Checks if `word[0] == '@'`, and if so, it adds word to the new list, `usernames`. If not, nothing happens.
4. Repeats steps 1-3 for all of the strings in `words`

**Note:** if we hadn’t done any checking (let’s say we had omitted `if word[0] == '@'`), the new list would be just a copy of `words`:

```python
usernames = [word for word in words]
#usernames is now ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
```





<hr>



#### More List Comprehensions

Let’s say we’re working with the `usernames` list from the last exercise:

```python
>>> print(usernames)
["@coolguy35", "@kewldawg54", "@matchamom"]
```

We want to create a new list with the string `" please follow me!"` added to the end of each `username`. We want to call this new list `messages`. We can use a list comprehension to make this list with one line:

```python
messages = [user + " please follow me!" for user in usernames]
```

This list comprehension:

1. Takes a string in `usernames`
2. Assigns that string to a variable called `user`
3. Adds “ please follow me!” to `user`
4. Appends that concatenation to the new list called `messages`
5. Repeats steps 1-4 for all of the strings in `usernames`

Now, `messages` contains these values:

```python
["@coolguy35 please follow me!", "@kewldawg54 please follow me!", "@matchamom please follow me!"]
```

Being able to create lists with modified values is especially useful when working with numbers. Let’s say we have this list:

```python
my_upvotes = [192, 34, 22, 175, 75, 101, 97]
```

We want to add `100` to each value. We can accomplish this goal in one line:

```python
updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]
```

This list comprehension:

1. Takes a number in `my_upvotes`
2. Assigns that number to a variable called `vote_value`
3. Adds 100 to `vote_value`
4. Appends that sum to the new list `updated_upvotes`
5. Repeats steps 1-4 for all of the numbers in `my_upvotes`

Now, `updated_upvotes` contains these values:

```py
[292, 134, 122, 275, 175, 201, 197]
```





<hr>



#### Objective

```python
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1.
total_price = 0

# 2.
for p in prices:
  total_price += p

# 3.
print(f'Total Haircut Price: <{total_price}>')
average_price = total_price / len(prices)

# 4.
print(f'Average Haircut Price: <{average_price}>')

# 5.
new_prices = []

# 6.
for np in prices:
  new_prices.append(np - 5)
print(new_prices)

#7.
total_revenue = 0

# 8.
for i in range(0, len(hairstyles)):
  # 9.
  total_revenue += prices[i] + last_week[i]

# 10.
print(f'Total Revenue:: <{total_revenue}>')

# 11.
average_daily_revenue = total_revenue / 7

# 12.
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)
```





<hr>





#### Delete Starting Even Numbers

```
delete_starting_evens(lst)
```

###### Instructions

Write a function called `delete_starting_evens()` that has a parameter named `lst`.

The function should remove elements from the front of `lst` until the front of the list is not even. The function should then return `lst`.

For example if `lst` started as `[4, 8, 10, 11, 12, 15]`, then `delete_starting_evens(lst)` should return `[11, 12, 15]`.

Make sure your function works even if every element in the list is even!

```python
#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
```





<hr>





#### Odd Indices

```python
odd_indices(lst)
```



```python
#Write your function here
def odd_indices(lst):
  new_lst = []
  for i in range(1, len(lst), 2):
    new_lst.append(lst[i])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
```





<hr>

#### Exponents

```
exponents(bases, powers)
```



<hr>

#### Larger Sum

```python
larger_sum(lst1, lst2)
```



<hr>

#### Over 9000

```python
over_nine_thousand(lst)
```



```python
#Write your function here

def over_nine_thousand(lst):
  sum = 0
  for i in lst:
    sum += i
    if sum >= 9000:
      return sum
      break
  return sum
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))


```



<hr>



