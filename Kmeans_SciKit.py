import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.cluster as sk
plt.rcParams['figure.figsize'] = (1,1)
plt.style.use('ggplot')

data = pd.read_csv('data.csv')
print('Input Data and Shape')
print(data.shape)
data.head()
print (data.columns)

feature1 = data[data.columns[0]].values
feature2 = data[data.columns[1]].values
feature1 = (feature1 - np.mean(feature1))/(max(feature1) - min(feature1))
feature2 = (feature2 - np.mean(feature2))/(max(feature2) - min(feature2))
print('feature1 is Volume')
print('feature2 is Average Average price')
X = np.array(list(zip(feature1,feature2)))
Y = pd.DataFrame()
plt.scatter(feature1, feature2, c='red', s=7 )
plt.show()

kmeans = sk.KMeans(n_clusters = 3)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
plt.scatter(feature1, feature2, c=labels, cmap = 'viridis')
plt.show()

#j=0

#for i in range(len(X)):
#	if kmeans.labels_[i] == 2:
#		Y[j] = X[i]
#		j=j+1		
#		pass
#print(Y.shape)
#plt.scatter(Y[0,:],Y[1,:],c = labels, cmap = 'viridis')
# plt.show()
