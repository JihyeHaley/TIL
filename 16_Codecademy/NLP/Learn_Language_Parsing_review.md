## Review

And there you go! Now you have the toolkit to dig into any piece of text data and perform natural language parsing with regular expressions. What insights will you gain, or what bias may you uncover? Let’s review what you have learned:

- The `re` module’s `.compile()` and `.match()` methods allow you to enter any regex pattern and look for a single match at the beginning of a piece of text
- The `re` module’s `.search()` method lets you find a single match to a regex pattern anywhere in a string, while the `.findall()` method finds all the matches of a regex pattern in a string
- *Part-of-speech tagging* identifies and labels the part of speech of words in a sentence, and can be performed in `nltk` using the `pos_tag()` function
- *Chunking* groups together patterns of words by their part-of-speech tag. Chunking can be performed in `nltk` by defining a piece of chunk grammar using regular expression syntax and calling a `RegexpParser`‘s `.parse()` method on a word tokenized sentence
- *NP-chunking* chunks together an optional determiner `DT`, any number of adjectives `JJ`, and a noun `NN` to form a noun phrase. The frequency of different NP-chunks can identify important topics in a text or demonstrate how an author describes different subjects
- *VP-chunking* chunks together a verb `VB`, a noun phrase, and an optional adverb `RB` to form a verb phrase. The frequency of different VP-chunks can give insight into what kind of action different subjects take or how the actions that different subjects take are described by an author, potentially indicating bias
- *Chunk filtering* provides an alternative means of chunking by specifying what parts of speech you do not want in a chunk and removing them



### Instructions

The code in the workspace is set up to perform natural language parsing on *The Wonderful Wizard of Oz*. However, the chunk grammar is empty! Instead of finding NP-chunks or VP-chunks, define your own chunk grammar using regular expressions in between the curly braces `{}`. Feel free to add any chunk filtering in between the inverted braces `}{` if you so desire!

Run the code and observe the frequencies of the chunks. What insights or knowledge do the chunk frequencies give you? Have you come to any different conclusions than from analyzing the NP-chunks and VP-chunks?



```PYTHON
from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

# import text of choice here
text = open('dorian_gray.txt', encoding='utf-8').read().lower()

# sentence and word tokenize text here
word_tokenized_text = word_sentence_tokenize(text)

# store and print any word tokenized sentence here
single_word_tokenized_sentence = word_tokenized_text[0]
print(single_word_tokenized_sentence)

# create a list to hold part-of-speech tagged sentences here
pos_tagged_text = list()

# create a for loop through each word tokenized sentence here
for wtt in word_tokenized_text:
  # part-of-speech tag each sentence and append to list of pos-tagged sentences here
  pos_tagged_text.append(pos_tag(wtt))
  

# store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tagged_text[100]
print(single_pos_sentence)

# define noun phrase chunk grammar here
np_chunk_grammar = 'NP: {<DT>?<JJ>*<NN>}'

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)

np_chunk_text = list()
for ppt in pos_tagged_text:
  np_chunk_text.append(np_chunk_parser.parse(ppt))

# define verb phrase chunk grammar here
vp_chunk_grammar = 'VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}'

# create verb phrase RegexpParser object here
vp_chunk_parser = RegexpParser(vp_chunk_grammar)


# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
vp_chunked_text = list()

# create a for loop through each pos-tagged sentence here
for ptt in pos_tagged_text: 
  # chunk each sentence and append to lists here
  vp_chunked_text.append(vp_chunk_parser.parse(ptt))
  

# store and print the most common NP-chunks here

most_commom_np_chunks = np_chunk_counter(np_chunk_text)

# store and print the most common VP-chunks here

most_commom_vp_chunks = vp_chunk_counter(vp_chunked_text)

```

