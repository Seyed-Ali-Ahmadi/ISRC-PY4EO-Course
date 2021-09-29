import laspy
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


rootDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
lasName = 'nb_2014_2533000_7362000-10 - Crop.las'
lasFile = laspy.read(rootDir + lasName)

x = np.array(lasFile.x)
y = np.array(lasFile.y)
z = np.array(lasFile.z)
c = np.array(lasFile.classification)
r = np.array(lasFile.return_number)
i = lasFile.intensity

i[i > 300] = 300

minx, miny, minz = lasFile.header.mins
maxx, maxy, maxz = lasFile.header.maxs

# sample = np.random.choice(lasFile.header.point_count, 10000).tolist()
sample = list(range(lasFile.header.point_count))

# fig = plt.figure()
# plt.tight_layout()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter3D(x[sample], y[sample], z[sample],
#              marker='.', c=i[sample], cmap='gray', alpha=0.5)  # color='k'
# plt.show()

fig = plt.figure()
plt.tight_layout()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x[(c == 2) & (i < 90)], y[(c == 2) & (i < 90)], z[(c == 2) & (i < 90)],
             marker='.', color='k', alpha=0.5)  # color='k'
plt.show()

fig = plt.figure()
plt.tight_layout()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x[i < 90], y[i < 90], z[i < 90],
             marker='.', c=i[i < 90], cmap='gray', alpha=0.5)  # color='k'
plt.show()

