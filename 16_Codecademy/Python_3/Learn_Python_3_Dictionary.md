#### Invalid Keys

We can have a list or a dictionary as a *value* of an item in a dictionary, but we cannot use these data types as keys of the dictionary. If we try to, we will get a `TypeError`. For example:

```py
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
```

will yield:

```
TypeError: unhashable type: 'list'
```

The word “unhashable” in this context means that this ‘list’ is an object that can be changed. Dictionaries in Python rely on each key having a *hash value*, a specific identifier for the key. If the key can change, that hash value would not be reliable. So the keys must always be unchangeable, hashable data types, like numbers or strings.



```python
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
```





#### Add A Key

To add a single key : value pair to a dictionary, we can use the syntax:

```python
my_dict["new_key"] = "new_value"
```

For example, if we had our `menu` object from the first exercise:

```python
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```

and we wanted to add a new item, `"cheesecake"` for `8` dollars, we could use:

```python
menu["cheesecake"] = 8
```

Now, `menu` looks like:

```python
{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}
```





#### Add Multiple Keys

If we wanted to add multiple key : value pairs to a dictionary at once, we can use the `.update()` method.

Looking at our `sensors` object from the first exercise:

```python
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
```

If we wanted to add 3 new rooms, we could use:

```python
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
```

which would add all three items to the `sensors` dictionary. Now, `sensors` looks like:

```python
 {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}
```

```python
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({'theLooper':138475, 'stringQueen': 85739})

print(user_ids)
```





#### Overwrite Values

We know that we can add a key by using syntax like:

```python
menu['avocado toast'] = 7
```

which will create a key `'avocado toast'` and set the value to `7`. But what if we already have an `'avocado toast'` entry in the `menu` dictionary?

In that case, our value assignment would overwrite the existing value attached to the key `'avocado toast'`.

```python
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
```

would yield:

```python
{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```

Notice the value of `"oatmeal"` has now changed to `5`.

```python
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners.update({'Supporting Actress': 'Viola Davis'})

oscar_winners['Best Picture'] = 'Moonlight'
```





## Review

So far we have learned:

- How to create a dictionary
- How to add elements to a dictionary
- How to update elements in a dictionary
- How to use a list comprehension to create a dictionary from two lists

Let’s practice these skills!



### Instructions

**1.**

We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.

Using a list comprehension, create a dictionary called `plays` that goes through `zip(songs, playcounts)` and creates a `song`:`playcount` pair for each `song` in `songs` and each `playcount` in `playcounts`.

Checkpoint 2 Passed





**2.**

Print `plays`.

Checkpoint 3 Passed



**3.**

After printing `plays`, add a new entry to it. The entry should be for the song `"Purple Haze"` and the playcount is `1`.

Checkpoint 4 Passed



**4.**

This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for `"Respect"` to be 94 in the `plays` dictionary.

Checkpoint 5 Passed



**5.**

Create a dictionary called `library` that has two key: value pairs:

- key `"The Best Songs"` with a value of `plays`, the dictionary you created
- key `"Sunday Feelings"` with a value of an empty dictionary

Checkpoint 6 Passed



**6.**

Print `library`.



```python
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for song, playcount in zip(songs, playcounts)}

print(plays)

plays.update({'Purple Haze' : 1})

plays['Respect'] = 94

library = {'The Best Songs': plays, 'Sunday Feelings': {}}

print(library)
```





#### Get A Key

Once you have a dictionary, you can access the values in it by providing the key. For example, let’s imagine we have a dictionary that maps buildings to their heights, in meters:

```python
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
```

Then we can access the data in it like this:

```python
>>> building_heights["Burj Khalifa"]
828
>>> building_heights["Ping An"]
599
```

```python
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements['earth'])
print(zodiac_elements['fire'])
```







#### Get an Invalid Key

Let’s say we have our dictionary of building heights from the last exercise:

```python
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
```

What if we wanted to know the height of the Landmark 81 in Ho Chi Minh City? We could try:

```python
print(building_heights["Landmark 81"])
```

But `"Landmark 81"` does not exist as a key in the `building_heights` dictionary! So this will throw a KeyError:

```python
KeyError: 'Landmark 81'
```

One way to avoid this error is to first check if the key exists in the dictionary:

```python
key_to_check = "Landmark 81"

if key_to_check in building_heights:
  print(building_heights["Landmark 81"])
```

This will not throw an error, because `key_to_check in building_heights` will return `False`, and so we never try to access the key.

```python
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements.update({'energy':'Not a Zodiac element'})
print(zodiac_elements["energy"])
```





#### Try/Except to Get a Key

We saw that we can avoid `KeyError`s by checking if a key is in a dictionary first. Another method we could use is a `try/except`:

```python
key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")
```

When we try to access a key that doesn’t exist, the program will go into the `except` block and print `"That key doesn't exist!"`.



```python
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, 'matcha' : 30}

try:
  print(caffeine_level['matcha'])
except KeyError:
  print('Unknown Caffeine Level')
```







#### Safely Get a Key

We saw in the last exercise that we had to add a key:value pair to a dictionary in order to avoid a KeyError. This solution is not sustainable. We can’t predict every key a user may call and add all of those placeholder values to our dictionary!

Dictionaries have a `.get()` method to search for a value instead of the `my_dict[key]` notation we have been using. If the key you are trying to `.get()` does not exist, it will return `None` by default:

```python
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

#this line will return None:
building_heights.get("My House")
```

You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary:

```python
>>> building_heights.get('Shanghai Tower', 0)
632
>>> building_heights.get('Mt Olympus', 0)
0
>>> building_heights.get('Kilimanjaro', 'No Value')
'No Value'
```

```python
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get('teraCoder', 100000)
print(tc_id)

stack_id = user_ids.get('superStackSmash', 100000)
print(stack_id)
```







#### Delete a Key

Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this dictionary mapping ticket numbers to prizes:

```py
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
```

When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize has been given away. We can use `.pop()` to do this. Just like with `.get()`, we can provide a default value to return if the key does not exist in the dictionary:

```py
>>> raffle.pop(320291, "No Prize")
"Gift Basket"
>>> raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
>>> raffle.pop(100000, "No Prize")
"No Prize"
>>> raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
>>> raffle.pop(872921, "No Prize")
"Concert Tickets"
>>> raffle
{223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}
```

`.pop()` works to delete items from a dictionary, when you know the key value.

```python
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}

health_points = 20

health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)
```







#### Get All Keys

Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a math class and their grades:

```py
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
```

We want to get a roster of the students in the class, without including their grades. We can do this with the built-in `list()` function:

```py
>>> list(test_scores)
["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
```

Dictionaries also have a `.keys()` method that returns a `dict_keys` object. A `dict_keys` object is a *view* object, which provides a look at the current state of the dicitonary, without the user being able to modify anything. The `dict_keys` object returned by `.keys()` is a set of the keys in the dictionary. You cannot add or remove elements from a `dict_keys` object, but it can be used in the place of a list for iteration:

```py
for student in test_scores.keys():
  print(student)
```

will yield:

```
"Grace"
"Jeffrey"
"Sylvia"
"Pedro"
"Martin"
"Dina"
```

```python
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

lessons = num_exercises.keys()

print(users)
print(lessons)
```





#### Get All Keys

Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a math class and their grades:

```py
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
```

We want to get a roster of the students in the class, without including their grades. We can do this with the built-in `list()` function:

```py
>>> list(test_scores)
["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
```

Dictionaries also have a `.keys()` method that returns a `dict_keys` object. A `dict_keys` object is a *view* object, which provides a look at the current state of the dicitonary, without the user being able to modify anything. The `dict_keys` object returned by `.keys()` is a set of the keys in the dictionary. You cannot add or remove elements from a `dict_keys` object, but it can be used in the place of a list for iteration:

```py
for student in test_scores.keys():
  print(student)
```

will yield:

```
"Grace"
"Jeffrey"
"Sylvia"
"Pedro"
"Martin"
"Dina"
```

```python
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for value in num_exercises.values():
  total_exercises += value 

print(total_exercises)
```





#### Get All Items

You can get both the keys and the values with the `.items()` method. Like `.keys()` and `.values()`, it returns a `dict_list` object. Each element of the `dict_list` returned by `.items()` is a tuple consisting of:

```py
(key, value)
```

so to iterate through, you can use this syntax:

```python
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
```

which would yield this output:

```
Apple has a value of 184 billion dollars.
Google has a value of 141.7 billion dollars.
Microsoft has a value of 80 billion dollars.
Coca-Cola has a value of 69.7 billion dollars.
Amazon has a value of 64.8 billion dollars.
```



```python
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
  print(f'Women make up {value} percent of {key}s.')
```





Scrabble

In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!

If you get stuck during this project or would like to see an experienced developer work through it, click “**Get Help**“ to see a **project walkthrough video**.



### Tasks

15/15 Complete

Mark the tasks as complete by checking them off

## Build your Point Dictionary



**1.**

We have provided you with two lists, `letters` and `points`. We would like to combine these two into a dictionary that would map a letter to its point value.

Using a list comprehension and `zip`, create a dictionary called `letter_to_points` that has the elements of `letters` as the keys and the elements of `points` as the values.

Stuck? Get a hint



**2.**

Our `letters` list did not take into account blank tiles. Add an element to the `letter_to_points` dictionary that has a key of `" "` and a point value of `0`.

Stuck? Get a hint

## Score a Word



**3.**

We want to create a function that will take in a word and return how many points that word is worth.

Define a function called `score_word` that takes in a parameter `word`.

Stuck? Get a hint



**4.**

Inside `score_word`, create a variable called `point_total` and set it to `0`.



**5.**

After defining `point_total`, create a for loop that goes through the letters in `word` and adds the point value of each letter to `point_total`.

You should get the point value from the `letter_to_points` dictionary. If the letter you are checking for is not in `letter_to_points`, add 0 to the `point_total`.

Stuck? Get a hint



**6.**

After the for loop is finished, return `point_total`.



**7.**

Let’s test this function! Create a variable called `brownie_points` and set it equal to the value returned by the `score_word()` function with an input of `"BROWNIE"`.



**8.**

We expect the word BROWNIE to earn 15 points:

```
(B + R + O + W + N + I + E)

(3 + 1 + 1 + 4 + 4 + 1 + 1) = 15
```

Let’s print out `brownie_points` to make sure we got it right.

## Score a Game



**9.**

Create a dictionary called `player_to_words` that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:

| player1 | wordNerd | Lexi Con | Prof Reader |
| ------- | -------- | -------- | ----------- |
| BLUE    | EARTH    | ERASER   | ZAP         |
| TENNIS  | EYES     | BELLY    | COMA        |
| EXIT    | MACHINE  | HUSKY    | PERIOD      |

Hint

A dictionary with one player, Player Lonely, who has played the three words WISHING, FOR, and FRIENDS, would look like:

```py
player_to_words = {"Player Lonely": ["WISHING", "FOR", "FRIENDS"]}
```



**10.**

Create an empty dictionary called `player_to_points`.

Hint

To initialize an empty dictionary, use empty brackets (`{}`).



**11.**

Iterate through the items in `player_to_words`. Call each player `player` and each list of words `words`.

Within your loop, create a variable called `player_points` and set it to 0.

Hint

To iterate through items in a dictionary, we can use this syntax:

```py
for key, value in my_dict.items():
  ... do something with key or value ...
```



**12.**

Within the loop, create another loop that goes through each `word` in `words` and adds the value of `score_word()` with `word` as an input.

Hint

Nested loops look like this:

```py
for item1 in one_list_or_dict:
  for item2 in another_object:
     ... do something with item1 or item2 ...
```



**13.**

After the inner loop ends, set the current `player` value to be a key of `player_to_points`, with a value of `player_points`.

Hint

To set a key:value pair in a dictionary, use the syntax:

```py
my_dict[key_to_add] = value_to_add
```



**14.**

`player_to_points` should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game!

If you’ve calculated correctly, wordNerd should be winning by 1 point.

## Ideas for Further Practice!



**15.**

If you want extended practice, try to implement some of these ideas with the Python you’ve learned:

- `play_word()` — a function that would take in a player and a word, and add that word to the list of words they’ve played
- `update_point_totals()` — turn your nested loops into a function that you can call any time a word is played
- make your `letter_to_points` dictionary able to handle lowercase inputs as well





```python
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letters:points for letters, points in zip(letters, points)}

letter_to_points.update({" ": 0})


def score_word(word):
  point_total = 0
  for l in word:
    point_total += letter_to_points.get(l)
    
  return point_total

brownie_point = score_word('BROWNIE')

print(brownie_point)

player_to_words = {'BLUE' : ['EARTH', 'ERASE', 'ZAP'], 'TENNIS': ['EYES', 'EYES', 'BELLY', 'COMA'], 'EXIT': ['MACHINE', 'HUSKY', 'PERIOD']}

player_to_points = {}

for player, words in player_to_words.items():
  plyaer_points = 0
  for word in words:
    plyaer_points = score_word(word)
  player_to_points[player] = plyaer_points



```





Frequency Count

```
frequency_dictionary()
```



### Instructions

**1.**

Write a function named `frequency_dictionary` that takes a list of elements named `words` as a parameter. The function should return a dictionary containing the frequency of each element in `words`.



```python
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
```





Unique Values

```
unique_values()
```



### Instructions

**1.**

Create a function named `unique_values` that takes a dictionary named `my_dictionary` as a parameter. The function should return the number of unique values in the dictionary.



```python
# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
```





Count First Letter

```
count_first_letter()
```



### Instructions

**1.**

Create a function named `count_first_letter` that takes a dictionary named `names` as a parameter. `names` should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:

```py
names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
```

The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

So in example above, the function would return:

```py
{"S" : 4, "L": 3}
```





```python
# Write your count_first_letter function here:
def count_first_letter(names):
  empty = {}
  for key, value in names.items():
    if key[0] not in empty:
      empty[key[0]] = len(value)
    else:
      empty[key[0]] += len(value)
  return empty
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
```

