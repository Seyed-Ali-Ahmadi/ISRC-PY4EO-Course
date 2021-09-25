# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.io import imread
#
#
# rootDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
# LC08_2015 = 'LC08_L2SP_161038_20150816_20200908_02_T1/'
#
# band_05 = imread(rootDir + LC08_2015 + 'LC08_L2SP_161038_20150816_20200908_02_T1_SR_B5.TIF')
# print(band_05.shape)
#
# band_05 = band_05.astype(float)
# band_05[band_05 == 0] = np.nan
#
# CORNER_UL_LAT_PRODUCT = 32.78332
# CORNER_UL_LON_PRODUCT = 54.25599
# CORNER_UR_LAT_PRODUCT = 32.81311
# CORNER_UR_LON_PRODUCT = 56.73508
# CORNER_LL_LAT_PRODUCT = 30.65287
# CORNER_LL_LON_PRODUCT = 54.31809
# CORNER_LR_LAT_PRODUCT = 30.68029
# CORNER_LR_LON_PRODUCT = 56.74108
#
#
# xticks = np.arange(0, band_05.shape[1], 600)
# xlabels = np.linspace(CORNER_LL_LON_PRODUCT, CORNER_LR_LON_PRODUCT, len(xticks))
# xlabels = np.round(xlabels, 4)
#
# yticks = np.arange(0, band_05.shape[0], 600)
# ylabels = np.linspace(CORNER_LL_LAT_PRODUCT, CORNER_UL_LAT_PRODUCT, len(yticks))
# ylabels = np.flip(np.round(ylabels, 4))
#
# # plt.figure()
# # plt.tight_layout()
# # plt.imshow(band_05, cmap='gray', vmin=np.nanmin(band_05), vmax=np.nanmax(band_05))
# # plt.xticks(ticks=xticks, labels=xlabels, rotation='vertical', fontsize=9)
# # plt.yticks(ticks=yticks, labels=ylabels, fontsize=9)
# # plt.show()
#
#
# band_04 = imread(rootDir + LC08_2015 + 'LC08_L2SP_161038_20150816_20200908_02_T1_SR_B4.TIF')
# band_04 = band_04.astype(float)
# band_04[band_04 == 0] = np.nan
#
# ndvi = (band_05 - band_04) / (band_05 + band_04)
#
# plt.figure()
# plt.tight_layout()
# plt.imshow(ndvi, cmap='Reds', vmin=np.nanmin(ndvi), vmax=np.nanmax(ndvi))
# plt.xticks(ticks=xticks, labels=xlabels, rotation='vertical', fontsize=9)
# plt.yticks(ticks=yticks, labels=ylabels, fontsize=9)
# plt.show()


# --------------------------------------------------------------------------------------------
import rasterio as rio
from rasterio.warp import calculate_default_transform, reproject, Resampling

rootDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
LC08_2015 = 'LC08_L2SP_161038_20150816_20200908_02_T1/'

src = rio.open(rootDir + LC08_2015 + 'LC08_L2SP_161038_20150816_20200908_02_T1_SR_B5.TIF')

print(src.transform)
print(src.bounds)
print(src.height)
print(src.width)
print(src.crs)

print(src.xy(1000, 1500))
print(src.xy(1001, 1501))


# from rasterio.plot import show
# show(src.read(), transform=src.transform)


# dst_src = 'EPSG:4326'   # WGS84
# transform, width, height = calculate_default_transform(src.crs, dst_src, src.width, src.height, *src.bounds)
#
# kwargs = src.meta.copy()
# kwargs.update({
#     'crs': dst_src,
#     'transform': transform,
#     'width': width,
#     'height': height
# })
#
#
# with rio.open('./LC08_WGS84_B05.tif', 'w', **kwargs) as f:
#     for i in range(1, src.count + 1):
#         reproject(
#             source=rio.band(src, i),
#             destination=rio.band(f, i),
#             src_transform=src.transform,
#             src_crs=src.crs,
#             dst_transform=transform,
#             dst_crs=dst_src,
#             resampling=Resampling.nearest
#         )

import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import numpy as np


dst = rio.open('./LC08_WGS84_B05.tif')
print(dst.crs, dst.bounds)
bbox = list(dst.bounds)
image = dst.read()[0, :, :].astype(float)
image[image == 0] = np.nan


plt.figure(figsize=(8, 6))
plt.tight_layout()
ax1 = plt.subplot2grid((6, 6), (0, 0), colspan=6, rowspan=6, projection=ccrs.PlateCarree())
# ax1.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '50m',
#                                              edgecolor='face',
#                                              facecolor=cfeature.COLORS['land']))
# ax1.add_feature(cfeature.LAND)
ax1.add_feature(cfeature.BORDERS, linestyle=':')
ax1.add_feature(cfeature.LAKES, alpha=0.5)
ax1.add_feature(cfeature.OCEAN)
ax1.stock_img()
ax1.coastlines('10m')
gl = ax1.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                   linewidth=1.3, color='black', alpha=0.6, linestyle=':')

step = 0.5
xlocations = list(np.arange(bbox[0], bbox[2] + step, step))
gl.xlocator = mticker.FixedLocator(xlocations)
ylocations = list(np.arange(bbox[1], bbox[3] + step, step))
gl.ylocator = mticker.FixedLocator(ylocations)
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
ax1.imshow(image, origin='upper', extent=[bbox[0], bbox[2], bbox[1], bbox[3]], transform=ccrs.PlateCarree(), zorder=3)
ax1.set_xlim([bbox[0] - 3, bbox[2] + 3])
ax1.set_ylim([bbox[1] - 3, bbox[3] + 3])
plt.show()













