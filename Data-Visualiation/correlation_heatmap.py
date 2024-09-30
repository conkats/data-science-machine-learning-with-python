'''Use heatmap to understand all 
the features in a single plot
correlation coeff:-1 to 1 
correlation=1-straight line from left to right
correlation=-1- straight line going down from left to right
2D matrix where the value at position(0,1) in the correlation
matrix, i.e. show the correlation coefficient features-rows 0 and 1


'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

insurance_df = pd.read_csv('insurance.csv')

age_bmi_changes = insurance_df[['age', 'bmi', 'charges']]

plt.figure()
corr_coeff_mat = age_bmi_changes.corr()
sns.heatmap(corr_coeff_mat, annot=True)
plt.show()
plt.close()

#Close to zero means that there 
#is little to be seen in terms of a relationship
