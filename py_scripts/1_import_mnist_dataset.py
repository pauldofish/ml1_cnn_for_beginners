# Sanity check to see that the pip packages are working properly.

import numpy
import mnist
from tensorflow import keras

# Assign mnist dataset to local arrays
train_images = mnist.train_images()
train_labels = mnist.train_labels()

# Print dataset dimensions
print(train_images.shape)
print(train_labels.shape)
