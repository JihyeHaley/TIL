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

```python
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
```





<hr>

#### .format()

Python also provides a handy string method for including variables in strings. This method is `.format()`. `.format()` takes variables as an argument and includes them in the string that it is run on. You include `{}` marks as placeholders for where those variables will be imported.

Consider the following function:

```python
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)
```

The function `favorite_song_statement` takes two arguments, song and artist, then returns a string that includes both of the arguments and prints a sentence. Note: `.format()` can take as many arguments as there are `{}` in the string it is run on, which in this case in two.

Here’s an example of the function being run:

```python
>>> favorite_song_statement("Smooth", "Santana")
"My favorite song is Smooth by Santana"
```

Now you may be asking yourself, I could have written this function using string concatenation instead of `.format()`, why is this method better? The answer is legibility and reusability. It is much easier to picture the end result `.format()` than it is to picture the end result of string concatenation and legibility is everything. You can also reuse the same base string with different variables, allowing you to cut down on unnecessary, hard to interpret code.



```python
def poem_title_card(poet, title):
  return 'The poem \"{0}\" is written by {1}.' .format(title, poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))
```



<hr>

```python
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
# print(highlighted_poems_list)


highlighted_poems_stripped = []
for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip(' '))
# print(highlighted_poems_stripped)

highlighted_poems_details = []
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(':'))

titles = []
poets = []
dates = []

for i in highlighted_poems_details:
  titles.append(i[0])
  poets.append(i[1])
  dates.append(i[2])

for i in range(0, len(titles)):
  print('The poem {0} was published by {1} in {2}.'.format(titles[i], poets[i], dates[i]))
```







<hr>

#### Thread Shed

You’ve recently been hired as a cashier at the local sewing hobby shop, ***Thread Shed\***. Some of your daily responsibilities involve tallying the number of sales during the day, calculating the total amount of money made, and keeping track of the names of the customers.

Unfortunately, the ***Thread Shed\*** has an extremely out-dating register system and stores all of the transaction information in one huge unwieldy string called `daily_sales`.

All day, for each transaction, the name of the customer, amount spent, types of thread purchased, and the date of sale is all recorded in this same string. Your task is to use your Python skills to iterate through this string and clean up each transaction and store all the information in easier to access lists.

If you get stuck during this project or would like to see an experienced developer work through it, click “**Get Help**“ to see a **project walkthrough video**.



### Tasks

22/22 Complete

Mark the tasks as complete by checking them off

## Break up `daily_sales` in easy to understand lists `customers`, `sales`, and `threads_sold`.



**1.**

First, take a minute to inspect the string `daily_sales` in the code editor.

How is each transaction stored? How is each piece of data within the transaction stored?

Start thinking about how we can split up this string into its individual pieces of data.



**2.**

It looks like each transaction is separated from the next transaction by a `,`, and then each piece of data within a transaction is separated by the artifact `;,;`.

If we want to split up `daily_sales` into a list of individual transactions, we are going to want to split by `,`, but first, we need to replace the artifact `;,;` to something *without* a comma, so we don’t split any transactions themselves.

Replace all the instances of `;,;` in `daily_sales` with some other character and save the result to `daily_sales_replaced`.

Stuck? Get a hint



**3.**

Now we can split the string into a list of each individual transaction.

Split `daily_sales_replaced` around commas and save it to a new list `daily_transactions`.

Stuck? Get a hint



**4.**

Print `daily_transactions`.

How does it look?



**5.**

Our next step is to split each individual transaction into a list of its data points.

First, define an empty list `daily_transactions_split`



**6.**

Now, iterate through `daily_transactions` (remember, this is a list of strings currently), and for each transaction, split the string around whatever character you replaced the `;,;` artifacts with in **Step 2**.

Append each of these split strings (which are lists now) to our new list `daily_transactions_split`.

Stuck? Get a hint



**7.**

Print `daily_transactions_split`.

How’s it looking?



**8.**

It looks like each data item has inconsistent whitespace around it. First, define an empty list `transactions_clean`.

Now, Iterate through `daily_transactions_split` and for each transaction iterate through the different data points and strip off any whitespace.

Add each of these cleaned up transactions to the new list `transactions_clean`.

Stuck? Get a hint



**9.**

Print `transactions_clean`.

If you performed the last step correctly, you shouldn’t see any unnecessary whitespace.



**10.**

Create three empty lists. `customers`, `sales`, and `thread_sold`. We are going to collect the individual data points for each transaction in these lists.



**11.**

Now, iterate through `transactions_clean` and for each transaction:

1. Append the customers name to `customers`.
2. Append the amount of the sale to `sales`.
3. Append the threads sold to `thread_sold`.



**12.**

Print `customers`, `sales`, and `thread_sold` to make sure each list is what you are expected.

## Determine the total value of the days sales.



**13.**

Now we want to know how much *Thread Shed* made in a day.

First, define a variable called `total_sales` and set it equal to `0`.



**14.**

Now, consider the list `sales`. It is a list of *strings* that we want to sum. In order for us to sum these values, we will have to remove the `$`, and set them equal to floats.

Iterate through `sales` and for each item, strip off the `$`, set it equal to a float, and add it to `total_sales`



**15.**

Print `total sales`.

How much did we make today?

## How much thread of any specific color was sold?



**16.**

Finally, we want to determine how many of each color thread we sold today. Let’s start with a single color, and then we’ll generalize it.

First, print out `thread_sold` and inspect it.



**17.**

We see that `thread_sold` is a list of strings, some are single colors and some are multiple colors separated by the `&` character.

The end product we want here is a list that contains an item for each color thread sold, so no strings that have multiple colors in them.

First, define an empty list `thread_sold_split`.



**18.**

Next, iterate through thread_sold. For each item, check if it is a single color or multiple colors. If it is a single color, append that color to `thread_sold_split`.

If it is multiple colors, first split the string around the `&` character and then add each color indivudally to `thread_sold_split`.



**19.**

Great, now we have a list `thread_sold_split` that contains an entry with the color of every thread sold today.

Define a function called `color_count` that takes one argument, `color`. The function should iterate through `thread_sold_split` and count the number of times the item is equal to argument, `color`. Then, it should return this count.



**20.**

Test your new function by running `color_count('white')`.

Your function should return `28`.



**21.**

Define a list called `colors` that stores all of the colored threads that *Thread Shed* offers:

```py
colors = ['red','yellow','green','white','black','blue','purple']
```



**22.**

Now, using the list `colors`, the string method `.format()`, and the function `color_count`, iterate through `thread_sold_split` and print a sentence that says how many threads of each color were sold today.

<hr>

```python
daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

#------------------------------------------------
# Start coding below!

# 1.
# print(daily_sales)
daily_sales_splited = daily_sales.replace(';', '').replace(' ', '').replace('\n','').split(',')
print(daily_sales_splited)

customers = []
sales = []
thread_sold = []
dates = []

for i in range(0, len(daily_sales_splited), 4):
  customers.append(daily_sales_splited[i])
  sales.append(daily_sales_splited[i+1].strip('$'))
  thread_sold.append(daily_sales_splited[i+2])
  dates.append(daily_sales_splited[i+3])


total_sales = 0
for sale in sales:
  total_sales += round(float(sale))
  print(sale)

print(total_sales)
color_white = len(thread_sold)
print(color_white)
# 2.
# daily_sales_replaces = daily_sales.replace(';,;', ',')

# 3.
# daily_transactions = daily_sales_replaces.split(',')
# print(daily_transactions)

```





<hr>

#### Count Letters

```python
unique_english_letters(word)
```



```python
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

# Uncomment these function calls to test your tip function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
```





#### Count X

```python
count_char_x()
```



```python
# Write your count_char_x function here:
def count_char_x(word, x):
  cnt = 0
  for i in word:
    if x == i :
      cnt += 1
  return cnt

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
```







#### Count Multi X

```python
count_multi_char_x()
```





```python
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  count = word.count(x)
  return count


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
```







#### Substring Between

```python
substring_between_letters()
```



 0  1  2  3  4 
 A  p  p  l  e

0 1  2  3  4  5 

```python
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  if start in word and end in word:
    first = word.find(start) + 1
    last = word.find(end)
    word_out = word[first:last]
    return word_out
  else:
    return word

  
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
```





#### X Length

```python
x_length_words()
```



```python
# Write your x_length_words function here:
def x_length_words(sentence, x):
  sentence_splited = sentence.split(' ')
  for i in sentence_splited:
    if len(i) < x:
      return False
  return True
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
```





#### Check Name

```python
check_for_name()
```



```python
# Write your check_for_name function here:
def check_for_name(sentence, name):
  sentence_splited = sentence.split(' ')
  if sentence_splited[3].title() == name:
    return True
  else:
    return False
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False
```





