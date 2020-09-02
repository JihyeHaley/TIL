# Write your reverse_string function here:
def reverse_string(word):
  word_return = ''
  print(list(range(len(word), 0, -1)))
  for i in range(len(word), 0, -1):
    word_return += word[i-1]
  return word_return
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

