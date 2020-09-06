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





