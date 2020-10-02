## Intro to Bag-of-Words

“A bag-of-words is all you need,” some NLPers have decreed.

The bag-of-words language model is a simple-yet-powerful tool to have up your sleeve when working on natural language processing (NLP). The model has many, many use cases including:

- determining topics in a song
- filtering spam from your inbox
- finding out if a tweet has positive or negative sentiment
- creating word clouds



### Instructions

**1.**

In the code editor, we’ve created a spam filter using bag-of-words. Test it out!

Replace the text in `test_text` with the text from a marketing email you’ve received and run the code. Was the result what you expected?



```python
from spam_data import training_spam_docs, training_doc_tokens, training_labels
from sklearn.naive_bayes import MultinomialNB
from preprocessing import preprocess_text

# Add your email text to test_text between the triple quotes:
test_text = """
Have you ever wondered how an email ends up in the spam folder? Or how customer service phone systems are able to understand what you're saying? From a cleaner inbox to faster customer service and virtual assistants that can tell you the weather, the number of applications using natural language processing (NLP) is rapidly growing. NLP is all about how computers work with human language. Learn how to create your own powerful NLP programs with this new course!

Start Now
 
Happy coding,
Codecademy
"""
test_tokens = preprocess_text(test_text)

def create_features_dictionary(document_tokens):
  features_dictionary = {}
  index = 0
  for token in document_tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary

def tokens_to_bow_vector(document_tokens, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  for token in document_tokens:
    if token in features_dictionary:
      feature_index = features_dictionary[token]
      bow_vector[feature_index] += 1
  return bow_vector

bow_sms_dictionary = create_features_dictionary(training_doc_tokens)
training_vectors = [tokens_to_bow_vector(training_doc, bow_sms_dictionary) for training_doc in training_spam_docs]
test_vectors = [tokens_to_bow_vector(test_tokens, bow_sms_dictionary)]

spam_classifier = MultinomialNB()
spam_classifier.fit(training_vectors, training_labels)

predictions = spam_classifier.predict(test_vectors)

print("Looks like a normal email!" if predictions[0] == 0 else "You've got spam!")
```



<hr>

## Bag-of-What?

***Bag-of-words (BoW)\*** is a statistical language model based on word count. Say what?

Let’s start with that first part: a ***statistical language model\*** is a way for computers to make sense of language based on probability. For example, let’s say we have the text:

“Five fantastic fish flew off to find faraway functions. Maybe find another five fantastic fish?”

A statistical language model focused on the starting letter for words might take this text and predict that words are most likely to start with the letter “f” because 11 out of 15 words begin that way. A different statistical model that pays attention to word order might tell us that the word “fish” tends to follow the word “fantastic.”

Bag-of-words does not give a flying fish about word starts or word order though; its sole concern is ***word count\*** — how many times each word appears in a document.

If you’re already familiar with statistical language models, you may also have heard BoW referred to as the ***unigram model\***. It’s technically a special case of another statistical model, the *n*-gram model, with *n* (the number of words in a sequence) set to `1`.

If you have no idea what *n*-grams are, don’t worry — we’ll dive deeper into them in another lesson.

### Instructions

Try out a few word combinations in the applet to see how the bag-of-words model works. What happens if you add the same word a few times?



<hr>

## BoW Dictionaries

One of the most common ways to implement the BoW model in Python is as a dictionary with each key set to a word and each value set to the number of times that word appears. Take the example below:

![The squids jumped out of the suitcases.](https://content.codecademy.com/courses/NLP/bag-of-words.gif)

The words from the sentence go into the bag-of-words and come out as a dictionary of words with their corresponding counts. For statistical models, we call the text that we use to build the model our ***training data\***. Usually, we need to prepare our text data by breaking it up into `documents` (shorter strings of text, generally sentences).

Let’s build a function that converts a given training text into a bag-of-words!



### Instructions

**1.**

Define a function `text_to_bow()` that accepts `some_text` as a variable. Inside the function, set `bow_dictionary` equal to an empty dictionary and return it from the function. This is where we’ll be collecting the words and their counts.



**2.**

Above the return statement, call the `preprocess_text()` function we created for you on `some_text` and assign the result to the variable `tokens`.

Text preprocessing allows us to count words like “game” and “Games” as the same word token.



**3.**

Still above the `return`, iterate over each `token` in `tokens` and check if `token` is already in the `bow_dictionary`.

- If it is, increment that token’s count by `1`. (Remember that each `token`‘s count is its corresponding value within the `bow_dictionary`.)
- Otherwise, set the count equal to `1` because this is the first time the model has seen that word token.

To iterate through a list in Python:

```python
for some_item in list_of_items:
  # do something with some_item
```

To check if an item exists as a key in a Python dictionary:

```python
if some_item in some_dictionary:
  # execute some code
```

You can set a key-value pair in a dictionary like this:

```python
some_dictionary[some_key] = some_value
```

To increment a dictionary value in Python:

```python
some_dictionary[some_key] += 1
```

**4.**

Uncomment the print statement and run the code to see your bag-of-words function in action!

```python
from preprocessing import preprocess_text
# Define text_to_bow() below:

def text_to_bow(some_text):
  bow_dictionary = {}
  tokens = preprocess_text(some_text)
  for token in tokens:
    if token in bow_dictionary:
      bow_dictionary[token] += 1
    else:
      bow_dictionary[token] = 1
  return bow_dictionary

print(text_to_bow("I love fantastic flying fish. These flying fish are just ok, so maybe I will find another few fantastic fish..."))
```



<hr>

## Introducing BoW Vectors

Sometimes a dictionary just won’t fit the bill. Topic modelling applications, for example, require an implementation of bag-of-words that is a bit more mathematical: ***feature vectors\***.

A feature vector is a numeric representation of an item’s important features. Each feature has its own column. If the feature exists for the item, you could represent that with a `1`. If the feature does not exist for that item, you could represent that with a `0`. A few monsters could be represented as vectors like so:

|          | has_fangs | melts_in_water | hates_sunlight | has_fur |
| -------- | --------- | -------------- | -------------- | ------- |
| vampire  | 1         | 0              | 1              | 0       |
| werewolf | 1         | 0              | 0              | 1       |
| witch    | 0         | 1              | 0              | 0       |



For bag-of-words, instead of monsters you would have documents and the features would be different words. And we don’t just care if a word is present in a document; we want to know how many times it occurred! Turning text into a BoW vector is known as ***feature extraction\*** or ***vectorization\***.

But how do we know which vector index corresponds to which word? When building BoW vectors, we generally create a ***features dictionary\*** of all vocabulary in our training data (usually several documents) mapped to indices.

For example, with “Five fantastic fish flew off to find faraway functions. Maybe find another five fantastic fish?” our dictionary might be:

```python
{'five': 0,
'fantastic': 1,
'fish': 2,
'fly': 3,
'off': 4,
'to': 5,
'find': 6,
'faraway': 7,
'function': 8,
'maybe': 9,
'another': 10}
```

Using this dictionary, we can convert new documents into vectors using a vectorization function. For example, we can take a brand new sentence “Another five fish find another faraway fish.” — ***test data\*** — and convert it to a vector that looks like:

```python
[1, 0, 2, 0, 0, 0, 1, 1, 0, 0, 2]
```

The word ‘another’ appeared twice in the test data. If we look at the feature dictionary for ‘another’, we find that its index is `10`. So when we go back and look at our vector, we’d expect the number at index `10` to be `2`.

<hr>

## Building a Features Dictionary

Now that you know what a bag-of-words vector looks like, you can create a function that builds them!

First, we need a way of generating a features dictionary from a list of training documents. We can build a Python function to do that for us…

### Instructions

**1.**

Define a function `create_features_dictionary()` that takes one argument, `documents`. This will be the list of string documents that we pass in (like `["All the cool fish love to fly high.", "Nobody knows why the fish fly so high.", "Those cool fish sure are spry."]`).

Inside the function, set `features_dictionary` equal to an empty dictionary. This is where we’ll map all of our terms to index numbers. For now, return `features_dictionary` from the function.



**2.**

Above the return statement, merge the `documents` into a string joined together by spaces and assign the result to `merged`.

Now that the documents are all in a single string, call `preprocess_text()` on `merged` and assign the result to `tokens`. Return `tokens` from the function in addition to `features_dictionary`.



**3.**

Above the return statement, assign `index` a value of `0`. This will correspond to the first word’s vector index.



**4.**

The words are prepared, the empty dictionary is prepared, and we have an index number we can use; it’s time to get the words into the dictionary and link each to a vector index number!

- Above the `return`, loop through each `token` in `tokens`.
- In the loop, check if `token` is **NOT** in `features_dictionary`.
- If it’s a new word, add `token` as a key to `features_dictionary` with a value of `index`.



**5.**

After adding `token` to `features_dictionary`, increment `index` by `1` so that each new word has its own index.



**6.**

Uncomment the print statement to test out the function!

```python
from preprocessing import preprocess_text

# Define create_features_dictionary() below:
def create_features_dictionary(documents):
  features_dictionary = {}
  merged = ' '.join(documents)
  tokens = preprocess_text(merged)
  index = 0
  for token in tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary, tokens

training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]

print(create_features_dictionary(training_documents)[0])
```

`{'five': 0, 'fantastic': 1, 'fish': 2, 'fly': 3, 'off': 4, 'to': 5, 'find': 6, 'faraway': 7, 'function': 8, 'maybe': 9, 'another': 10, 'my': 11, 'with': 12, 'a': 13, 'please': 14}`

<hr>



## Building a BoW Vector

Nice work! Time to put that dictionary of vocabulary to good use and build a bag-of-words vector from a new document.

In Python, we can use a list to represent a vector. Each index in the list will correspond to a word and be set to its count.

![features dictionary of words 'all, my, fish, fly, away, help, me' transforms the string 'help my fly fish fly away' into the vector [0,1,1,2,1,1,0]](https://content.codecademy.com/courses/NLP/Building_vector.gif)

### Instructions

**1.**

Define a function `text_to_bow_vector()` with two parameters:

- `some_text` (the document we pass in to vectorize)
- `features_dictionary` (the dictionary of vocabulary we generated in the previous exercise)

Create a list of `0`s the length of `features_dictionary` and assign it to the variable `bow_vector`. Each `0` represents a word’s count within the vector.

Return `bow_vector` from the function.



**2.**

Above the return statement, preprocess the `some_text` document using the `preprocess_text()` function we built for you and assign the result to the variable `tokens`. Add `tokens` as a second return value for the function.



**3.**

Still above the return statement, loop through each `token` in `tokens`.

- Determine which index the `token` has within `features_dictionary` and assign the value to a new variable `feature_index`. (Take a look a the gif. If `token` is the word `fish`, then we would want `feature_index` to be `2`.)
- Now that you have the word’s index, access the word count index within the `bow_vector` and increment that count by `1`.



**4.**

Uncomment the print statement to test out the function!



```python
from preprocessing import preprocess_text
# Define text_to_bow_vector() below:
def text_to_bow_vector(some_text, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  tokens = preprocess_text(some_text)
  for token in tokens:
    feature_index = features_dictionary[token]
    bow_vector[feature_index] += 1
  return bow_vector, tokens

features_dictionary = {'function': 8, 'please': 14, 'find': 6, 'five': 0, 'with': 12, 'fantastic': 1, 'my': 11, 'another': 10, 'a': 13, 'maybe': 9, 'to': 5, 'off': 4, 'faraway': 7, 'fish': 2, 'fly': 3}

text = "Another five fish find another faraway fish."
print(text_to_bow_vector(text, features_dictionary)[0])
```

`[1, 0, 2, 0, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0]`





<hr>



## It's All in the Bag

Phew! That was a lot of work.

It’s time to put `create_features_dictionary()` and `tokens_to_bow_vector()` together and use them in a spam filter we created that uses a Naive Bayes classifier. We’ve slightly modified the two functions for this use case, but they should still look familiar.

Let’s see `create_features_dictionary()` and `tokens_to_bow_vector()` in action with real test data, helping fend off spam!



### Instructions

**1.**

Below `tokens_to_bow_vector()`, call `create_features_dictionary()` on `training_doc_tokens` and assign the result to `bow_sms_dictionary`.



**2.**

Define `training_vectors` as a list comprehension. The list comprehension should call `tokens_to_bow_vector()` on `training_doc` and `bow_sms_dictionary` for each `training_doc` in `training_spam_docs`.



**3.**

Define `test_vectors` as a list comprehension that calls `tokens_to_bow_vector()` on `test_doc` and `bow_sms_dictionary` for each `test_doc` in `test_spam_docs`.



**4.**

Ready? Get set! Uncomment the code at the bottom of **script.py** and run the code again!

The Naive Bayes classifier was pretty darn accurate in determining which messages were spam by using your bag-of-words functions!

```python
from spam_data import training_spam_docs, training_doc_tokens, training_labels, test_labels, test_spam_docs, training_docs, test_docs
from sklearn.naive_bayes import MultinomialNB

def create_features_dictionary(document_tokens):
  features_dictionary = {}
  index = 0
  for token in document_tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary

def tokens_to_bow_vector(document_tokens, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  for token in document_tokens:
    if token in features_dictionary:
      feature_index = features_dictionary[token]
      bow_vector[feature_index] += 1
  return bow_vector

# Define bow_sms_dictionary:
bow_sms_dictionary = create_features_dictionary(training_doc_tokens)

# Define training_vectors:
training_vectors = [tokens_to_bow_vector(training_doc, bow_sms_dictionary) for training_doc in training_spam_docs]

# Define test_vectors:
test_vectors = [tokens_to_bow_vector(test_doc, bow_sms_dictionary) for test_doc in test_spam_docs]


spam_classifier = MultinomialNB()

def spam_or_not(label):
  return "spam" if label else "not spam"

# Uncomment the code below when you're done:
spam_classifier.fit(training_vectors, training_labels)

predictions = spam_classifier.score(test_vectors, test_labels)

print("The predictions for the test data were {0}% accurate.\n\nFor example, '{1}' was classified as {2}.\n\nMeanwhile, '{3}' was classified as {4}.".format(predictions * 100, test_docs[0], spam_or_not(test_labels[0]), test_docs[10], spam_or_not(test_labels[10])))
```

```
The predictions for the test data were 99.0% accurate.

For example, 'well obviously not because all the people in my cool college life go home _' was classified as not spam.

Meanwhile, 'urgent we be try to contact you last weekend draw show u have win a 1000 prize guarantee call 09064017295 claim code k52 valid 12hrs 150p pm' was classified as spam.
```





<hr>



## Spam A Lot No More

Amazing work! As is the case with many tasks in Python, there’s already a library that can do all of that work for you.

For `text_to_bow()`, you can approximate the functionality with the `collections` module’s `Counter()` function:

```python
from collections import Counter

tokens = ['another', 'five', 'fish', 'find', 'another', 'faraway', 'fish']
print(Counter(tokens))

# Counter({'fish': 2, 'another': 2, 'find': 1, 'five': 1, 'faraway': 1})
```

For vectorization, you can use `CountVectorizer` from the machine learning library `scikit-learn`. You can use `fit()` to train the features dictionary and then `transform()` to transform text into a vector:

```python
from sklearn.feature_extraction.text import CountVectorizer

training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]
test_text = ["Another five fish find another faraway fish."]
bow_vectorizer = CountVectorizer()
bow_vectorizer.fit(training_documents)
bow_vector = bow_vectorizer.transform(test_text)
print(bow_vector.toarray())
# [[2 0 1 1 2 1 0 0 0 0 0 0 0 0 0]]
```



### Instructions

**1.**

Now, let’s see how scikit-learn stacks up with the same bag-of-words functionality! Import `CountVectorizer` from `sklearn`. (Check out the example we gave for how to import `CountVectorizer`.)



**2.**

Define `bow_vectorizer` as our vectorizer using `CountVectorizer()`.



**3.**

Define `training_vectors` as `bow_vectorizer.fit_transform()` called on `training_docs`.

`fit_transform()` does two things: creation of the features dictionary and the vectorization of the training data.

Define `test_vectors` as `bow_vectorizer.transform()` called on `test_docs`.



**4.**

Uncomment the code at the bottom of **script.py**. Run the code again to see why it makes sense to use `sklearn`‘s optimized functions!

```python
from spam_data import training_spam_docs, training_doc_tokens, training_labels, test_labels, test_spam_docs, training_docs, test_docs
from sklearn.naive_bayes import MultinomialNB

# Import CountVectorizer from sklearn:
from sklearn.feature_extraction.text import CountVectorizer


# Define bow_vectorizer:
bow_vectorizer = CountVectorizer()


# Define training_vectors:
training_vectors = bow_vectorizer.fit_transform(training_docs)


# Define test_vectors:
test_vectors = bow_vectorizer.transform(test_docs)

spam_classifier = MultinomialNB()

def spam_or_not(label):
  return "spam" if label else "not spam"

# Uncomment the code below when you're done:
spam_classifier.fit(training_vectors, training_labels)

predictions = spam_classifier.score(test_vectors, test_labels)

print("The predictions for the test data were {0}% accurate.\n\nFor example, '{1}' was classified as {2}.\n\nMeanwhile, '{3}' was classified as {4}.".format(predictions * 100, test_docs[7], spam_or_not(test_labels[7]), test_docs[15], spam_or_not(test_labels[15])))
```



```
The predictions for the test data were 100.0% accurate.

For example, 'really do hope the work doesnt get stressful have a gr8 day' was classified as not spam.

Meanwhile, '2p per min to call germany 08448350055 from your bt line just 2p per min check planettalkinstant com for info t s c s text stop to opt out' was classified as spam.
```



<hr>







<hr>

