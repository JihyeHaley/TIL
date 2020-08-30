#### Negative Indices

In the previous exercise, we used `len()` to get a slice of characters at the end of a string.

There’s a much easier way to do this, we can use negative indices! Negative indices count backward from the end of the string, so `string_name[-1]` is the last character of the string, `string_name[-2]` is the second last character of the string, etc.

Here are some examples:

```python
>>> favorite_fruit = 'blueberry`
>>> favorite_fruit[-1]
'y'
>>> favorite_fruit[-2]
'r'
>>> favorite_fruit[-3:]
'rry'
```

Notice that we are able to slice the last three characters of ‘blueberry’ by having a starting index of `-3` and omitting a final index.





<hr>

#### Strings are Immutable

So far in this lesson, we’ve been selecting characters from strings, slicing strings, and concatenating strings. Each time we perform one of these operations we are creating an entirely new string.

This is because strings are *immutable*. This means that we cannot change a string once it is created. We can use it to create other strings, but we cannot change the string itself.

This property, generally, is known as *mutability*. Data types that are *mutable* can be changed, and data types, like strings, that are *immutable* cannot be changed.





<hr>

#### Escape Characters

Occasionally when working with strings, you’ll find that you want to include characters that already have a special meaning in python. For example let’s say I create the string

```python
 favorite_fruit_conversation = "He said, "blueberries are my favorite!""
```

We’ll have accidentally ended the string before we wanted to by including the `"` character. The way we can do this is by introducing *escape characters*. By adding a backslash in front of the special character we want to escape, `\"`, we can include it in a string.

```pyhon
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
```

Now it works!



<hr>

#### Iterating through Strings

Now you know enough about strings that we can start doing the really fun stuff!

Because strings are lists, that means we can iterate through a string using `for` or `while` loops. This opens up a whole range of possibilities of ways we can manipulate and analyze strings. Let’s take a look at an example.

```python
def print_each_letter(word):
  for letter in word:
    print(letter)
```

This code will iterate through each letter in a given word and will print it to the terminal.

```python
>>> favorite_color = "blue"
>>> print_each_letter(favorite_color)
'b'
'l'
'u'
'e'
```

Let’s try a couple problems where we need to iterate through a string.



<hr>

#### Strings and Conditionals (Part One)

Now that we are iterating through strings, we can really explore the potential of strings. When we iterate through a string we do *something* with each character. By including conditional statements inside of these iterations, we can start to do some really cool stuff.

Take a look at the following code:

```python
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)
```

This code will count the number of `b`s in the string “blueberry” (hint: it’s two). Let’s take a moment and break down what exactly this code is doing.

First, we define our string, `favorite_fruit`, and a variable called `counter`, which we set equal to zero. Then the `for` loop will iterate through each character in `favorite_fruit` and compare it to the letter `b`.

Each time a character equals `b` the code will increase the variable `counter` by one. Then, once all characters have been checked, the code will print the counter, telling us how many `b`s were in “blueberry”. This is a great example of how iterating through a string can be used to solve a specific application, in this case counting a certain letter in a word.



```python
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False
```

```python
def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  for c in string_two:
    if c in string_one:
      return c

print(common_letters('banana', 'cream'))
```





<hr>

#### Review

Great work! I hope you are now starting to see the potential of strings and how they can be used to solve a huge variety of problems.

In this lesson you learned:

- A string is a list of characters.
- A character can be selected from a string using its index `string_name[index]`. These indices start at 0.
- A ‘slice’ can be selected from a string. These can be between two indices or can be open-ended, selecting all of the string from a point.
- Strings can be concatenated to make larger strings.
- `len()` can be used to determine the number of characters in a string.
- Strings can be iterated through using `for` loops.
- Iterating through strings opens up a huge potential for applications, especially when combined with conditional statements.

Let’s put your new skills to the test!



**1.**

*Copeland’s Corporate Company* has finalized what they want to their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, `username_generator` and `password_generator`.

Let’s start with `username_generator`. Create a function called `username_generator` take two inputs, `first_name` and `last_name` and returns a `username`. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

For example, if the employee’s name is `Abe Simpson` the function should generate the username `AbeSimp`.

Checkpoint 2 Passed



**2.**

Great work! Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is `AbeSimp`, then the temporary password generated should be `pAbeSim`.

Start by defining the function `password_generator` so that it takes one input, `username` and in it define an empty string named `password`.

Checkpoint 3 Passed



**3.**

Inside `password_generator` create a for loop that iterates through the indices username by going from `0` to `len(username)`.

To shift the letters right, at each letter the for loop should add the previous letter to the string `password`.





```python
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
```





<hr>

#### Splitting Strings

`.upper()`, `.lower()`, and `.title()` all are performed on an existing string and produce a string in return. Let’s take a look at a string method that returns a different object entirely!

`.split()` is performed on a string, takes one argument, and returns a list of substrings found between the given argument (which in the case of `.split()` is known as the delimiter). The following syntax should be used:

```python
string_name.split(delimiter)
```

If you do not provide an argument for `.split()` it will default to splitting at spaces.

For example, consider the following strings:

```python
>>> man_its_a_hot_one = "Like seven inches from the midday sun"
>>> man_its_a_hot_one.split()
['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']
```

`.split` returned a list with each word in the string. Important to note: if we run `.split()` on a string with no spaces, we will get the same string in return.





<hr>



#### Splitting Strings II

If we provide an argument for `.split()` we can dictate the character we want our string to be split on. This argument should be provided as a string itself.

Consider the following example:

```python
>>> greatest_guitarist = "santana"
>>> greatest_guitarist.split('n')
['sa', 'ta', 'a']
```

We provided `'n'` as the argument for `.split()` so our string “santana” got split at each `'n'` character into a list of three strings.

What do you think happens if we split the same string at `'a'`?

```python
>>> greatest_guitarist.split('a')
['s', 'nt', 'n', ' ']
```

Notice that there is an unexpected extra `''` string in this list. When you split a string on a character that it also ends with, you’ll end up with an empty string at the end of the list.

You can use *any* string as the argument for `.split()`, making it a versatile and powerful tool.



```python
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"


author_names = authors.split(',')

author_last_names = []

for i in author_names:
  author_last_name = i.split(' ')
  author_last_names.append(author_last_name[-1])

print(author_last_names)
```



<hr>

#### Splitting Strings III

We can also split strings using *escape sequences*. Escape sequences are used to indicate that we want to split by something in a string that is not necessarily a character. The two escape sequences we will cover here are

- `\n` Newline
- `\t` Horizontal Tab

Newline or `\n` will allow us to split a multi-line string by line breaks and `\t` will allow us to split a string by tabs. `\t` is particularly useful when dealing with certain datasets because it is not uncommon for data points to be separated by tabs.

Let’s take a look at an example of splitting by an escape sequence:

```python
smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines)
```

This code is splitting the multi-line string at the newlines (`\n`) which exist at the end of each line and saving it to a new list called `chorus_lines`. Then it prints `chorus_lines` which will produce the output

```python
['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to better suit your mood', "Because you're so smooth"]
```

The new list contains each line of the original string as it’s own smaller string. Also, notice that Python automatically escaped the `'` character when it created the new list.



```python
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
```



<hr>

#### Joining Strings

Now that you’ve learned to break strings apart using `.split()`, let’s learn to put them back together using `.join()`. `.join()` is essentially the opposite of `.split()`, it *joins* a list of strings together with a given delimiter. The syntax of `.join()` is:

```python
'delimiter'.join(list_you_want_to_join)
```

Now this may seem a little weird, because with `.split()` the argument was the delimiter, but now the argument is the list. This is because *join* is still a string method, which means it has to act on a string. The string `.join()` acts on is the delimiter you want to join with, therefore the list you want to join has to be the argument.

This can be a bit confusing, so let’s take a look at an example.

```python
>>> my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
>>> ' '.join(my_munequita)
'My Spanish Harlem Mona Lisa'
```

We take the list of strings, `my_munequita`, and we joined it together with our delimiter, `' '`, which is a space. The space is important if you are trying to build a sentence from words, otherwise, we would have ended up with:

```python
>>> ''.join(my_munequita)
'MySpanishHarlemMonaLisa'
```

```python
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
```



<hr>



#### Joining Strings II

In the last exercise, we joined together a list of words using a space as the delimiter to create a sentence. In fact, you can use any string as a delimiter to join together a list of strings. For example, if we have the list

```python
>>> santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
```

We could join this list together with ANY string. One often used string is a comma `,` because then we can create a string of *comma separated variables*, or CSV.

```python
>>> santana_songs_csv = ','.join(santana_songs)
>>> santana_songs_csv
'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'
```

You’ll often find data stored in CSVs because it is an efficient, simple file type used by popular programs like Excel or Google Spreadsheets.

You can also join using *escape sequences* as the delimiter. Consider the following example:

```python
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']

smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)

print(smooth_fifth_verse)
```

This code is taking the list of strings and joining them using a newline `\n` as the delimiter. Then it prints the result and produces the output:

```python
Well I'm from the barrio
You hear my rhythm on your radio
You feel the turning of the world so soft and slow
Turning you 'round and 'round
```



```python
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
```





<hr>

#### .strip()

When working with strings that come from real data, you will often find that the strings aren’t super clean. You’ll find lots of extra whitespace, unnecessary linebreaks, and rogue tabs.

Python provides a great method for cleaning strings: `.strip()`. Stripping a string removes all whitespace characters from the beginning and end. Consider the following example:

```python
>>> featuring = "           rob thomas                 "
>>> featuring.strip()
'rob thomas'
```

All the whitespace on either side of the string has been stripped, but the whitespace in the middle has been preserved.

You can also use `.strip()` with a character argument, which will strip that character from either end of the string.

```python
>>> featuring = "!!!rob thomas       !!!!!"
>>> featuring.strip('!')
'rob thomas       '
```

By including the argument `'!'` we are able to strip all of the `!` characters from either side of the string. Notice that now that we’ve included an argument we are no longer stripping whitespace, we are ONLY stripping the argument.



```python
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = []


# for i in love_maybe_lines:
#   love_maybe_lines_stripped.append(i.strip())

# love_maybe_full = '\n'.join(love_maybe_lines_stripped)
# print(love_maybe_full)



for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
  
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)
```



<hr>

#### Replace

The next string method we will cover is `.replace()`. Replace takes two arguments and replaces all instances of the first argument in a string with the second argument. The syntax is as follows

```python
string_name.replace(character_being_replaced, new_character)
```

Great! Let’s put it in context and look at an example.

```python
>>> with_spaces = "You got the kind of loving that can be so smooth"
>>> with_underscores = with_spaces.replace(' ', '_')
>>> with_underscores
'You_got_the_kind_of_loving_that_can_be_so_smooth'
```

Here we used `.replace()` to change every instance of a space in the string above to be an underscore instead.



```python
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
```



<hr>



#### .find()

Another interesting string method is `.find()`. `.find()` takes a string as an argument and searching the string it was run on for that string. It then returns the first *index value* where that string is located.

Here’s an example:

```python
>>> 'smooth'.find('t')
'4'
```

We searched the string `'smooth'` for the string `'t'` and found that it was at the fourth index spot, so `.find()` returned `4`.

You can also search for larger strings, and `.find()` will return the index value of the first character of that string.

```python
>>>"smooth".find('oo')
'2'
```

Notice here that `2` is the index of the *first* o.







