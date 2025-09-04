import numpy as np
import matplotlib.pyplot as plt


X = np.array([5234, 7890, 10021, 4567, 8765, 9340, 10234, 11200, 8765, 6500])# A dummy dataset representing the number of steps walked over a timespan of 10 days

X_mean = X.mean()

n = int(input("Enter no of bootstraps here : "))
 
def bootstrap(X , n):
    X_mean_store = []
    for i in range(n):
        sample = np.random.choice(X , size = len(X) , replace= True)# this implements the sampling with replacing
        X_mean = sample.mean()
        X_mean_store.append(X_mean)
    return X_mean_store
        
means = bootstrap(X , n)      
means2 = bootstrap(X , 1000) # bigger n for a more stable bootstrap  

c = int(input("Enter the confidence interval here :"))
trimed_portion = (100-c) / 2
upper_bound = np.percentile(means2 , (100 -trimed_portion))
lower_bound = np.percentile(means2 , 0 + trimed_portion)
# 1st plot is for the original data and its mean
plt.subplot(1 , 3 , 1)
plt.bar(range(1 , len(X) + 1) , X , color = 'skyblue' , edgecolor = 'black')
plt.xlabel("Sample Index")
plt.ylabel("Value")
# 2nd plot is for the bootstraped mean
plt.subplot(1 , 3 , 2)
plt.bar(range(1 , n+1) , means , color = 'red' , edgecolor = 'black')
plt.xlabel("Bootstraped Index")
plt.ylabel("Bootstraped mean")
# 3rd plot for the CI interval
plt.subplot(1 , 3 , 3)
plt.hist(means2, bins=30, color="skyblue", edgecolor="black", alpha=0.7)
plt.axvline(lower_bound, color="red", linestyle="--", linewidth=2, label = "Lower Bound")
plt.axvline(upper_bound , color = "red" , linestyle = "--" , label = "Upper_bound")
plt.show()




