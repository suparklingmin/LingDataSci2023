# Linguistics and Data Science [hw03]
# Release date: 2023-09-20 
# Due date: 2023-09-22 1:00 PM

import numpy as np

# Descriptive Statistics
# mean
def mean(x:np.ndarray):
    return sum(x) / len(x)

# deviation
def dev(x:np.ndarray):
    return # [Q1] EDIT THIS LINE

# standard deviation
def std(x:np.ndarray):
    return # [Q2] EDIT THIS LINE

# covariance
def cov(x:np.ndarray, y:np.ndarray):
    return # [Q3] EDIT THIS LINE

# correlation
def cor(x:np.ndarray, y:np.ndarray):
    return cov(x, y) / (std(x) * std(y))

# Dataset (http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights)
# height in inches
height = [
    65.78, 71.52, 69.40, 68.22, 67.79,
    68.70, 69.80, 70.01, 67.90, 66.78,
    66.49, 67.62, 68.30, 67.12, 68.28,
    71.09, 66.46, 68.65, 71.23, 67.13,    
]
height = np.array(height)

# weight in pounds
weight = [
    112.99, 136.49, 153.03, 142.34, 144.30,
    123.30, 141.49, 136.46, 112.37, 120.67,
    127.45, 114.14, 125.61, 122.46, 116.09,
    140.00, 129.50, 142.97, 137.90, 124.04,
]
weight = np.array(weight)

print('correlation between height and weight:', cor(height, weight)) # [Q4] Write the result

# convert inch to (centi)meter
height = height # EDIT THIS LINE

# convert pound to kilogram
weight = weight # EDIT THIS LINE

# calculate BMI (Body mass index)
bmi = np.array() # EDIT THIS LINE

print('who has the lowest BMI:', bmi.argmin()) # [Q5] Write the result
