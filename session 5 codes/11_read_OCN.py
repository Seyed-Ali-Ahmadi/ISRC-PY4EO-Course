import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import matplotlib.ticker as mticker


root = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
dataDir = 'Sentinel/S1A_IW_OCN__2SDV_20210822T022328_20210822T022353_039336_04A544_056C.SAFE/measurement/'
data = 's1a-iw-ocn-vv-20210822t022328-20210822t022353-039336-04A544-001.nc'

rootgrp = nc.Dataset(root + dataDir + data, 'r')

windD = rootgrp.variables['owiWindDirection']
windS = rootgrp.variables['owiWindSpeed']
lat = rootgrp.variables['owiLat'][:]
lon = rootgrp.variables['owiLon'][:]

lat = np.array(lat)
lon = np.array(lon)
windS = np.array(windS)
windS[windS == -999.] = np.nan


plt.figure(figsize=(8, 6))
plt.tight_layout()
ax1 = plt.subplot2grid((6, 6), (0, 0), colspan=6, rowspan=6, projection=ccrs.PlateCarree())
ax1.add_feature(cfeature.BORDERS, linestyle=':')
ax1.add_feature(cfeature.OCEAN)
ax1.stock_img()
ax1.coastlines('10m')
gl = ax1.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                   linewidth=1.3, color='black', alpha=0.6, linestyle=':')
step = 0.5
xlocations = list(np.arange(np.amin(lon), np.amax(lon) + step, step))
gl.xlocator = mticker.FixedLocator(xlocations)
ylocations = list(np.arange(np.amin(lat), np.amax(lat) + step, step))
gl.ylocator = mticker.FixedLocator(ylocations)
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
ax1.contourf(lon, lat, windS, 100, transform=ccrs.PlateCarree(), cmap='jet_r')
ax1.set_xlim([np.amin(lon) - .5, np.amax(lon) + .5])
ax1.set_ylim([np.amin(lat) - .5, np.amax(lat) + .5])
plt.show()
