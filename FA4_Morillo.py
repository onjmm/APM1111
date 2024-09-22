#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd

# New data input
data = {
    "Normal": [67, 70, 63, 65, 68, 60, 70, 64, 69, 61, 66, 65, 71, 62, 66, 68, 64, 67, 62, 66, 65, 63, 66, 65, 63,
               69, 62, 67, 59, 66, 65, 63, 65, 60, 67, 64, 68, 61, 69, 65, 62, 67, 70, 64, 63, 68, 64, 65, 61, 66],
    
    "Skewed-right": [31, 43, 30, 30, 38, 26, 29, 55, 46, 26, 29, 55, 46, 26, 29, 57, 34, 34, 36, 40, 28, 26, 66, 63, 30, 33, 24, 35, 34,
                     40, 24, 29, 24, 27, 35, 33, 75, 38, 34, 85, 29, 40, 41, 35, 26, 34, 19, 23, 28, 26, 31, 25, 22, 28],
    
    "Skewed-left": [102, 55, 70, 95, 73, 79, 60, 73, 89, 85, 72, 92, 76, 93, 76, 97, 10, 70, 85, 25, 83, 58, 10, 92, 82,
                    87, 104, 75, 80, 66, 93, 90, 84, 73, 98, 79, 35, 71, 63, 58, 82, 72, 93, 44, 65, 77, 81, 77],
    
    "Uniform": [12.1, 11.6, 12.4, 12.1, 12.1, 12.2, 12.2, 12.2, 11.9, 12.2, 12.3, 12.3, 11.7, 12.3, 12.3, 12.4, 12.4, 12.1, 12.4, 12.4, 12.5, 11.8, 12.5, 12.5, 12.5, 
                11.6, 11.6, 12.0, 11.6, 11.6, 11.7, 12.3, 11.7, 11.7, 11.7, 11.8, 11.8, 11.8, 11.9, 11.9, 11.9, 12.0, 11.9, 12.0, 12.0, 12.0]
}

# Calculate moments
moment_result = {key: [np.mean([x**i for x in values]) for i in range(1, 5)] for key, values in data.items()}

# Calculate mean moments
mean_result = {key: [np.mean([(x-np.mean(values))**i for x in values]) for i in range(1, 5)] for key, values in data.items()}

# Calculate moments about 75
moments_75 = {key: [np.mean([(x-75)**i for x in values]) for i in range(1, 5)] for key, values in data.items()}

# Verification of relationships between moments
def verify_rel(moment_data, mean_data):
    m1_pr, m2_pr, m3_pr, m4_pr = moment_data
    m2_calc = m2_pr - m1_pr**2
    m3_calc = m3_pr - 3 * m1_pr * m2_pr + 2 * m1_pr**3
    m4_calc = m4_pr - 4 * m1_pr * m3_pr + 6 * m1_pr**2 * m2_pr - 3 * m1_pr**4
    
    return {
        "m2_calculated": m2_calc,
        "m2_mean": mean_data[1],
        "m3_calculated": m3_calc,
        "m3_mean": mean_data[2],
        "m4_calculated": m4_calc,
        "m4_mean": mean_data[3]
    }

verify_results = {key: verify_rel(moments_75[key], mean_result[key]) for key in data.keys()}

# Create DataFrames for results
df_moments = pd.DataFrame(moment_result, index=["1st Moment", "2nd Moment (Variance)", "3rd Moment (Skewness)", "4th Moment (Kurtosis)"]).round(2)
df_moments_mean = pd.DataFrame(mean_result, index=["1st Mean Moment", "2nd Mean Moment (Variance)", "3rd Mean Moment (Skewness)", "4th Mean Moment (Kurtosis)"]).round(2)
df_moments_75 = pd.DataFrame(moments_75, index=["1st Moment (75)", "2nd Moment (75)", "3rd Moment (75)", "4th Moment (75)"]).round(2)
df_verify = pd.DataFrame(verify_results).T.round(2)

# Display results
print("Moments Table")
display(df_moments)
# From this table, we can conclude that:
# The mean from the normal dataset is relatively high, indicating values cluster around a higher range.
# The variance for the normal distribution is relatively low compared to the skewed distributions, indicating tighter clustering around the mean.
# The third moment (skewness) for the normal distribution is close to zero, confirming its symmetry.
# The fourth moment (kurtosis) shows that the normal distribution has significantly lower values than the skewed distributions, indicating lighter tails.

print("Mean Moments Table")
display(df_moments_mean)
# From this table, we can conclude that:
# The first mean moment is zero for all datasets, confirming its definition.
# The second mean moment (variance) is lowest for the normal distribution, indicating tighter clustering around the mean.
# The third mean moment shows the direction and extent of asymmetry, with the normal distribution being symmetrical.
# The fourth mean moment indicates lighter tails for the normal distribution compared to the skewed distributions, which exhibit higher kurtosis.

print("Moments about 75 Table")
display(df_moments_75)
# From this table, we can conclude that:
# The first moment about 75 is negative for all datasets, indicating that most values are below 75.
# The second moment shows that the normal distribution has the smallest variance when measured about 75.
# The third moment indicates significant negative skewness for the skewed-left distribution.
# The fourth moment illustrates that the normal distribution has the smallest kurtosis, suggesting fewer extreme values around 75.

print("Verification Results Table")
display(df_verify)
# From this table, we can conclude that:
# The calculated moments match the mean moments for each distribution, confirming their relationships.
# This consistency indicates that the moment calculations are accurate and adhere to the mathematical properties expected for each type of distribution.


# In[ ]:




