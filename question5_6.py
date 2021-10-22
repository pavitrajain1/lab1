
import pandas as pd
import matplotlib.pyplot as plt
import math

#reading csv file and converting to dataframe
df=pd.read_csv('pima-indians-diabetes.csv')

# Q5
# grouping by class
class_grp=df.groupby('class')

# Plotting the histogram of attribute ‘preg’ for class=0

#getting group with class=0
a=class_grp.get_group(0)

#plotting histogram
bins=[0,2,4,8,10,12,14,16]
plt.hist(a['pregs'],bins=bins)
plt.title('histogram for preg (class=0)')
plt.show()

# Plotting the histogram of attribute ‘preg’ for class=1

#getting group with class=1
a=class_grp.get_group(1)

#plotting histogram
bins=[0,2,4,8,10,12,14,16,18]
plt.hist(a['pregs'],bins=bins)
plt.title('histogram for preg (class=1)')
plt.show()

#Q6

# boxplot for all the attribute excluding ‘class’ 

#creating subplots
fig, axs = plt.subplots(3,3,figsize=(15,10))
a=list(df.columns)
a.remove('class')

# plotting boxplots
k=0
for i in range(3):
    for j in range(3):
        if(i+j!=4):
            axs[i,j].boxplot(df[a[k]])
            axs[i,j].set(title='Boxplot for '+ a[k])
            k=k+1

# deleting empty subplots
fig.delaxes(axs[2,2]) 

plt.tight_layout()
plt.show()

