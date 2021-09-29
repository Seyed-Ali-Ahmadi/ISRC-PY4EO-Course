import h5py as h5
import matplotlib.pyplot as plt

rootDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
data = 'ICESat/208978797/processed_ATL03_20210216071011_08291007_004_01.h5'

file = h5.File(rootDir + data, 'r')
print(file)

print(file.keys())
print(file['gt2r'].keys())
print(file['gt2r/heights'].keys())
print(file['gt2r']['geolocation'].keys())

h = list(file['gt2r/heights/h_ph'])
y = list(file['gt2r/heights/lat_ph'])
x = list(file['gt2r/heights/lon_ph'])

plt.figure()
plt.plot(x, h, '.k', alpha=0.3)
plt.show()

