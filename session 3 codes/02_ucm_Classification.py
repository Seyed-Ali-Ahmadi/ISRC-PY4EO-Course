import matplotlib.pyplot as plt
from skimage.io import imread
import numpy as np
import os
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import datetime as dt


dataDir = 'D:/00.University/00.Courses/PythonCourse/Iranian Space Research Center Workshop/Datasets/'
ucmDir = 'UCMerced_LandUse_Tiny/Small_images/'

# print(os.listdir(dataDir + ucmDir))
# Show a subset of images
# for folder in os.listdir(dataDir + ucmDir):
#     # print(len(os.listdir(dataDir + ucmDir + folder)))
#     print('>>>  ' + folder)
#     images = os.listdir(dataDir + ucmDir + folder)
#     sampleImages = random.sample(images, 20)
#     print(sampleImages)
#     print('-----------------')
#     plt.figure()
#     plt.tight_layout()
#     for i in range(20):
#         patch = imread(dataDir + ucmDir + folder + '/' + sampleImages[i])
#         plt.subplot(4, 5, i + 1)
#         plt.imshow(patch)
#         plt.title(sampleImages[i])
#         plt.xticks([]), plt.yticks([])
#     plt.show()

# Classify UCM dataset.
# 21 class, each with 100 patch, each with size 32*32
# (21 * 100) * (32 * 32) = 2100 * 1024
# n_samples  * n_features
# Train --> 1700
# Test --> 400 (Val)
# FEATURES: 32 * 32 * 1 pixels (gray value), if RGB: 32 * 32 * 3
# 4. FEATURES: Texture, Edge, ... <Increase classification accuracy>

n_class = 21
n_patch = 100
w = 32
h = 32
input = np.empty((n_class * n_patch, w * h), dtype=np.float)
output = np.empty((n_class * n_patch, 1))
print(input.shape, output.shape)

count = 1
row = 0
for folder in os.listdir(dataDir + ucmDir):
    # print('>>>  ' + folder)
    images = os.listdir(dataDir + ucmDir + folder)
    for image in images:
        img = np.mean(imread(dataDir + ucmDir + folder + '/' + image), axis=2)  # create a semi-grayscale image

        input[row, :] = img.flatten()
        output[row] = count
        row += 1

    count += 1

# Split train/test datasets
DATA = np.hstack((input, output))
np.random.shuffle(DATA)
train_x = DATA[:1700, :-1]
train_y = DATA[:1700, -1]
test_x = DATA[1700:, :-1]
test_y = DATA[1700:, -1]

print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)

# Train RFC
classifier = RandomForestClassifier(n_estimators=150, warm_start=True, n_jobs=-1)
t_start = dt.datetime.now()
classifier.fit(train_x, train_y)
t_end = dt.datetime.now()
print('Training took {} seconds.'.format(t_end - t_start))

t_start = dt.datetime.now()
labels = classifier.predict(test_x)
t_end = dt.datetime.now()
print('Prediction took {} seconds.'.format(t_end - t_start))

# Print classification report
print(classification_report(test_y, labels, target_names=os.listdir(dataDir + ucmDir)))




