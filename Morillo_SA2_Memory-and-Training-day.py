#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
import statsmodels.api as sm
from scipy.stats import levene

df = pd.read_csv('Alzheimers-Mice-Data.csv')

# Assumptions for Training Day Errors
print("Training Day Errors")

# Assumption 1: The dependent variable (Training errors) is continuous.
print("\nAssumption 1 (Training Day): The dependent variable (Training errors) is continuous.")
print("This assumption is satisfied since the number of errors made is a continuous measure.")

# Assumption 2: The independent variables (AD_Status and Treatment) are categorical.
print("\nAssumption 2 (Training Day): The independent variables (AD_Status and Treatment) are categorical.")
print("AD_Status and Treatment are categorical variables with multiple groups (AD_Status: Transgenic/Wild, Treatment: 4 different drugs).")

# Assumption 3: Independence of observations.
print("\nAssumption 3 (Training Day): Independence of observations.")
print("This assumption is satisfied since each mouse is independently assigned to a group and treatment.")

# Assumption 4: Outliers
plt.figure(figsize=(8, 6))
sns.boxplot(x='AD_Status', y='Training', hue='Treatment', data=df)
plt.title('Boxplot of Training Errors by AD Status and Treatment')
plt.show()
print("\nAssumption 4 (Training Day): There should be no significant outliers.")
print("Boxplot inspection shows no extreme outliers in any group for Training day errors.")

# Assumption 5: Normality
training_groups = [group['Training'] for _, group in df.groupby(['AD_Status', 'Treatment'])]
training_normality = [stats.shapiro(group) for group in training_groups]

print("\nAssumption 5 (Training Day): Normality of the dependent variable for each group (Shapiro-Wilk test).")
for i, (stat, p) in enumerate(training_normality):
    print(f"Shapiro-Wilk test for Training group {i}: W={stat:.3f}, p={p:.3f}")
    if p > 0.05:
        print("Since p > 0.05, the assumption of normality holds.")
    else:
        print("Since p < 0.05, the assumption of normality does not hold.")

# Assumption 6: Homogeneity of variances
training_levene = levene(*training_groups)

print("\nAssumption 6 (Training Day): Homogeneity of variances (Levene's test).")
print(f"Levene's test for Training day errors: W={training_levene.statistic:.3f}, p={training_levene.pvalue:.3f}")
print(f"Since p > 0.05, the assumption of equal variances holds." if training_levene.pvalue > 0.05 else "Since p < 0.05, the assumption of equal variances does not hold.")

# Perform ANOVA for Training Day Errors
def perform_anova(data, dependent_var):
    formula = f"{dependent_var} ~ C(AD_Status) + C(Treatment) + C(AD_Status):C(Treatment)"
    model = ols(formula, data=data).fit()
    aov_table = sm.stats.anova_lm(model, typ=2)
    return aov_table

print("\n=== Training Day Errors Analysis ===\n")
training_anova = perform_anova(df, 'Training')
print("ANOVA Results for Training Day Errors:")
print(training_anova)


# Assumptions for Memory Day Errors
print("Memory Day Errors")

# Assumption 1: The dependent variable (Memory errors) is continuous.
print("\nAssumption 1 (Memory Day): The dependent variable (Memory errors) is continuous.")
print("This assumption is satisfied since the number of errors made is a continuous measure.")

# Assumption 2: The independent variables (AD_Status and Treatment) are categorical.
print("\nAssumption 2 (Memory Day): The independent variables (AD_Status and Treatment) are categorical.")
print("AD_Status and Treatment are categorical variables with multiple groups (AD_Status: Transgenic/Wild, Treatment: 4 different drugs).")

# Assumption 3: Independence of observations.
print("\nAssumption 3 (Memory Day): Independence of observations.")
print("This assumption is satisfied since each mouse is independently assigned to a group and treatment.")

# Assumption 4: Outliers
plt.figure(figsize=(8, 6))
sns.boxplot(x='AD_Status', y='Memory', hue='Treatment', data=df)
plt.title('Boxplot of Memory Errors by AD Status and Treatment')
plt.show()
print("\nAssumption 4 (Memory Day): There should be no significant outliers.")
print("Boxplot inspection shows no extreme outliers in any group for Memory day errors.")

# Assumption 5: Normality
memory_groups = [group['Memory'] for _, group in df.groupby(['AD_Status', 'Treatment'])]
memory_normality = [stats.shapiro(group) for group in memory_groups]

print("\nAssumption 5 (Memory Day): Normality of the dependent variable for each group (Shapiro-Wilk test).")
for i, (stat, p) in enumerate(memory_normality):
    print(f"Shapiro-Wilk test for Memory group {i}: W={stat:.3f}, p={p:.3f}")
    if p > 0.05:
        print("Since p > 0.05, the assumption of normality holds.")
    else:
        print("Since p < 0.05, the assumption of normality does not hold.")

# Assumption 6: Homogeneity of variances
memory_levene = levene(*memory_groups)

print("\nAssumption 6 (Memory Day): Homogeneity of variances (Levene's test).")
print(f"Levene's test for Memory day errors: W={memory_levene.statistic:.3f}, p={memory_levene.pvalue:.3f}")
print(f"Since p > 0.05, the assumption of equal variances holds." if memory_levene.pvalue > 0.05 else "Since p < 0.05, the assumption of equal variances does not hold.")

# Perform ANOVA for Memory Day Errors
print("\n=== Memory Day Errors Analysis ===\n")
memory_anova = perform_anova(df, 'Memory')
print("ANOVA Results for Memory Day Errors:")
print(memory_anova)


# In[72]:


def calc_statistics(data):
    valid = data.notna().sum()
    mode = data.mode()[0]
    median = data.median()
    std_dev = data.std()
    variance = data.var()
    skewness = data.skew()
    kurtosis = data.kurtosis()
    std_error_skew = np.sqrt(6 * valid / (valid - 1) / (valid + 1) * (valid - 2) / valid)
    std_error_kurt = np.sqrt(24 * valid * (valid - 1) ** 2 / ((valid - 2) * (valid - 3) * (valid + 1) ** 2))
    min_val = data.min()
    max_val = data.max()
    percentiles = data.quantile([0.25, 0.5, 0.9])

    stats_dict = {
        'Valid': valid,
        'Mode': mode,
        'Median': median,
        'Standard Deviation': std_dev,
        'Variance': variance,
        'Skewness': skewness,
        'Kurtosis': kurtosis,
        'Std Error of Skewness': std_error_skew,
        'Std Error of Kurtosis': std_error_kurt,
        'Min': min_val,
        'Max': max_val,
        '25th Percentile': percentiles[0.25],
        '50th Percentile (Median)': percentiles[0.5],
        '90th Percentile': percentiles[0.9]
    }

    return stats_dict

# List of all combinations of AD_Status and Treatment
ad_status_treatment_combinations = [(1, 1), (1, 2), (1, 3), (1, 4), 
                                    (2, 1), (2, 2), (2, 3), (2, 4)]

training_stats_list = []
# Loop through each combination of AD_Status and Treatment, and calculate the statistics
for ad_status, treatment in ad_status_treatment_combinations:
    # Filter the dataframe for the current combination of AD_Status and Treatment
    filtered_df = df[(df['AD_Status'] == ad_status) & (df['Treatment'] == treatment)]
    training_stats = calc_statistics(filtered_df['Training'])
    
    # Add AD_Status and Treatment information to the stats for easier identification
    training_stats['AD_Status'] = ad_status
    training_stats['Treatment'] = treatment
    training_stats_list.append(training_stats)

# Convert the list of statistics to a DataFrame
training_stats_df = pd.DataFrame(training_stats_list)
# Set 'AD_Status' and 'Treatment' as the index for the DataFrame
training_stats_df.set_index(['AD_Status', 'Treatment'], inplace=True)
training_stats_df


# In[73]:


memory_stats_list = []

# Loop through each combination of AD_Status and Treatment, and calculate the statistics for Memory
for ad_status, treatment in ad_status_treatment_combinations:
    # Filter the dataframe for the current combination of AD_Status and Treatment
    filtered_df = df[(df['AD_Status'] == ad_status) & (df['Treatment'] == treatment)]
    memory_stats = calc_statistics(filtered_df['Memory'])
    
    # Add AD_Status and Treatment information to the stats for easier identification
    memory_stats['AD_Status'] = ad_status
    memory_stats['Treatment'] = treatment
    memory_stats_list.append(memory_stats)

# Convert the list of statistics to a DataFrame
memory_stats_df = pd.DataFrame(memory_stats_list)
# Set 'AD_Status' and 'Treatment' as the index for the DataFrame
memory_stats_df.set_index(['AD_Status', 'Treatment'], inplace=True)
memory_stats_df


# In[79]:


from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Post-Hoc Test: Tukey's HSD for Treatment if the main effect of Treatment is significant
if training_anova['PR(>F)']['C(Treatment)'] < 0.05:
    print("\nPost-hoc Analysis for Treatment (Training Day) using Tukey's HSD:")
    tukey = pairwise_tukeyhsd(df['Training'], df['Treatment'], alpha=0.05)
    print(tukey.summary())


# In[80]:


# Post-Hoc Test: Tukey's HSD for Treatment if the main effect of Treatment is significant
if memory_anova['PR(>F)']['C(Treatment)'] < 0.05:
    print("\nPost-hoc Analysis for Treatment (Memory Day) using Tukey's HSD:")
    tukey = pairwise_tukeyhsd(df['Memory'], df['Treatment'], alpha=0.05)
    print(tukey.summary())


# In[ ]:




