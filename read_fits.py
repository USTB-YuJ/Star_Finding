from astropy.io import fits
import pylab as plt

path = '../fit_datasets/20240306204816083_6002.fits'
hdulist = fits.open(path, mode='update', output_verify='fix')
header = hdulist[0].header
data = hdulist[0].data
hdulist.info()
for key in header:
    print(key, header[key])

plt.imshow(data)
plt.colorbar()
plt.show()
