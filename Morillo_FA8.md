Morillo_FA8
================
MORILLO, JADE MARCO S.
2024-11-08

``` r
# Load the dataset
plant_data <- read.csv("C:\\Users\\Marco\\plantgrowth.csv")
```

Assumption \#1: You have one dependent variable that is measured at the
continuous level.

``` r
is_continuous <- is.numeric(plant_data$weight)
cat("Assumption #1 (Continuous variable):", is_continuous, "\n")
```

    ## Assumption #1 (Continuous variable): TRUE

Assumption \#2: You have one independent variable that consists of three
or more categorical, independent groups.

``` r
unique_groups <- unique(plant_data$group)
cat("Assumption #2 (Categorical independent variable with three groups):", length(unique_groups) == 3, "\n")
```

    ## Assumption #2 (Categorical independent variable with three groups): TRUE

``` r
cat("Groups:", paste(unique_groups, collapse = ", "), "\n")
```

    ## Groups: ctrl, trt1, trt2

Assumption \#3: You should have independence of observations, which
means that there is no relationship between the observations in each
group of the independent variable or among the groups themselves.

The independence of observations is not tested here.

Assumption \#4: There should be no significant outliers in the three or
more groups of your independent variable in terms of the dependent
variable.

``` r
print("Checking for outliers with boxplot:")
```

    ## [1] "Checking for outliers with boxplot:"

``` r
ggplot(plant_data, aes(x = group, y = weight, fill = group)) +
  geom_boxplot() +
  labs(title = "Boxplot for Outliers Check",
       x = "Treatment Group",
       y = "Weight") +
  theme_minimal()
```

![](Morillo_FA8_files/figure-gfm/assumption4-1.png)<!-- -->

``` r
# Identify outliers using the IQR rule
outliers <- plant_data %>%
  group_by(group) %>%
  summarize(
    lower_bound = quantile(weight, 0.25) - 1.5 * IQR(weight),
    upper_bound = quantile(weight, 0.75) + 1.5 * IQR(weight),
    outliers = sum(weight < (quantile(weight, 0.25) - 1.5 * IQR(weight)) | 
                   weight > (quantile(weight, 0.75) + 1.5 * IQR(weight)))
  )
print("Assumption #4 (Outliers):")
```

    ## [1] "Assumption #4 (Outliers):"

``` r
print(outliers)
```

    ## # A tibble: 3 × 4
    ##   group lower_bound upper_bound outliers
    ##   <chr>       <dbl>       <dbl>    <int>
    ## 1 ctrl         3.44        6.41        0
    ## 2 trt1         3.21        5.86        2
    ## 3 trt2         4.57        6.44        0

Assumption \#5: Your dependent variable should be approximately normally
distributed for each group of the independent variable.

``` r
shapiro_test <- plant_data %>%
  group_by(group) %>%
  summarize(shapiro_p_value = shapiro.test(weight)$p.value)
cat("Assumption #5 (Normality by Shapiro-Wilk test):\n")
```

    ## Assumption #5 (Normality by Shapiro-Wilk test):

``` r
print(shapiro_test)
```

    ## # A tibble: 3 × 2
    ##   group shapiro_p_value
    ##   <chr>           <dbl>
    ## 1 ctrl            0.747
    ## 2 trt1            0.452
    ## 3 trt2            0.564

Assumption \#6. You have homogeneity of variances (i.e., the variance of
the dependent variable is equal in each group of your independent
variable).

``` r
plant_data$group <- as.factor(plant_data$group)

# Perform Levene's Test for homogeneity of variances
levene_test <- leveneTest(weight ~ group, data = plant_data)
cat("Assumption #6 (Homogeneity of variances by Levene's Test):\n")
```

    ## Assumption #6 (Homogeneity of variances by Levene's Test):

``` r
print(levene_test)
```

    ## Levene's Test for Homogeneity of Variance (center = median)
    ##       Df F value Pr(>F)
    ## group  2  1.1192 0.3412
    ##       27

``` r
cat("\nSummary of Assumptions Check:\n")
```

    ## 
    ## Summary of Assumptions Check:

``` r
cat("1. Assumption #1 (Continuous variable):", is_continuous, "\n")
```

    ## 1. Assumption #1 (Continuous variable): TRUE

``` r
cat("2. Assumption #2 (Categorical independent variable with three groups):", length(unique_groups) == 3, "\n")
```

    ## 2. Assumption #2 (Categorical independent variable with three groups): TRUE

``` r
cat("3. Assumption #3 (Independence of observations): Assumed based on study design.\n")
```

    ## 3. Assumption #3 (Independence of observations): Assumed based on study design.

``` r
cat("4. Assumption #4 (No significant outliers):\n")
```

    ## 4. Assumption #4 (No significant outliers):

``` r
print(outliers)
```

    ## # A tibble: 3 × 4
    ##   group lower_bound upper_bound outliers
    ##   <chr>       <dbl>       <dbl>    <int>
    ## 1 ctrl         3.44        6.41        0
    ## 2 trt1         3.21        5.86        2
    ## 3 trt2         4.57        6.44        0

``` r
cat("5. Assumption #5 (Normality by Shapiro-Wilk test):\n")
```

    ## 5. Assumption #5 (Normality by Shapiro-Wilk test):

``` r
print(shapiro_test)
```

    ## # A tibble: 3 × 2
    ##   group shapiro_p_value
    ##   <chr>           <dbl>
    ## 1 ctrl            0.747
    ## 2 trt1            0.452
    ## 3 trt2            0.564

``` r
cat("6. Assumption #6 (Homogeneity of variances by Levene's Test):\n")
```

    ## 6. Assumption #6 (Homogeneity of variances by Levene's Test):

``` r
print(levene_test)
```

    ## Levene's Test for Homogeneity of Variance (center = median)
    ##       Df F value Pr(>F)
    ## group  2  1.1192 0.3412
    ##       27

``` r
anova_result <- aov(weight ~ group, data = plant_data)
cat("ANOVA Results:\n")
```

    ## ANOVA Results:

``` r
summary(anova_result)
```

    ##             Df Sum Sq Mean Sq F value Pr(>F)  
    ## group        2  3.766  1.8832   4.846 0.0159 *
    ## Residuals   27 10.492  0.3886                 
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

``` r
descriptive_stats <- plant_data %>%
  group_by(group) %>%
  summarize(
    count = n(),
    mean_weight = mean(weight, na.rm = TRUE),
    sd_weight = sd(weight, na.rm = TRUE)
  )
cat("Descriptive Statistics:\n")
```

    ## Descriptive Statistics:

``` r
print(descriptive_stats)
```

    ## # A tibble: 3 × 4
    ##   group count mean_weight sd_weight
    ##   <fct> <int>       <dbl>     <dbl>
    ## 1 ctrl     10        5.03     0.583
    ## 2 trt1     10        4.66     0.794
    ## 3 trt2     10        5.53     0.443

``` r
posthoc_result <- TukeyHSD(anova_result)
cat("Post-hoc Test (Tukey's HSD):\n")
```

    ## Post-hoc Test (Tukey's HSD):

``` r
print(posthoc_result)
```

    ##   Tukey multiple comparisons of means
    ##     95% family-wise confidence level
    ## 
    ## Fit: aov(formula = weight ~ group, data = plant_data)
    ## 
    ## $group
    ##             diff        lwr       upr     p adj
    ## trt1-ctrl -0.371 -1.0622161 0.3202161 0.3908711
    ## trt2-ctrl  0.494 -0.1972161 1.1852161 0.1979960
    ## trt2-trt1  0.865  0.1737839 1.5562161 0.0120064

``` r
cat("\nSummary of Analysis:\n")
```

    ## 
    ## Summary of Analysis:

``` r
cat("1. Descriptive Statistics:\n")
```

    ## 1. Descriptive Statistics:

``` r
print(descriptive_stats)
```

    ## # A tibble: 3 × 4
    ##   group count mean_weight sd_weight
    ##   <fct> <int>       <dbl>     <dbl>
    ## 1 ctrl     10        5.03     0.583
    ## 2 trt1     10        4.66     0.794
    ## 3 trt2     10        5.53     0.443

``` r
cat("2. ANOVA Results:\n")
```

    ## 2. ANOVA Results:

``` r
summary(anova_result)
```

    ##             Df Sum Sq Mean Sq F value Pr(>F)  
    ## group        2  3.766  1.8832   4.846 0.0159 *
    ## Residuals   27 10.492  0.3886                 
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

``` r
cat("3. Post-hoc Test (Tukey's HSD):\n")
```

    ## 3. Post-hoc Test (Tukey's HSD):

``` r
print(posthoc_result)
```

    ##   Tukey multiple comparisons of means
    ##     95% family-wise confidence level
    ## 
    ## Fit: aov(formula = weight ~ group, data = plant_data)
    ## 
    ## $group
    ##             diff        lwr       upr     p adj
    ## trt1-ctrl -0.371 -1.0622161 0.3202161 0.3908711
    ## trt2-ctrl  0.494 -0.1972161 1.1852161 0.1979960
    ## trt2-trt1  0.865  0.1737839 1.5562161 0.0120064
