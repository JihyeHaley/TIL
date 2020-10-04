## Introduction

It’s a dark night in the middle of winter as you make your way through another of Emily Dickinson’s poems. As you grapple with questions of immortality and death, you notice the word choice in each poem you read. With each passing poem, you discover for yourself which words are common throughout her work, and which indicate more unique meaning in individual poems.

You might not even realize, but you are building a language model in your head similar to ***term frequency-inverse document frequency\***, commonly known as ***tf-idf\***. Tf-idf is another powerful tool in your NLP toolkit that has a variety of use cases included:

- ranking results in a search engine
- text summarization
- building smarter chatbots



### Instructions

The gif on the right showcases an example of applying tf-idf to a set of documents. The output of applying tf-idf is the table shown, also known as a term-document matrix. You can think of a term-document matrix like a matrix of bag-of-word vectors.

Each column of the table represents a unique document (in this case, an individual sentence). Each row represents a unique word token. The value in each cell represents the tf-idf score for a word token in that particular document.

Proceed to the next exercise to learn more about what tf-idf is and how you can calculate it!



<hr>



## What is Tf-idf?

*Term frequency-inverse document frequency* is a numerical statistic used to indicate how important a word is to each document in a collection of documents, or a corpus.

When applying tf-idf to a corpus, each word is given a tf-idf score for each document, representing the relevance of that word to the particular document. A higher tf-idf score indicates a term is more important to the corresponding document.

Tf-idf has many similarities with the [bag-of-words language model](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-bag-of-words/exercises/intro-to-bag-of-words), which if you recall is concerned with word count — how many times each word appears in a document.

While tf-idf can be used in any situation bag-of-words can be used, there is a key difference in how it is calculated.

Tf-idf relies on two different metrics in order to come up with an overall score:

- *term frequency*, or how often a word appears in a document. This is the same as bag-of-words’ word count.
- *inverse document frequency*, which is a measure of how often a word appears in the overall corpus. By penalizing the score of words that appear throughout a corpus, tf-idf can give better insight into how important a word is to a particular document of a corpus.

We will dig into each component of tf-idf in the next two exercises.



#### Instructions

**1.**

The code in **script.py** is used to apply tf-idf to a corpus of documents and display the scores as a DataFrame in the web browser component. The current code is incomplete, so the DataFrame is not yet appearing!

Like with many natural language processing tasks, we must preprocess our text data before applying a technique. Paste the below line of code into the “preprocess documents” section of **script.py** to preprocess each document in the corpus. Then run the code.

```python
processed_corpus = [preprocess_text(doc) for doc in corpus]
```



**2.**

You should now see what is known as a *term-document matrix* in the browser. Each row of the table represents a term, and each column of the table represents a document. The value in each cell indicates the tf-idf score for each term-document pair.

Try changing the text in `document_1`, `document_2` and `document_3` and re-running the code. How do the tf-idf values change?





```python
import codecademylib3_seaborn
from preprocessing import preprocess_text
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# sample documents
document_1 = "This was a sample sentence!"
document_2 = "This was my second sentence."
document_3 = "Was this my third sentence?"

# corpus of documents
corpus = [document_1, document_2, document_3]

# preprocess documents
processed_corpus = [preprocess_text(doc) for doc in corpus]
print(processed_corpus)

# initialize and fit TfidfVectorizer
vectorizer = TfidfVectorizer(norm=None)
tf_idf_scores = vectorizer.fit_transform(processed_corpus)

# get vocabulary of terms
feature_names = vectorizer.get_feature_names()
corpus_index = [n for n in processed_corpus]

# create pandas DataFrame with tf-idf scores
df_tf_idf = pd.DataFrame(tf_idf_scores.T.todense(), index=feature_names, columns=corpus_index)
print(df_tf_idf)
```





<hr>



## Breaking It Down Part I: Term Frequency

The first component of tf-idf is *term frequency*, or how often a word appears in a document within the corpus.

The value for the term frequency is the same as if applying the bag-of-words language model to a document. If you have previously studied bag-of-words, this will all be familiar! If not, have no fear.

Term frequency indicates how often each word appears in the document. The intuition for including term frequency in the tf-idf calculation is that the more frequently a word appears in a single document, the more important that term is to the document.

Consider the stanza from Emily Dickinson’s poem *I’m Nobody! Who are you?* below:

```python
stanza = '''I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us — don't tell!
They'd banish us, you know.'''
```

The term frequency for “you” is `3`, “nobody” is `2`, “are” is `2`, “us” is `2`, and the rest of the terms have a frequency of `1`. We can get a general sense of what this stanza is about by the most frequently used words.

Term frequency can be calculated in Python using scikit-learn’s `CountVectorizer`, as shown below:

```python
vectorizer = CountVectorizer()

term_frequencies = vectorizer.fit_transform([stanza])
```

- A `CountVectorizer` object is initialized
- The `CountVectorizer` object is fit (trained) and transformed (applied) on the corpus of data, returning the term frequencies for each term-document pair



### Instructions

**1.**

Provided in **script.py** is Emily Dickinson’s poem *Success is counted sweetest*, stored in the variable `poem`. Read through `poem` yourself and find the term-frequency of “clear”. Save your answer, as an integer, to a variable named `clear_count`.



**2.**

Reading through each word of a document to count how many times it appears isn’t too efficient.

The code in **script.py** preprocesses the poem and then uses scikit-learn’s `CountVectorizer` to get the term-frequencies for all terms in `poem`. It’s currently missing one line of code to display the term-document matrix of term-frequencies.

`CountVectorizer` objects have a `.get_feature_names()` method which returns a list of all the unique terms in the corpus.

Paste the below line into the “get vocabulary of terms” section of **script.py** to display the term-frequencies matrix.

```python
feature_names = vectorizer.get_feature_names()
```

Which term appears the most frequently?



```python
import codecademylib3_seaborn
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import preprocess_text

poem = '''
Success is counted sweetest
By those who ne'er succeed.
To comprehend a nectar
Requires sorest need.

Not one of all the purple host
Who took the flag to-day
Can tell the definition,
So clear, of victory,

As he, defeated, dying,
On whose forbidden ear
The distant strains of triumph
Break, agonized and clear!'''

# define clear_count:
clear_count = 3

# preprocess text
processed_poem = preprocess_text(poem)

# initialize and fit CountVectorizer
vectorizer = CountVectorizer()
term_frequencies = vectorizer.fit_transform([processed_poem])

# get vocabulary of terms
feature_names = vectorizer.get_feature_names()

# create pandas DataFrame with term frequencies
try:
  df_term_frequencies = pd.DataFrame(term_frequencies.T.todense(), index=feature_names, columns=['Term Frequency'])
  print(df_term_frequencies)
except:
  pass
```

