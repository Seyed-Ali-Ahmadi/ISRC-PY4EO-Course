import laspy

rootDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
lasName = 'nb_2014_2536000_7363000-7.laz'

lasFile = laspy.read(rootDir + lasName)

print(lasFile)
print(lasFile.header.point_count)

print(lasFile.x)
print(lasFile.y)
print(lasFile.z)
print('----------------------------')
print(lasFile.header.scales)
print(lasFile.header.offsets)
print('----------------------------')
print(lasFile.X)
print(lasFile.Y)
print(lasFile.Z)
print('----------------------------')
print(lasFile.return_number)
print(lasFile.intensity)
print(lasFile.classification)
print('----------------------------')
print(lasFile.header.mins)
print(lasFile.header.maxs)


