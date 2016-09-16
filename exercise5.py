import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

# for image processing
import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation

# load the images
bc_images = skimage.io.imread_collection('data/bacterial_growth/bacillus_*.tif')
bc_im = skimage.io.concatenate_images(bc_images)

# to show the image
# for i in range(len(bc_im)):
#     plt.imshow(np.array(bc_im[i]), cmap=plt.cm.viridis)

plt.close()

hist_im, bins_im = skimage.exposure.histogram(bc_im)
# plot histogram of the images
# for i in range(len(bc_im)):
#     hist_im, bins_im = skimage.exposure.histogram(np.array(bc_im[i]))
#     plt.plot(bins_im, hist_im)
#     plt.xlabel('pixel value')
#     plt.ylabel('counts')

# appley a gaussian blur
bc_blur = skimage.filters.gaussian(bc_im, 10.0)

# correct the uneven immumination
bc_float = skimage.img_as_float(bc_im)
bc_sub = bc_float - bc_blur
# plt.imshow(np.array(bc_float[i]), cmap=plt.cm.Greys_r)
# plt.imshow(np.array(bc_sub[i]), cmap=plt.cm.viridis)
#
for i in range(len(bc_im)):
    bc_blur[i] = skimage.filters.gaussian(np.array(bc_im[i]), 10.0)
    bc_float[i] = skimage.img_as_float(np.array(bc_im[i]))
    bc_sub[i] = bc_float[i] - bc_blur[i]
    plt.imshow(np.array(bc_sub[i]), cmap=plt.cm.Spectral_r)

# apply otsu thresholding
thresh = skimage.filters.threshold_otsu(bc_sub)
seg = bc_sub < thresh
seg_lab, num_cells = skimage.measure.label(seg)
# plot our segmentation
for i in range(len(seg)):
    plt.close('all')
    plt.imshow(np.array(seg[i]), cmap=plt.cm.Greys_r)


for i in range(len(seg)):
    # label the seg
    seg_lab[i], num_cells[i] = skimage.measure.label(np.array(seg[i]), return_num=True, background=0)
    plt.close()
    plt.imshow(np.array(seg_lab[i]), cmap=plt.cm.Spectral_r)

seg_lab[33], num_cells[33] = skimage.measure.label(np.array(seg[33]), return_num=True, background=0)
plt.close()
plt.imshow(np.array(seg_lab[33]), cmap=plt.cm.Spectral_r)
return skimage.io.imsave('seg_lab_33.tif')
