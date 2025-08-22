import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_orig = [10 ,26 ,3 ,44, 51, 54, 6, 67, 73, 61, 58]
mean_orig = np.mean(data_orig)
#in this case the value of n decides how many more samples are to be created(with replacement!!!)
def bootstrap_data(data , n):
    bootstraped_mean_array = []
    for i in range (n):
        data_after = np.random.choice(data , size = len(data) , replace=True)
        bootstraped_mean = np.mean(data_after)
        bootstraped_mean_array.append(float(bootstraped_mean))
    return bootstraped_mean_array


bootstrap1 = bootstrap_data(data_orig ,50)
bootstrap2 = bootstrap_data(data_orig ,500)
bootstrap3 = bootstrap_data(data_orig ,5000)
bootstrap4 = bootstrap_data(data_orig ,50000)

bootstrap_means = [
    np.mean(bootstrap1),
    np.mean(bootstrap2),
    mean_orig,  #this ensures that the middle most plot is the original mean
    np.mean(bootstrap3),
    np.mean(bootstrap4)
]

labels = ["n=50","n=500","original","n=5000","n=50000"]

plt.bar(labels , bootstrap_means , color = ["blue" , "green" , "red" , "purple" , "orange"] , width = 0.4)
plt.show()





