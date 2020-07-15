
xi = np.arange(9)
x0 = 9 // 2  # 4
x = xi - x0
sigma = 1
gaussian_kernel = (1/(np.sqrt(2*np.pi)*sigma) * 
                   np.exp(-(x**2) / 2*sigma**2))
fig = plt.figure()
plt.plot(gaussian_kernel)

## 2

gauss_diff = np.convolve(gaussian_kernel, [-1, 0, 1], mode='full')

## 3

smooth_diff = ndi.correlate(noisy_signal, gauss_diff, mode='reflect')

fig = plt.figure()
plt.plot(noisy_signal)
plt.plot(smooth_diff)
