#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np

grades = [
    (90, 100, 9),
    (80, 89, 32),
    (70, 79, 43),
    (60, 69, 21),
    (50, 59, 11),
    (40, 49, 3),
    (30, 39, 1),
]

all_grades = []

for lower, upper, frequency in grades:
    all_grades.extend(list(range(lower, upper + 1)) * frequency)

Q1 = np.percentile(all_grades, 25)
Q2 = np.percentile(all_grades, 50)
Q3 = np.percentile(all_grades, 75)

print(f"First Quartile: {Q1}")
print(f"Second Quartile (Median): {Q2}")
print(f"Third Quartile: {Q3}")


# In[42]:


mean_stats = 78
std_dev_stats = 8.0

mean_algebra = 73
std_dev_algebra = 7.6

absolute_dispersion_stats = std_dev_stats
absolute_dispersion_algebra = std_dev_algebra

cv_stats = (std_dev_stats / mean_stats) * 100
cv_algebra = (std_dev_algebra / mean_algebra) * 100

print(f"Absolute Dispersion (Standard Deviation):")
print(f"Statistics: {absolute_dispersion_stats}")
print(f"Algebra: {absolute_dispersion_algebra}")
greater_absolute = "Statistics" if absolute_dispersion_stats > absolute_dispersion_algebra else "Algebra"
print(f"Greater Absolute Dispersion: {greater_absolute}")

print(f"\nRelative Dispersion (Coefficient of Variation):")
print(f"Statistics: {cv_stats:.2f}%")
print(f"Algebra: {cv_algebra:.2f}%")
greater_relative = "Statistics" if cv_stats > cv_algebra else "Algebra"
print(f"Greater Relative Dispersion: {greater_relative}")


# In[43]:


import numpy as np

data = np.array([6, 2, 8, 7, 5])

mean = np.mean(data)
std_dev = np.std(data)

z_scores = (data - mean) / std_dev

mean_z = np.mean(z_scores)
std_dev_z = np.std(z_scores)

print(f"Original Data: {data}")
print(f"Mean of Original Data: {mean}")
print(f"Standard Deviation of Original Data: {std_dev}")
print(f"Z-Scores: {z_scores}")
print(f"Mean of Z-Scores: {round(mean_z, 10)}")
print(f"Standard Deviation of Z-Scores: {round(std_dev_z,10)}")


# In[44]:


import numpy as np

masses = np.array([20.48, 35.97, 62.34])
std_devs = np.array([0.21, 0.46, 0.54])

mean_sum = np.mean(masses)
std_dev_sum = np.sqrt(np.sum(std_devs**2))

print(f"Mean of the sum: {mean_sum:.2f} g")
print(f"Standard deviation of the sum: {std_dev_sum:.3f} g")


# In[45]:


import numpy as np
import pandas as pd
from itertools import product

# Given data
x = np.array([6, 9, 12, 15, 18])
p = np.array([0.1, 0.2, 0.4, 0.2, 0.1])

mean = round(np.sum(x * p),10)
variance = np.sum((x - mean) ** 2 * p)
print(f"Mean: {mean}")
print(f"Variance: {variance}")

samples = list(product(x, repeat=2))

results = []
for sample in samples:
    mean_sample = np.mean(sample)
    prob_sample = p[x == sample[0]][0] * p[x == sample[1]][0]
    results.append((sample, mean_sample, prob_sample))

results_df = pd.DataFrame(results, columns=['Sample', 'Mean', 'Probability'])

results_df.index = range(1, len(results_df) + 1)

print(results_df)


# In[ ]:




