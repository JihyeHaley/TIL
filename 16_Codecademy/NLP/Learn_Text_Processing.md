## Noise Removal

Text cleaning is a technique that developers use in a variety of domains. Depending on the goal of your project and where you get your data from, you may want to remove unwanted information, such as:

- punctuation and accents
- special characters
- numeric digits
- leading, ending, and vertical whitespace
- HTML formatting

The type of noise that you need to remove from text usually depends on its source. For example, you could access data via the Twitter API, scraping a webpage, or voice recognition software. Fortunately, you can use the `.sub()` method in Python’s regular expression (`re`) library for most of your noise removal needs.

The `.sub()` method has three required arguments:

1. `pattern` – a regular expression that is searched for in the input string. There must be an `r` preceding the string to indicate it is a raw string, which treats backslashes as literal characters.
2. `replacement_text` – text that replaces all matches in the input string
3. `input` – the input string that will be edited by the `.sub()` method

The method returns a string with all instances of the `pattern` replaced by the `replacement_text`. Let’s see a few examples of using this method to remove and replace text from a string.

#### Examples

First, let’s consider how to remove HTML `<p>` tags from a string:

```python
import re 

text = "<p>    This is a paragraph</p>" 

result = re.sub(r'<.?p>', '', text)

print(result) 
#    This is a paragraph
```

Notice, we replace the tags with an empty string `''`. This is a common approach for removing text.

------

Next, let’s remove the whitespace from the beginning of the text. The whitespace consists of four spaces.

```python
import re 

text = "    This is a paragraph" 

result = re.sub(r'\s{4}', '', text)

print(result) 
# This is a paragraph
```

Take a look at Codecademy’s [Parsing with Regular Expressions](https://www.codecademy.com/learn/natural-language-processing/modules/nlp-regex-parsing-module) lesson if you want to learn more regular expression syntax and tricks.





**1.**

At the top of **script.py**, import the regular expression library.

Checkpoint 2 Passed

**2.**

We used a package called Beautiful Soup to scrape [The Onion website](https://www.theonion.com/) from October of 2019. We saved one of the headlines to a variable called `onion_headline`.

Remove the opening and closing `h1` tags from `onion_headline`. Save the value to `headline_no_tag`.

**3.**

We also saved a Tweet to the variable `tweet`. Remove all `@` characters. Save the result to `tweet_no_at`

```python
import re

headline_one = '<h1>Nation\'s Top Pseudoscientists Harness High-Energy Quartz Crystal Capable Of Reversing Effects Of Being Gemini</h1>'

tweet = '@fat_meats, veggies are better than you think.'
onion_headline = r'<h1>|</h1>'
headline_no_tag = re.sub(onion_headline, '', headline_one)
tweet_no_at = re.sub(r'@', '', tweet)

try:
  print(headline_no_tag)
except:
  print('No variable called `headline_no_tag`')
try:
  print(tweet_no_at)
except:
  print('No variable called `tweet_no_at`')
```





<hr>



## Tokenization

For many natural language processing tasks, we need access to each word in a string. To access each word, we first have to break the text into smaller components. The method for breaking text into smaller components is called *tokenization* and the individual components are called *tokens*.

A few common operations that require tokenization include:

- Finding how many words or sentences appear in text
- Determining how many times a specific word or phrase exists
- Accounting for which terms are likely to co-occur

While tokens are usually individual words or terms, they can also be sentences or other size pieces of text.

To tokenize individual words, we can use `nltk`‘s `word_tokenize()` function. The function accepts a string and returns a list of words:

```python
from nltk.tokenize import word_tokenize

text = "Tokenize this text"
tokenized = word_tokenize(text)

print(tokenized)
# ["Tokenize", "this", "text"]
```

------

To tokenize at the sentence level, we can use `sent_tokenize()` from the same module.

```python
from nltk.tokenize import sent_tokenize

text = "Tokenize this sentence. Also, tokenize this sentence."
tokenized = sent_tokenize(text)

print(tokenized)
# ['Tokenize this sentence.', 'Also, tokenize this sentence.']
```



**1.**

Import the `word_tokenize()` and `sent_tokenize()` functions from Python’s NLTK package.

Checkpoint 2 Passed

**2.**

Tokenize `ecg_text` by word and save the result to `tokenized_by_word`.

**3.**

Tokenize `ecg_text` by sentence and save the result to `tokenized_by_sentence`.



```python
from nltk.tokenize import word_tokenize, sent_tokenize

ecg_text = 'An electrocardiogram is used to record the electrical conduction through a person\'s heart. The readings can be used to diagnose cardiac arrhythmias.'


tokenized_by_word = word_tokenize(ecg_text)
tokenized_by_sentence = sent_tokenize(ecg_text)



try:
  print('Word Tokenization:')
  print(tokenized_by_word)
except:
  print('Expected a variable called `tokenized_by_word`')
try:
  print('Sentence Tokenization:')
  print(tokenized_by_sentence)
except:
  print('Expected a variable called `tokenized_by_sentence`')
```





<hr>



## Normalization

Tokenization and noise removal are staples of almost all text pre-processing pipelines. However, some data may require further processing through text normalization. Text *normalization* is a catch-all term for various text pre-processing tasks. In the next few exercises, we’ll cover a few of them:

- Upper or lowercasing
- Stopword removal
- *Stemming* – bluntly removing prefixes and suffixes from a word
- *Lemmatization* – replacing a single-word token with its root

The simplest of these approaches is to change the case of a string. We can use Python’s built-in String methods to make a string all uppercase or lowercase:

```python
my_string = 'tHiS HaS a MiX oF cAsEs'

print(my_string.upper())
# 'THIS HAS A MIX OF CASES'

print(my_string.lower())
# 'this has a mix of cases'
```

**1.**

Make all the characters in `brands` lowercase and save the results to `brands_lower`.

**2.**

Make all the letters in `brands` uppercase and save the results to `brands_upper`.

```python
brands = 'Salvation Army, YMCA, Boys & Girls Club of America'


brands_lower = brands.lower()
brands_upper = brands.upper()

try:
  print(f'Lowercased brands: {brands_lower}')
except:
  print('Expected a variable called `brands_lower`')
try:
  print(f'Uppercased brands: {brands_upper}')
except:
  print('Expected a variable called `brands_upper`')
```






<hr>



## Stopword Removal

Stopwords are words that we remove during preprocessing when we don’t care about sentence structure. They are usually the most common words in a language and don’t provide any information about the tone of a statement. They include words such as “a”, “an”, and “the”.

NLTK provides a built-in library with these words. You can import them using the following statement:

```python
from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english')) 
```

We create a set with the stop words so we can check if the words are in a list below.

Now that we have the words saved to `stop_words`, we can use tokenization and a list comprehension to remove them from a sentence:

```python
nbc_statement = "NBC was founded in 1926 making it the oldest major broadcast network in the USA"

word_tokens = word_tokenize(nbc_statement) 
# tokenize nbc_statement

statement_no_stop = [word for word in word_tokens if word not in stop_words]

print(statement_no_stop)
# ['NBC', 'founded', '1926', 'making', 'oldest', 'major', 'broadcast', 'network', 'USA']
```

In this code, we first tokenized our string, `nbc_statement`, then used a list comprehension to return a list with all of the stopwords removed.



**1.**

At the top of your script, import stopwords from NLTK. Save all English stopwords, as a set, to a variable called `stop_words`.

**2.**

Tokenize the text in `survey_text` and save the result to `tokenized_survey`.

**3.**

Remove stop words from `tokenized_survey` and save the result to `text_no_stops`.



```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

survey_text = 'A YouGov study found that American\'s like Italian food more than any other country\'s cuisine.'

stop_words = set(stopwords.words('english'))


tokenized_survey = word_tokenize(survey_text)
text_no_stops = [f for f in tokenized_survey if f not in stop_words]



try:
  print(f'Stopwords type: {type(stop_words)}')
except:
  print('Expected a variable called `stop_words`')
try:
  print(f'Words Tokenized: {tokenized_survey}')
except:
  print('Expected a variable called `tokenized_survey`')
try:
  print(f'Text without Stops: {text_no_stops}')
except:
  print('Expected a variable called `text_no_stops`')
  
```





<hr>



## Stemming

In natural language processing, *stemming* is the text preprocessing normalization task concerned with bluntly removing word affixes (prefixes and suffixes). For example, stemming would cast the word “going” to “go”. This is a common method used by search engines to improve matching between user input and website hits.

NLTK has a built-in stemmer called PorterStemmer. You can use it with a list comprehension to stem each word in a tokenized list of words.

First, you must import and initialize the stemmer:

```python
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
```

Now that we have our stemmer, we can apply it to each word in a list using a list comprehension:

```python
tokenized = ['NBC', 'was', 'founded', 'in', '1926', '.', 'This', 'makes', 'NBC', 'the', 'oldest', 'major', 'broadcast', 'network', '.']

stemmed = [stemmer.stem(token) for token in tokenized]

print(stemmed)
# ['nbc', 'wa', 'found', 'in', '1926', '.', 'thi', 'make', 'nbc', 'the', 'oldest', 'major', 'broadcast', 'network', '.']
```

Notice, the words like ‘was’ and ‘founded’ became ‘wa’ and ‘found’, respectively. The fact that these words have been reduced is useful for many language processing applications. However, you need to be careful when stemming strings, because words can often be converted to something unrecognizable.


**1.**

At the top of **script.py**, import `PorterStemmer`, then initialize an instance of it and save the object to a variable called `stemmer`.



**2.**

Tokenize `populated_island` and save the result to `island_tokenized`.



**3.**

Use a list comprehension to stem each word in `island_tokenized`. Save the result to a variable called `stemmed`.

```python
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

populated_island = 'Java is an Indonesian island in the Pacific Ocean. It is the most populated island in the world, with over 140 million people.'

stemmer = PorterStemmer()
island_tokenized = word_tokenize(populated_island)

stemmed = [stemmer.stem(it) for it in island_tokenized]




try:
  print('A stemmer exists:')
  print(stemmer)
except:
  print('Expected a variable called `stemmer`')
try:
  print('Words Tokenized:')
  print(island_tokenized)
except:
  print('Expected a variable called `island_tokenized`')
try:
  print('Stemmed Words:')
  print(stemmed)
except:
  print('Expected a variable called `stemmed`')
  
```

<hr>



## Lemmatization

*Lemmatization* is a method for casting words to their root forms. This is a more involved process than stemming, because it requires the method to know the part-of-speech for each word. Since lemmatization requires the part of speech, it is a less efficient approach than stemming.

In the next exercise, we will consider how to tag each word with a part of speech. In the meantime, let’s see how to use NLTK’s lemmatize operation.

We can use NLTK’s `WordNetLemmatizer` to lemmatize text:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
```

Once we have the `lemmatizer` initialized, we can use a list comprehension to apply the lemmatize operation to each word in a list:

```python
tokenized = ["NBC", "was", "founded", "in", "1926"]

lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]

print(lemmatized)
# ["NBC", "wa", "founded", "in", "1926"]
```

The result, saved to `lemmatized` contains `'wa'`, while the rest of the words remain the same. Not too useful. This happened because `lemmatize()` treats every word as a noun. To take advantage of the power of lemmatization, we need to tag each word in our text with the most likely part of speech. We’ll do that in the next exercise.



**1.**

At the top of **script.py**, import `WordNetLemmatizer`, then initialize an instance of it and save the result to `lemmatizer`.

Stuck? Get a hint

**2.**

Tokenize the string saved to `populated_island`. Save the result to `tokenized_string`.

Stuck? Get a hint

**3.**

Use a list comprehension to lemmatize every word in `tokenized_string`. Save the result to the variable `lemmatized_words`.



```python
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

populated_island = 'Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people.'



lemmatizer = WordNetLemmatizer()

tokenized_string = word_tokenize(populated_island)
lemmatized_words = [lemmatizer.lemmatize(ts) for ts in tokenized_string]




try:
  print(f'A lemmatizer exists: {lemmatizer}')
except:
  print('Expected a variable called `lemmatizer`')
try:
  print(f'Words Tokenized: {tokenized_string}')
except:
  print('Expected a variable called `tokenized_string`')
try:
  print(f'Lemmatized Words: {lemmatized_words}')
except:
  print('Expected a variable called `lemmatized_words`')
  
```





<hr>



## Part-of-Speech Tagging

To improve the performance of lemmatization, we need to find the part of speech for each word in our string. In **script.py**, to the right, we created a part-of-speech tagging function. The function accepts a word, then returns the most common part of speech for that word. Let’s break down the steps:

#### 1. Import wordnet and Counter

```py
from nltk.corpus import wordnet
from collections import Counter
```

- `wordnet` is a database that we use for contextualizing words
- `Counter` is a container that stores elements as dictionary keys

#### 2. Get synonyms

Inside of our function, we use the `wordnet.synsets()` function to get a set of synonyms for the word:

```python
def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
```

The returned synonyms come with their part of speech.

#### 3. Use synonyms to determine the most likely part of speech

Next, we create a `Counter()` object and set each value to the count of the number of synonyms that fall into each part of speech:

```python
pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
... 
```

This line counts the number of nouns in the synonym set.

#### 4. Return the most common part of speech

Now that we have a count for each part of speech, we can use the `.most_common()` counter method to find and return the most likely part of speech:

```python
most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
```

------

Now that we can find the most probable part of speech for a given word, we can pass this into our lemmatizer when we find the root for each word. Let’s take a look at how we would do this for a tokenized string:

```python
tokenized = ["How", "old", "is", "the", "country", "Indonesia"]

lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

print(lemmatized)
# ['How', 'old', 'be', 'the', 'country', 'Indonesia']
# Previously: ['How', 'old', 'is', 'the', 'country', 'Indonesia']
```

Because we passed in the part of speech, “is” was cast to its root, “be.” This means that words like “was” and “were” will be cast to “be”.



**1.**

Navigate to the file **script.py**. At the top of the file, we imported `get_part_of_speech` for you. Use `get_part_of_speech()` to improve your lemmatizer.

Under the line with the `lemmatized` variable, use the `get_part_of_speech()` function in a list comprehension to lemmatize all the words in `tokenized_string`. Save the result to a new variable called `lemmatized_pos`.

```python

```



