#!/usr/bin/env python
# coding: utf-8

# In[19]:


import itertools
import numpy as np
import pandas as pd

population = [9, 12, 15]
samples = list(itertools.product(population, repeat=2))
data = []

for sample in samples:
    sample_mean = np.mean(sample)
    p_xbar = 1 / len(samples)
    xbar_p = sample_mean * p_xbar
    xbar2_p = sample_mean ** 2 * p_xbar
    data.append([sample[0], sample[1], sample_mean, p_xbar, xbar_p, xbar2_p])

df = pd.DataFrame(data, columns=['A (Value 1)', 'B (Value 2)', 'C (Sample Mean)', 'D (p(x̄))', 'E (x̄ * p(x̄))', 'F (x̄² * p(x̄))'])

styled_df = df.style.set_table_styles([
    {'selector': 'th', 'props': [('text-align', 'center')]}, 
    {'selector': 'td', 'props': [('text-align', 'center')]} 
]).set_properties(**{'text-align': 'center'}) 

styled_df


# In[22]:


# The table above reveals that each combination has an equal probability of occurrence, and each mean contributes to the overall expected value and variance, demonstrating how different sample combinations influence the statistical properties of the population.


# In[23]:


import numpy as np
import itertools

population = np.array([3, 7, 11, 15])
population_mean = np.mean(population)
population_std = np.std(population, ddof=0)
samples = list(itertools.product(population, repeat=2))
sample_means = [np.mean(sample) for sample in samples]
sampling_mean = np.mean(sample_means)
sampling_std = np.std(sample_means, ddof=0)
standard_error = population_std / np.sqrt(2)

print(f"(a) Population Mean: {population_mean}")
print(f"(b) Population Standard Deviation: {population_std}")
print(f"(c) Mean of the Sampling Distribution of Means: {sampling_mean}")
print(f"(d) Standard Deviation of the Sampling Distribution of Means: {sampling_std}")
print(f"Verification: Standard Error from population standard deviation: {standard_error}")


# In[24]:


# The data above shows that the population mean and the mean of the sampling distribution of means are equal. 
# The standard deviation is relatively high due to the large disparity of the lowest and highest value on the population while the standard deviation of sampling distribution of means have a lower result thus the means of samples of size 2 have less difference between the highest and lowest values.


# In[25]:


import numpy as np
from scipy.stats import norm

num = 200 
prob = 0.5 
mean = num * prob 
stddev = np.sqrt(num * prob * (1 - prob)) 

#a
x_a = 0.4 * num
z_a = (x_a - mean) / stddev
p_a = norm.cdf(z_a)

#b
x_b1 = 0.43 * num
x_b2 = 0.57 * num
z_b1 = (x_b1 - mean) / stddev
z_b2 = (x_b2 - mean) / stddev
p_b = norm.cdf(z_b2) - norm.cdf(z_b1)

#c
x_c = 0.54 * num
z_c = (x_c - mean) / stddev
p_c = 1 - norm.cdf(z_c)

print(f"(a) Probability that less than 40% will be boys: {p_a:.4f}")
print(f"(b) Probability that between 43% and 57% will be girls: {p_b:.4f}")
print(f"(c) Probability that more than 54% will be boys: {p_c:.4f}")


# In[26]:


# The data above shows that the likelihood that there would be less than 40% boys born for the next 200 babies considering that there are equal probabilities of it being a boy or a girl is just 0.23% while for it to be 54% boys is a bit higher at 12.89%. On the other hand, it is very much likely that there would be 43% to 57% girls with 95.23% possibility


# In[27]:


import numpy as np
import itertools
import pandas as pd

x_values = np.array([6, 9, 12, 15, 18])
p_values = np.array([0.1, 0.2, 0.4, 0.2, 0.1])
population_mean = np.sum(x_values * p_values)
population_variance = np.sum((x_values - population_mean)**2 * p_values)
samples = list(itertools.product(x_values, repeat=2))
sample_means = [(x1 + x2) / 2 for x1, x2 in samples]
sample_probs = [p_values[np.where(x_values == x1)[0][0]] * p_values[np.where(x_values == x2)[0][0]] for x1, x2 in samples]

df = pd.DataFrame(samples, columns=['x1', 'x2'])
df['mean'] = sample_means
df['probability'] = sample_probs

print(f"Population Mean (μ): {population_mean}")
print(f"Population Variance (σ²): {population_variance}")
df


# In[28]:


# The results above showcases the population mean of 12 and a variance of 10.8 which is somewhat high as 6 and 18 are a bit far from each other.
# The table reveals the mean of samples of size 2 and the probabilities of each sample occuring based on the given probability of each number.

