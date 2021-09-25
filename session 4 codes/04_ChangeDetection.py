import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
# OpenCV, PIL, Matplotlib


# Image formats: .png, .tif, .jpg, .bmp

rootDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'

pre_disaster = 'hurricane-matthew_00000027_pre_disaster.png'
post_disaster = 'hurricane-matthew_00000027_post_disaster.png'
# pre_disaster = 'hurricane-florence_00000046_pre_disaster.png'
# post_disaster = 'hurricane-florence_00000046_post_disaster.png'
# pre_disaster = 'hurricane-florence_00000001_pre_disaster.png'
# post_disaster = 'hurricane-florence_00000001_post_disaster.png'

pre_image = imread(rootDir + pre_disaster).astype(float) / 255
post_image = imread(rootDir + post_disaster).astype(float) / 255


# print(pre_image.dtype)
# plt.figure()
# plt.subplot(121), plt.hist(pre_image.flatten(), bins=100)
# plt.subplot(122), plt.hist(post_image.flatten(), bins=100)
# plt.show()


difference_image = post_image - pre_image

plt.figure()
plt.tight_layout()
plt.subplot(231), plt.xticks([]), plt.yticks([])
plt.imshow(pre_image, cmap='gray'), plt.title('Pre Disaster Image')

plt.subplot(232), plt.xticks([]), plt.yticks([])
plt.imshow(post_image, cmap='gray'), plt.title('Post Disaster Image')

plt.subplot(233), plt.xticks([]), plt.yticks([])
plt.imshow(post_image - pre_image, cmap='gray'), plt.title('Difference Image')


plt.subplot(234)
plt.hist(pre_image[:, :, 0].flatten(), bins=100, alpha=0.9, color='r')
plt.hist(pre_image[:, :, 1].flatten(), bins=100, alpha=0.9, color='b')
plt.hist(pre_image[:, :, 2].flatten(), bins=100, alpha=0.9, color='k')

plt.subplot(235)
plt.hist(post_image[:, :, 0].flatten(), bins=100, alpha=0.9, color='r')
plt.hist(post_image[:, :, 1].flatten(), bins=100, alpha=0.9, color='b')
plt.hist(post_image[:, :, 2].flatten(), bins=100, alpha=0.9, color='k')

plt.subplot(236)
plt.hist(difference_image[:, :, 0].flatten(), bins=100, alpha=0.9, color='r')
plt.hist(difference_image[:, :, 1].flatten(), bins=100, alpha=0.9, color='b')
plt.hist(difference_image[:, :, 2].flatten(), bins=100, alpha=0.9, color='k')

plt.show()


threshold = 0.5
# change_map = np.mean(difference_image, axis=2) > threshold
change_map = (difference_image[:, :, 0] > 0) * (difference_image[:, :, 1] > 0) * (difference_image[:, :, 2] > 0)
# change_map = (difference_image[:, :, 0] > 0) + (difference_image[:, :, 1] > 0) + (difference_image[:, :, 2] > 0)

plt.figure()
plt.subplot(121), plt.imshow(difference_image, cmap='gray'), plt.colorbar()
plt.subplot(122), plt.imshow(change_map)
plt.show()

# f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, sharex=True)
# ax1.imshow(), ax1.set_xticks([])

from skimage.filters import threshold_otsu, threshold_multiotsu
otsu_threshold = threshold_otsu(np.mean(difference_image, axis=2))
change_map = np.mean(difference_image, axis=2) > otsu_threshold
plt.figure()
plt.imshow(change_map, cmap='gray')
plt.show()


thresholds = threshold_multiotsu(np.mean(difference_image, axis=2))
regions = np.digitize(np.mean(difference_image, axis=2), bins=thresholds)

plt.figure()
plt.imshow(regions, cmap='jet')
plt.show()


