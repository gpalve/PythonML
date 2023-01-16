from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = np.mean(speed)
median = np.median(speed)
mode = stats.mode(speed)
stdev = np.std(speed)
variance = np.var(speed)
percentile = np.percentile(speed,50) # 50 percentile of given data gives 87 as speed. means if your speed is 87 you are achiving 50 percent speed out of given data.

print(mean,median,mode,stdev,variance,percentile,sep="\n")  


# creating random dataset using numpy

# data = np.random.uniform(0.0,5.0,250)
# print(data)
# plt.hist(data, 10) # plotting graph with 10 bars...gives how many values between 0-1 1-2 ...4-5.
# plt.show()

data = np.random.uniform(0.0,5.0,250000)
print(data)
plt.hist(data, 100) # plotting graph with 10 bars...gives how many values between 0-1 1-2 ...4-5.
plt.show()