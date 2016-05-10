# trng
This is a GitHub repository for a Hardware True Random Number Generator that uses a white-noise generating circuit as a source of entropy.
## Dependencies
The python scripts found in util require Python 2.7.
Creating images requires Pillow and PyPNG python modules.
Compiling trng_client requires libusb
## About this repository
Random numbers are vital to the success of many applications that use cryptography.  Pseudo-random number generators (PRNGs) used in modern computers are flawed in their generation due to their deterministic nature, any numbers generated rely on a seed to fuel their generation and without a truly random seed the resulting numbers are inherently insecure.  Using a white-noise generator we can sample data from the voltage signal and create a stream of statistically verified random bits.  Because white-noise has a constant power spectrum across its frequencies it is less prone to obvious oscillations in its signal and therefore more difficult to predict.
