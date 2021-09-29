import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datetime as dt


root = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
# -----------------------------------------------------------------------------------------------
data = 'ACE_GSE_position.txt'

ADCS = pd.read_csv(root + data, delimiter='\t')
print(ADCS.shape)

time = []
for i in range(len(ADCS)):
    time.append(dt.datetime(ADCS['Year'][i], 1, 1) + dt.timedelta(days=int(ADCS['DOY'][i]) - 1))

x = ADCS.iloc[:, 3]
y = ADCS.iloc[:, 4]
z = ADCS.iloc[:, 5]

fig = plt.figure()
plt.tight_layout()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(0, 0, 0, marker='o', color='b', s=20)
ax.scatter3D(x, y, z, marker='.', color='k', alpha=0.3)
plt.show()
# -----------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------
data = 'ancillary.txt'

GPS_Veloc = np.loadtxt(root + data)
print(GPS_Veloc.shape)

x = GPS_Veloc[:, 0]
y = GPS_Veloc[:, 1]
z = GPS_Veloc[:, 2]

fig = plt.figure()
plt.tight_layout()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(0, 0, 0, marker='o', color='b', s=20)
ax.scatter3D(x, y, z, marker='.', color='k', alpha=0.3)
plt.show()

plt.figure()
plt.plot(x, 'k.')
plt.plot(y, 'b.')
plt.plot(z, 'r.')
plt.show()
