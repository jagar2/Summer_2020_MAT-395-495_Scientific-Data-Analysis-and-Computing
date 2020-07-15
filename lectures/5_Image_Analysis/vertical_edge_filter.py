
horizontal_kernel = vertical_kernel.T

gradient_horizontal = ndi.correlate(pixelated.astype(float), horizontal_kernel,
                                    mode='reflect')

gradient_mag = np.sqrt(gradient_vertical**2 + gradient_horizontal**2)
plt.imshow(gradient_mag)
