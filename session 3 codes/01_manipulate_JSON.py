import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt


dataDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'


# Read .geojson with Pandas
# metadata_pd = pd.read_json(dataDir + 'TehranAreaOfInterest.geojson')
# print(metadata_pd)

# Read .geojson file with json
with open(dataDir + 'TehranAreaOfInterest.geojson', 'r') as f:
    metadata = json.load(f)

# f = open(dataDir + 'TehranAreaOfInterest.geojson', 'r')
# metadata = json.load(f)

# print(metadata)
# print(metadata.keys())
# print(metadata['type'])
# print(metadata['features'])

META = {}
for i in range(len(metadata['features'])):
    # print(metadata['features'][i].keys())
    META[metadata['features'][i]['properties']['OrderDesc']] = \
        np.array(metadata['features'][i]['geometry']['coordinates'])[0, :, :]


plt.figure()
for key in META.keys():
    plt.plot(META[key][:, 0], META[key][:, 1])
plt.show()


# 1. Extract information from Products.geojson file and save them as a .CSV file.
# id/vehicle/sensor/bands/acq_date/cloud_pc/...

# 2. Display the product boundaries on a matplotlib figure.
# 3. Display the products and AOIs on an interactive online map using colab. (folium)

