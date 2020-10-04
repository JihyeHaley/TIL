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





## What is Tf-idf?

*Term frequency-inverse document frequency* is a numerical statistic used to indicate how important a word is to each document in a collection of documents, or a corpus.

When applying tf-idf to a corpus, each word is given a tf-idf score for each document, representing the relevance of that word to the particular document. A higher tf-idf score indicates a term is more important to the corresponding document.

Tf-idf has many similarities with the [bag-of-words language model](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-bag-of-words/exercises/intro-to-bag-of-words), which if you recall is concerned with word count — how many times each word appears in a document.

While tf-idf can be used in any situation bag-of-words can be used, there is a key difference in how it is calculated.

Tf-idf relies on two different metrics in order to come up with an overall score:

- *term frequency*, or how often a word appears in a document. This is the same as bag-of-words’ word count.
- *inverse document frequency*, which is a measure of how often a word appears in the overall corpus. By penalizing the score of words that appear throughout a corpus, tf-idf can give better insight into how important a word is to a particular document of a corpus.

We will dig into each component of tf-idf in the next two exercises.