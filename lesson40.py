import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

# for image processing
import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation

# Load image data
image = skimage.io.imread('')

# show the image
plt.imshow(image, cmap=plt.cm.viridis)

# correct the uneven immumination
image_blur = skimage.filters.gaussian(image_im, 50.0)
image_float = skimage.img_as_float(image)
image_sub = image_float - image_blur

# corrent for 'hot' or 'bad' pixels
selem = skimage.morphology.square(3)
image_filt = skimage.filters.median(image_sub), selem)
plt.imshow(image_filt[150:250, 450:550]/image_filt.max(), cmap=plt.cm.viridis)

# putting otsu threshold
thresh = skimage.filters.threshold_otsu(image_filt)
seg = phase_filt < thresh
