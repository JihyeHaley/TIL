# #2 Python :computer:

# 모듈 / 함수 / 라이브러리 (공적마스크 api)

**random 공식문서 url**

https://docs.python.org/ko/3.7/library/random.html



## Functions for sequences

- `random.choice`(*seq*)

  Return a random element from the non-empty sequence *seq*. If *seq* is empty, raises [`IndexError`](https://docs.python.org/ko/3.7/library/exceptions.html#IndexError).

- `random.``sample`(*population*, *k*)

  Return a *k* length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.

  Returns a new list containing elements from the population while leaving the original population unchanged. The resulting list is in selection order so that all sub-slices will also be valid random samples. This allows raffle winners (the sample) to be partitioned into grand prize and second place winners (the subslices).

  Members of the population need not be [hashable](https://docs.python.org/ko/3.7/glossary.html#term-hashable) or unique. If the population contains repeats, then each occurrence is a possible selection in the sample.

  To choose a sample from a range of integers, use a [`range()`](https://docs.python.org/ko/3.7/library/stdtypes.html#range) object as an argument. This is especially fast and space efficient for sampling from a large population: `sample(range(10000000), k=60)`.

  If the sample size is larger than the population size, a [`ValueError`](https://docs.python.org/ko/3.7/library/exceptions.html#ValueError) is raised.

- `random.``randrange`(*stop*)

  `random.``randrange`(*start*, *stop*[, *step*])

  Return a randomly selected element from `range(start, stop, step)`. This is equivalent to `choice(range(start, stop, step))`, but doesn’t actually build a range object.

  The positional argument pattern matches that of [`range()`](https://docs.python.org/ko/3.7/library/stdtypes.html#range). Keyword arguments should not be used because the function may use them in unexpected ways.

  *버전 3.2에서 변경:* [`randrange()`](https://docs.python.org/ko/3.7/library/random.html#random.randrange) is more sophisticated about producing equally distributed values. Formerly it used a style like `int(random()*n)` which could produce slightly uneven distributions.







요청, 응답