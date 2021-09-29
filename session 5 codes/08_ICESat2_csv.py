import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


rootDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
data = 'ICESat/photon_2021-02-16_gt2r_t829_1632861182784.csv'

photon_height = pd.read_csv(rootDir + data)
photon_height = np.array(photon_height)
print(photon_height)

lat = photon_height[:, 0]
lon = photon_height[:, 1]
hgt = photon_height[:, 2]
conf = photon_height[:, -1]

plt.figure()
plt.tight_layout()
# plt.plot(lat[conf == 0.], hgt[conf == 0.], 'r.', alpha=0.5)
# plt.plot(lat[conf == 1.], hgt[conf == 1.], 'm.', alpha=0.5)
# plt.plot(lat[conf == 2.], hgt[conf == 2.], 'c.', alpha=0.5)
plt.plot(lat[conf == 3.], hgt[conf == 3.], 'g.', alpha=0.5)
plt.plot(lat[conf == 4.], hgt[conf == 4.], 'b.', alpha=0.5)
plt.ylim([min(hgt), max(hgt)])
plt.show()


fig = plt.figure()
plt.tight_layout()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(lon[conf == 4.], lat[conf == 4.], hgt[conf == 4.], marker='.', s=2, color='k')
plt.show()


