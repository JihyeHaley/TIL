# ONE-SAMPLE T-TESTS IN SCIPY

### Assumptions of a One Sample T-Test

When running any hypothesis test, it is important to know and verify the assumptions of the test. The assumptions of a one-sample t-test are as follows:

- The sample was randomly selected from the population
  - For example, if you only collect data for site visitors who agree to share their personal information, this subset of visitors was not randomly selected and may differ from the larger population.
- The individual observations were independent
  - For example, if one visitor to BuyPie loves the apple pie they bought so much that they convinced their friend to buy one too, those observations were not independent.
- The data is normally distributed without outliers OR the sample size is large (enough)
  - There are no set rules on what a “large enough” sample size is, but a common threshold is around 40. For sample sizes smaller than 40, and really all samples in general, it’s a good idea to make sure to plot a histogram of your data and check for outliers, multi-modal distributions (with multiple humps), or skewed distributions. If you see any of those things for a small sample, a t-test is probably not appropriate.

In general, if you run an experiment that violates (or possibly violates) one of these assumptions, you can still run the test and report the results — but you should also report assumptions that were not met and acknowledge that the test results could be flawed.

```ptyhon
import codecademylib3
import numpy as np
import matplotlib.pyplot as plt

prices = np.genfromtxt("prices.csv")
print(prices)
#plot your histogram here


plt.hist(prices)
plt.show()
```





### Review

Congratulations! You now know how to implement a one-sample t-test in Python and verify the assumptions of the test. To recap, here are some of the things you learned:

- One-sample t-tests are used for comparing a sample mean to an expected population mean
- A one-sample t-test can be implemented in Python using the SciPy `ttest_1samp()` function
- Assumptions of a one-sample t-test include:
  - The sample was randomly drawn from the population of interest
  - The observations in the sample are independent
  - The sample size is large “enough” or the sample data is normally distributed



### Instructions

As a final exercise, some data has been loaded for you with purchase prices for consecutive days at BuyPie. You can access the first day using `daily_prices[0]`, the second using `daily_prices[1]`, etc.. To practice running a one-sample t-test and inspecting the resulting p-value, try the following:



As a final exercise, some data has been loaded for you with purchase prices for consecutive days at BuyPie. You can access the first day using `daily_prices[0]`, the second using `daily_prices[1]`, etc.. To practice running a one-sample t-test and inspecting the resulting p-value, try the following:

1. Calculate and print out a p-value for day 1 where the null hypothesis is that the average purchase price was 1000 Rupees and the alternative hypothesis is that the average purchase price was **not** 1000 Rupees. Print out the p-value.
2. Run the same hypothesis tests for days 1-10 (the fastest way to do this is with a for-loop!) and print out the resulting p-values. What’s the smallest p-value you observe for those 10 days?
3. Try changing the null hypothesis so that the expected population mean that you’re testing against is **different** from 1000. Try any numbers that you want. How do your p-values change?

Solution code can be found in **solution.py**

```python
from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")

# day 1:
# tstat, pval = ttest_1samp(daily_prices[0], 1000)
# print("day 1 p-value:", pval)


# 10 days:
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 1000)
  print("day",i+1, "p-value:")
  if pval < 0.05:
    print(f'\t*{pval}, it is significnt')
  else:
    print(f'\t{pval}, it is not significant')

# 10 days with a different null hypothesis
print("day 1-10 with a different alternative hypothesis:")
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 1000)
  print("day",i+1, "p-value:")
  if pval < 0.05:
      print(f'\t*{pval}, it is significnt')
  else:
     print(f'\t{pval}, it is not significant')
```



### Summarizing the Sample

The marketing department at Live-it-LIVE reports that, during this time of year, about 10% of visitors to Live-it-LIVE.com make a purchase.

The monthly report shows every visitor to the site and whether or not they made a purchase. The checkout page had a small bug this month, so the business department wants to know whether the purchase rate dipped below expectation. They’ve asked us to investigate this question.

In order to run a hypothesis test to address this, we’ll first need to know two things from the data:

- The number of people who visited the website
- The number of people who made a purchase on the website

Assuming each row of our dataset represents a unique site visitor, we can calculate the number of people who visited the website by finding the number of rows in the data frame. We can then find the number who made a purchase by using a conditional statement to add up the total number of rows where a purchase was made.

For example, suppose that the dataset `candy` contains a column named `chocolate` with `'yes'` recorded for every candy that has chocolate in it and `'no'` otherwise. The following code calculates the sample size (the number of candies) and the number of those candies that contain chocolate:

```python
## sample size (number of rows): 
samp_size = len(candy)

## number with chocolate: 
total_with_chocolate = np.sum(candy.chocolate == 'yes')
```





#### Introdution 

**1.**

Each row of the dataset `monthly_report` represents a single visitor to Live-it-LIVE.com during the week in question. Use `.head()` to print the first five rows of the data once again and inspect the `'purchase'` column. What are the values and how can you tell whether someone made a purchase?

Note that this will print in both the output terminal and the web browser, but it will look nicer and be easier to read in the web browser.



**2.**

Calculate the sample size and assign it to a variable named `sample_size`. Print `sample_size`. How many visitors accessed the website this week?

Note that this will print to the output terminal, not the web browser.



**3.**

Calculate the number of visitors who made a purchase this week and save it to a variable named `num_purchased`. Print `num_purchased`. How many visitors made a purchase this week?

Note that this will print to the output terminal, not the web browser.

```python
import numpy as np
import pandas as pd
import codecademylib3

monthly_report = pd.read_csv('monthly_report.csv')

#print the head of monthly_report:
print(monthly_report.head())

#calculate and print sample_size:
sample_size = len(monthly_report)
print(sample_size)

#calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase=='y')
print(num_purchased)

```





<hr>



### Simulating Randomness

In the last exercise, we calculated that there were 500 site visitors to live-it-LIVE.com this month and 41 of them made a purchase. In comparison, if each of the 500 visitors had a 10% chance of making a purchase, we would expect around 50 of those visitors to buy something. Is 41 different enough from 50 that we should question whether this months’ site visitors really had a 10% chance of making a purchase?

To conceptualize why our **expectation** (50) and **observation** (41) might not be equal — EVEN IF there was no dip in the purchase probability — let’s turn to a common probability example: flipping a fair coin. We can simulate a coin flip in Python using the `numpy.random.choice()` function:

```python
flip = np.random.choice(['heads', 'tails'], size=1, p=[0.5, 0.5])
print(flip) 
## output is either ['heads'] or ['tails']
```

If we run this code (or flip a real coin) a few times, we’ll find that — just like we can’t know ahead of time whether any single visitor to Live-it-LIVE.com will make a purchase — we can’t predict the outcome of any individual coin flip.

If we flip a fair coin 10 times in a row, we expect about 5 of those coins to come up heads (50%). We can simulate this in python by changing the `size` parameter of `numpy.random.choice()`:

```python
flip = np.random.choice(['heads', 'tails'], size=10, p=[0.5, 0.5])
print(flip)
## output is something like: ['heads' 'heads' 'heads' 'tails' 'tails' 'heads' 'heads' 'tails' 'heads' 'heads']
```

If you try this yourself, it’s perfectly reasonable that you’ll get only four heads, or maybe six or seven! Because this is a random process, we can’t guarantee that exactly half of our coin flips will come up heads. Similarly, even if each Live-it-LIVE visitor has a 10% chance of making a purchase, that doesn’t mean we expect **exactly** 10% to do so in any given sample.



#### Instructions

**1.**

In **script.py**, use the `random.choice()` function from NumPy to simulate a single visitor to Live-it-LIVE.com, who has a 10% chance of making a purchase (p=0.1). Save the outcome as a variable named `one_visitor` and print it. If the visitor made a purchase, the value of `one_visitor` should be `['y']`; if they did not make a purchase, it should be `['n']` (just like in the original data!).

Did that one simulated visitor make a purchase? Try pressing “Run” a few more times and see if you ever observe a different outcome. (Note that you’ll see an error for the next checkpoint if you press run a few times; don’t worry about that!).

Stuck? Get a hint

**2.**

Now, create a new list named `simulated_monthly_visitors`, which contains the randomly-generated outcomes for 500 visitors to Live-it-LIVE.com (still with a 10% chance of a purchase). Print `simulated_monthly_visitors` out. Do you see any visitors in this list who made a purchase?



```python
import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')
print(monthly_report)


#simulate one visitor:
one_visitor = np.random.choice(['y', 'n'], size=1, p=[0.1, 0.9])
print(one_visitor)

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
print(simulated_monthly_visitors)
```





<hr>

### Simulating the Null Distribution I

The first step in running a hypothesis test is to form a *null hypothesis*. For the question of whether the purchase rate at Live-it-LIVE.com was different from 10% this month, the null hypothesis describes a world in which the true probability of a visitor making a purchase was exactly 10%, but by random chance, we observed that only 41 visitors (8.2%) made a purchase.

Let’s return to the coin flip example from the previous exercise. We can simulate 10 coin flips and print out the number of those flips that came up heads using the following code:

```python
flips = np.random.choice(['heads', 'tails'], size=10, p=[0.5, 0.5])
num_heads = np.sum(flips == 'heads')
print(num_heads)
## output: 4
```

If we run this code a few times, we’ll likely see different results each time. This will give us get a sense for the range in the number of heads that could occur by random chance, even if the coin is fair. We’re more likely to see numbers like four, five, or six, but maybe we’ll see something more extreme every once in a while — ten heads in a row, or even zero!

#####  Introduction 

###### 1. 

In **script.py**, you’ll see the code we used in the previous exercise to generate `simulated_monthly_visitors`, a list of 500 simulated outcomes, `'y'` (with probability 0.1) or `'n'`, indicating whether each imaginary site visitor made a purchase.

Add a line of code to calculate the number of those simulated visitors who made a purchase. Save the result as `num_purchased` and print it out.

###### 2.

Inspect the value of `num_purchased` from the previous instruction. Is it close to 50 (which is what we would expect for a purchase probability of 10%)? Less than? Greater than? Now try pressing “Run” a few more times and see what other values of `num_purchased` you observe. What’s the farthest number from 50 that you observe after pressing “Run” 5 times?

```python
import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')
print(len(monthly_report))
#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

#calculate the number of simulated visitors who made a purchase:

num_purchased = np.sum(simulated_monthly_visitors=='y')
print(num_purchased)

```





<hr>



### Simulating the Null Distribution II

In the last exercise, we simulated a random sample of 500 visitors, where each visitor had a 10% chance of making a purchase. When we pressed “Run” a few times, we saw that the number of purchases varied from sample to sample, but was **around** 50.

Similarly, we simulated a single random sample of 10 coin flips, where each flip had a 50% chance of coming up heads. We saw that the number of simulated heads was not necessarily 5, but somewhere around 5.

By running the same simulated experiment **many** times, we can get a sense for how much a particular outcome (like the number of purchases, or heads) varies by random chance. Consider the following code:

```python
outcomes = []
for i in range(10000): 
    flips = np.random.choice(['heads', 'tails'], size=10, p=[0.5, 0.5])
    num_heads = np.sum(flips == 'heads')
    outcomes.append(num_heads)
print(outcomes)
## output is something like: [3, 4, 5, 8, 5, 6, 4, 5, 3, 2, 8, 5, 7, 4, 4, 5, 4, 3, 6, 5,...]
```

In this code chunk, we’ve done the following:

- initialized an empty list named `outcomes` to store the number of ‘heads’ from simulated samples of coin flips
- set up a for-loop to repeat the steps below 10000 times:
  - flip a fair coin 10 times
  - calculate the number of those 10 flips that came up heads
  - append that number onto `outcomes`

Note that 10000 is an arbitrarily chosen large number — it’s big enough that it will yield almost all possible outcomes of our experiment, and small enough that the simulation still runs quickly. From inspecting the output, we can see that the number of ‘heads’ varied between 0 and 10:

```python
min_heads = np.min(outcomes) 
print(min_heads) #output: 0
 
max_heads = np.max(outcomes)
print(max_heads) #output: 10
```

Thus, if we flip a fair coin 10 times, we could observe anywhere between 0 and 10 heads by random chance.



```python
import numpy as np
import pandas as pd

null_outcomes = []

#start for loop here:
for i in range(10000):
  # week_of_visitors = np.random.choice(['y', 'n'], size = 500, =[0.1, 0.9])
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)


#calculate the minimum and maximum values in null_outcomes here:

null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)

print(f'min: {null_min}')
print(f'max: {null_max}')
```





<hr>



### Inspecting the Null Distribution

In the previous exercise, we simulated 10000 different samples of 500 visitors, where each visitor had a 10% chance of making a purchase, and calculated the number of purchases per sample. Upon further inspection, we saw that those numbers ranged from around 25 to 75. This is useful information, but we can learn even more from inspecting the full distribution.

For example, recall our 10000 coin flip experiments: for each experiment, we flipped a fair coin 10 times and recorded the number of heads in a list named `outcomes`. We can plot a histogram of `outcomes` using `matplotlib.pyplot.hist()`. We can also add a vertical line at any x-value using `matplotlib.pyplot.axvline()`:

```python
import matplotlib.pyplot as plt
plt.hist(outcomes)
plt.axvline(2, color = 'r')
plt.show()
```

This histogram shows us that, over 10000 experiments, we observed as few as 0 and as many as 10 heads out of 10 flips. However, we were most likely to observe around 4-6 heads. It would be unlikely to observe only 2 heads (where the vertical red line is).

##### Introduction

###### 1.

The code from the previous exercise is provided for you in **script.py**. The list `null_outcomes` contains numbers of purchases simulated under the null hypothesis.

Add code to plot a histogram of `null_outcomes` and inspect the plot. What range of values occurs most frequently?

Note that, because we are using simulation, if you press “Run” a few times, the histogram will change slightly each time — but the basic shape and range covered on the x-axis will stay the same.



###### 2.

In the month we’re investigating, we calculated that there were 41 purchases. Add a vertical line to your histogram at 41. Make this line red using `color = 'r'` so that you can see it.

Where does 41 fall in this distribution? Is it relatively likely or unlikely?

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(41, color ='r')
plt.show()
```





<hr>

### Confidence Intervals

So far, we’ve inspected the null distribution and calculated the minimum and maximum values. While the number of purchases in each simulated sample ranged roughly from 25 to 75 by random chance, upon further inspection of the distribution, we saw that those extreme values happened very rarely.

By reporting an interval covering 95% of the values instead of the full range, we can say something like: “we are 95% confident that, if each visitor has a 10% chance of making a purchase, a random sample of 500 visitors will make between 37 and 63 purchases.” We can use the `np.percentile()` function to calculate this 95% interval as follows:

```
np.percentile(outcomes, [2.5,97.5])
# output: [37. 63.]
```

We calculated the 2.5th and 97.5th percentiles so that exactly 5% of the data falls outside those percentiles (2.5% above the 97.5th percentile, and 2.5% below the 2.5th percentile). This leaves us with a range covering 95% of the data.

If our observed statistic falls outside this interval, then we can conclude it is unlikely that the null hypothesis is true. In this example, because 41 falls within the 95% interval (37 - 63), it is still reasonably likely that we observed a lower purchase rate by random chance, even though the null hypothesis was true.



##### Instructions

###### **1.**

The code to generate `null_outcomes` has been provided for you. Calculate an interval covering the middle 90% of the values in `null_outcomes`. Save the output in a variable named `null_90CI` and print it out. Is the observed value of 41 purchases inside or outside this interval?



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the 90% interval here:
null_95CI = np.percentile(null_outcomes, [2.5, 97.5])
null_90CI = np.percentile(null_outcomes, [5, 95])

print(null_95CI)
print(null_90CI)
```



<hr>

### Calculating a One-Sided P-Value

*P-value* calculations and interpretations depend on the *alternative hypothesis* of a test, a description of the difference from expectation that we are interested in.

For example, let’s return to the 10-coin-flip example from earlier. Suppose that we flipped a coin 10 times and observed only 2 heads. We might run a hypothesis test with the following null and alternative hypotheses:

- Null: the probability of heads is 0.5
- Alternative: the probability of heads is **less than** 0.5

This hypothesis test asks the question: IF the probability of heads is 0.5, what’s the probability of observing 2 or fewer heads among a single sample of 10 coin flips?

Earlier, we used a for-loop to repeatedly (10000 times!) flip a fair coin 10 times, and store the number of heads (for each set of 10 flips) in a list named `outcomes`. The probability of observing 2 or fewer heads among 10 coin flips is approximately equal to the proportion of those 10000 experiments where we observed 0, 1, or 2 heads:

```python
import numpy as np
outcomes = np.array(outcomes)
p_value = np.sum(outcomes <= 2)/len(outcomes) 
print(p_value) #output: 0.059
```

This calculation is equivalent to calculating the proportion of this histogram that is colored in red:![null distribution with bars colored red for values less than or equal to 2](https://content.codecademy.com/courses/Hypothesis_Testing/one_sided_coin_flip.svg)

We estimated that the probability of observing 2 or fewer heads is about 0.059 (5.9%). This probability (0.059) is referred to as a *one-sided p-value*.

##### Introduction

###### 1. 

The code you wrote to generate `null_outcomes` is available to you in **script.py**. Use `null_outcomes` to estimate the p-value for a binomial hypothesis test with the following null and alternative hypotheses:

- Null: the probability of a purchase was 10%
- Alternative: the probability of a purchase rate was LESS THAN 10%

In other words, calculate the proportion of values in `null_outcomes` that are less than or equal to 41 (the observed number of purchases that we calculated earlier). Save this number as a variable named `p_value` and print it out.

Try pressing “Run” a few times; You should see slightly different values of `p_value` each time. What do you think the true probability is?



```python
import numpy as np
import pandas as pd

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41)/len(null_outcomes)
print(p_value)
```

<hr>

### Calculating a Two-Sided P-Value

In the previous exercise, we calculated a one-sided p-value. In this exercise, we’ll estimate a p-value for a 2-sided test, which is the default setting for many functions in Python (and other languages, like R!).

In our 10-coin-flip experiment, remember that we observed 2 heads, which is 3 less than the expected value of 5 (50% of 10) if the null hypothesis is true. The two sided test focuses on the number of heads being three **different** from expectation, rather than just **less than**. The hypothesis test now asks the following question:

Suppose that the true probability of heads is 50%. What is the probability of observing **either** two or fewer heads OR eight or more heads? (Note that two and eight are both three away from five). The calculation now estimates the proportion of the null histogram that is colored in red:

![null distribution for 10 coin flips with a probability of heads equal to 0.5, and all bars above x-values <=2 or >=8 are shaded red, illustrating a two-sided hypothesis test](https://content.codecademy.com/courses/Hypothesis_Testing/two_sided_coin_flip.svg)

This proportion can be calculated in Python as follows. Note that the `|` symbol is similar to `'or'`, but works for comparing multiple values at once.

```python
import numpy as np
outcomes = np.array(outcomes)
p_value = np.sum((outcomes <= 2) | (outcomes >= 8))/len(outcomes)
print(p_value) #output: 0.12
```

We end up with a p-value that is twice as large as the one-sided p-value.

##### Introduction

###### 1

The code you wrote to generate `null_outcomes` is available to you in **script.py**. Use `null_outcomes` to calculate the p-value for a two-sided test (alternative hypothesis is that the purchase probability was DIFFERENT FROM 10%). Remember that, if the purchase rate is 10%, we expect 50 of the 500 visitors to make a purchase.

In other words, calculate the proportion of values in `null_outcomes` that are less than or equal to 41 (the number of purchases we observed in our sample, which is 9 fewer than 50) OR greater than or equal to 59 (which is 9 purchases more than 50). Save this number as a variable named `p_value` and print it out.

Again, try pressing run a few times to observe a few different estimates of `p_value`. What do you think the true p-value is for this test?

```python
import numpy as np
import pandas as pd

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))/ len(null_outcomes)
print(p_value)

if p_value <= 0.05:
  print('significant')
elif p_value > 0.05:
  print('not significant')
```

