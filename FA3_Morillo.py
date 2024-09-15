#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from scipy import stats
from IPython.display import HTML

# Data sample
scores = [88, 45, 53, 86, 33, 86, 85, 30, 89, 53, 41, 96, 56, 38, 62, 71, 51, 86, 
          68, 29, 28, 47, 33, 37, 25, 36, 33, 94, 73, 46, 42, 34, 79, 72, 88, 99, 
          82, 62, 57, 42, 28, 55, 67, 62, 60, 96, 61, 57, 75, 93, 34, 75, 53, 32, 
          28, 73, 51, 69, 91, 35]

mean = f"{np.mean(scores):.3f}"
median = f"{np.median(scores):.3f}"

# Calculate mode and handle different return formats
mode_result = stats.mode(scores, keepdims=False)
mode_value = mode_result.mode if isinstance(mode_result.mode, np.ndarray) else np.array([mode_result.mode])
mode_count = mode_result.count if isinstance(mode_result.count, np.ndarray) else np.array([mode_result.count])

if mode_count[0] > 1:
    mode = f"{mode_value[0]:.3f}"
else:
    mode = f"{mode_value[0]:.3f}"

std_dev = f"{np.std(scores, ddof=1):.3f}"
variance = f"{np.var(scores, ddof=1):.3f}"
skewness = f"{stats.skew(scores):.3f}"
std_error_skewness = f"{np.sqrt(6/len(scores)):.3f}"
kurtosis = f"{stats.kurtosis(scores):.3f}"
std_error_kurtosis = f"{np.sqrt(24/len(scores)):.3f}"
minimum = f"{np.min(scores):.3f}"
maximum = f"{np.max(scores):.3f}"
q1 = f"{np.percentile(scores, 25):.3f}"
q2 = f"{np.percentile(scores, 50):.3f}"
q3 = f"{np.percentile(scores, 75):.3f}"
d9 = f"{np.percentile(scores, 90):.3f}"
p95 = f"{np.percentile(scores, 95):.3f}"

descriptive_stats = {
    "": ["Valid", "<div style='display: flex; justify-content: space-between;'><span>Mode</span><span style='text-align: right;'><sup>a</sup></span></div>", "Median", "Mean", "Std Deviation", "Variance", "Skewness", "Std Error of Skewness",
         "Kurtosis", "Std Error of Kurtosis", "Minimum", "Maximum", "25th Percentile (Q1)", 
         "50th Percentile (Q2)", "75th Percentile (Q3)", "90th Percentile (D9)", "95th Percentile (P95)"],
    "Score": [len(scores), mode, median, mean, std_dev, variance, skewness, std_error_skewness,
              kurtosis, std_error_kurtosis, minimum, maximum, q1, q2, q3, d9, p95]
}

descriptive_stats_df = pd.DataFrame(descriptive_stats)

def color_alternating_rows(row):
    return ['background-color: #f2f2f2' if row.name % 2 == 0 else 'background-color: #ffffff' for _ in row]

def style_left_column(df):
    return df.style.applymap(lambda x: 'text-align: left;', subset=[''])

styled_df = style_left_column(descriptive_stats_df).apply(color_alternating_rows, axis=1).hide(axis='index')

note = "<div style='text-align:left;'><small><sup>a</sup> More than one mode exists, only the first is reported.</small></div>"

html = styled_df.to_html(escape=False)
html += note

HTML(html)


# In[ ]:




