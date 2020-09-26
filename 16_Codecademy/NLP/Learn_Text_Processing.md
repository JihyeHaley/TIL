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

