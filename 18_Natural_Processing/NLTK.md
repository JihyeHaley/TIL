# NLTK

 

#### Text Preprocessing

**Noise removal** — stripping text of formatting (e.g., HTML tags).

**Tokenization** — breaking text into individual words.

**Normalization** — cleaning text data in any other way:

- **Stemming** is a blunt axe to chop off word prefixes and suffixes. “booing” and “booed” become “boo”, but “sing” may become “s” and “sung” would remain “sung.”
- **Lemmatization** is a scalpel to bring words down to their root forms. For example, NLTK’s savvy lemmatizer knows “am” and “are” are related to “be.”
- Other common tasks include lowercasing, [stopwords](https://en.wikipedia.org/wiki/Stop_words) removal, spelling correction, etc.





####  Parsing Text

**Part-of-speech tagging (POS tagging)** identifies parts of speech (verbs, nouns, adjectives, etc.). NLTK can do it faster (and maybe more accurately) than your grammar teacher.

**Named entity recognition (NER)** helps identify the proper nouns (e.g., “Natalia” or “Berlin”) in a text. This can be a clue as to the topic of the text and NLTK captures many for you.

**Dependency grammar** trees help you understand the relationship between the words in a sentence. It can be a tedious task for a human, so the Python library spaCy is at your service, even if it isn’t always perfect.



#### Language Models - Bag-of-Words Approach

**Language models** are probabilistic computer models of language. We build and use these models to figure out the likelihood that a given sound, letter, word, or phrase will be used. Once a model has been trained, it can be tested out on new texts.