# KUB
- KUB refers to a medical imaging technique called a Kidneys, Ureters, and Bladder X-ray.
- This imaging test allows doctors to visualize these organs to detect any abnormalities, stones, or issues in urinary system and surroundings.
- The file format of a KUB X-ray images are saved in 'DICOM' file format.
- The image produced by a KUB X-ray is a 2D representation.
- The resulting image shows the kidneys, ureters, and bladder
- The image produced by a KUB X-ray is typically in grayscale (varying shades of gray).

# nii Images
- The Neuroimaging Informatics Technology Initiative (NIfTI) is an open file format commonly used to store brain imaging data obtained using Magnetic Resonance Imaging (MRI) method.
- NII files contain information about the structure of the brain.
- NIfTI files typically have the extensions .nii or .nii.gz (if compressed).
- Brain images in NIfTI format are represented as a 3D or 4D matrix of voxels (volumetric pixels).
- NIfTI files include header information that describes the image data, such as dimensions, voxel size, data type, orientation, and other metadata like patient information, acquisition parameters, and study details.

# Image Compression
- Image compression is a process that makes image files smaller.
- Works either by removing bytes of information from the image, or by using an image compression algorithm to rewrite the image file in a way that takes up less storage space.

## Lossy Image Compression
 Lossy image compression retains the most significant information for the image without keeping every single pixel.
 
 Common examples of lossy compression methods include:
#### JPEG
This file format, named after the Joint Photographic Experts Group, is perhaps the most widely used image compression method. It can usually compress files by a ratio of 10:1 with a minimal reduction in image quality. More recent versions of JPEG include JPEG 2000 and JPEG XR, but many browsers do not support these formats.
#### WebP
While WebP also supports lossless compression, it is more commonly used for lossy image compression. Google originally developed WebP to replace the JPEG, PNG, and GIF file formats.
#### High Efficiency Image Format (HEIF)
The High Efficiency Image Format (HEIF) is a type of container file for compressed images. Images compressed with this method are sometimes called HEIC files.
  

## Lossless Image Compression
"Lossless" image compression uses mathematical algorithms to rewrite an image file without removing any information.
An image treated with lossless compression should appear basically identical to the original, but should have a much smaller file size.

Widely used lossless compression methods include:

#### Portable Network Graphics (PNG)
which is sometimes used on the web instead of JPEG or WebP.
#### Graphics Interchange Format (GIF)
often used on the web as well.
#### Bitmap (BMP)
files are usually too large for practical use on the web.
