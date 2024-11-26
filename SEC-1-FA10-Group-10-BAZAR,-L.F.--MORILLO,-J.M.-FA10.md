FA10
================
MORILLO, JADE MARCO & BAZAR, LINDSAY FAITH
2024-11-26

``` r
library(tidyverse)
library(car)
library(afex)
library(emmeans)

data <- read.csv("Cholesterol_R2.csv")

head(data)
```

    ##   ID Before After4weeks After8weeks Margarine
    ## 1  1   6.42        5.83        5.75         B
    ## 2  2   6.76        6.20        6.13         B
    ## 3  3   6.56        5.83        5.71         B
    ## 4  4   4.80        4.27        4.15         A
    ## 5  5   8.43        7.71        7.67         B
    ## 6  6   7.49        7.12        7.05         A

``` r
data_long <- data %>%
  pivot_longer(
    cols = starts_with("After"), 
    names_to = "Time",           
    values_to = "Cholesterol"    
  ) %>%
  mutate(
    Time = factor(Time, levels = c("Before", "After4weeks", "After8weeks")),
    Margarine = as.factor(Margarine),
    ID = as.factor(ID)
  )

head(data_long)
```

    ## # A tibble: 6 × 5
    ##   ID    Before Margarine Time        Cholesterol
    ##   <fct>  <dbl> <fct>     <fct>             <dbl>
    ## 1 1       6.42 B         After4weeks        5.83
    ## 2 1       6.42 B         After8weeks        5.75
    ## 3 2       6.76 B         After4weeks        6.2 
    ## 4 2       6.76 B         After8weeks        6.13
    ## 5 3       6.56 B         After4weeks        5.83
    ## 6 3       6.56 B         After8weeks        5.71

``` r
summary_stats <- data_long %>%
  group_by(Margarine, Time) %>%
  summarize(
    Mean = mean(Cholesterol, na.rm = TRUE),
    SD = sd(Cholesterol, na.rm = TRUE),
    n = n()
  )

summary_stats
```

    ## # A tibble: 4 × 5
    ## # Groups:   Margarine [2]
    ##   Margarine Time         Mean    SD     n
    ##   <fct>     <fct>       <dbl> <dbl> <int>
    ## 1 A         After4weeks  5.47 1.39      8
    ## 2 A         After8weeks  5.41 1.37      8
    ## 3 B         After4weeks  6.14 0.815    10
    ## 4 B         After8weeks  6.08 0.779    10

``` r
anova_results <- aov_ez(
  id = "ID", 
  dv = "Cholesterol", 
  data = data_long, 
  within = "Time", 
  between = "Margarine"
)

anova_results
```

    ## Anova Table (Type 3 tests)
    ## 
    ## Response: Cholesterol
    ##           Effect    df  MSE        F   ges p.value
    ## 1      Margarine 1, 16 2.38     1.67  .094    .215
    ## 2           Time 1, 16 0.00 13.19 ** <.001    .002
    ## 3 Margarine:Time 1, 16 0.00     0.02 <.001    .886
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '+' 0.1 ' ' 1

``` r
anova_table <- as.data.frame(anova_results$anova_table)

if (anova_results$anova_table["Margarine:Time", "Pr(>F)"] < 0.05) {
  post_hoc <- emmeans(anova_results, ~ Margarine | Time)
  post_hoc_results <- pairs(post_hoc)
  
  post_hoc_results
}

apa_report <- paste0(
  "A two-way mixed ANOVA was conducted to examine the effect of margarine brands (Brand A and Brand B) and time (three time points) on cholesterol levels. ",
  "The main effect of Margarine was ", 
  ifelse(anova_results$anova_table["Margarine", "Pr(>F)"] < 0.05, "significant", "not significant"), 
  " (F(", anova_results$anova_table["Margarine", "Df"], ", ", anova_results$anova_table["Margarine", "Df.res"], ") = ",
  round(anova_results$anova_table["Margarine", "F"], 2), ", p = ", 
  round(anova_results$anova_table["Margarine", "Pr(>F)"], 3), "). ",
  "The main effect of Time was ", 
  ifelse(anova_results$anova_table["Time", "Pr(>F)"] < 0.05, "significant", "not significant"), 
  " (F(", anova_results$anova_table["Time", "Df"], ", ", anova_results$anova_table["Time", "Df.res"], ") = ",
  round(anova_results$anova_table["Time", "F"], 2), ", p = ", 
  round(anova_results$anova_table["Time", "Pr(>F)"], 3), "). ",
  "The interaction effect between Margarine and Time was ", 
  ifelse(anova_results$anova_table["Margarine:Time", "Pr(>F)"] < 0.05, "significant", "not significant"), 
  " (F(", anova_results$anova_table["Margarine:Time", "Df"], ", ", anova_results$anova_table["Margarine:Time", "Df.res"], ") = ",
  round(anova_results$anova_table["Margarine:Time", "F"], 2), ", p = ", 
  round(anova_results$anova_table["Margarine:Time", "Pr(>F)"], 3), ")."
)

apa_report
```

    ## [1] "A two-way mixed ANOVA was conducted to examine the effect of margarine brands (Brand A and Brand B) and time (three time points) on cholesterol levels. The main effect of Margarine was not significant (F(, ) = 1.67, p = 0.215). The main effect of Time was significant (F(, ) = 13.19, p = 0.002). The interaction effect between Margarine and Time was not significant (F(, ) = 0.02, p = 0.886)."
