
from scipy import ndimage as ndi

smooth_ndi = ndi.convolve(noisy_signal, mean_kernel11,
                          mode='reflect')

plt.plot(smooth_ndi)
