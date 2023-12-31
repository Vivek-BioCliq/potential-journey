# DICOM
 - DICOM stands for Digital Imaging and Communications in Medicine.
 - It is s standard protocol that is responsible to produce, store, process and display digital images in radiology.
 - DICOM is widely used for most types of medical imaging, for example magnetic resonance imaging (MRI), computed tomography (CT) scans, mammograms, and ultrasounds.
 - Image files that are compliant with ?part 10? of the DICOM standard are generally referred to as “DICOM format files” or simply “DICOM files” and are represented as “.dcm.”
 - DICOM files contain both the images themselves (like CT scans, MRIs, or X-rays) and the related metadata.
   

# DICOM Tags
- DICOM tags are data elements within a DICOM file that contain information about the patient, the image, and how the image was acquired.
- Each tag has a unique identifier (tag number) and can store different types of information, such as patient information (name, ID, birth date), image parameters (pixel data, modality, study description), acquisition details (date, time, equipment used), and more.
- DICOM tag identifies the attribute, usually in the format (XXXX,XXXX) with hexadecimal numbers, and may be divided further into DICOM Group Number and DICOM Element Number.


# CT
- Stands for Computed Tomography
- Computed Tomography (CT) is a medical imaging technique that uses X-rays to create detailed images of structures inside the body.
- It produces cross-sectional images, or "slices," of the body, allowing doctors to visualize internal organs, bones, soft tissues, and blood vessels in great detail.
- During a CT scan, the X-ray machine rotates around the patient, capturing multiple X-ray images from different angles. A computer processes these images to create detailed cross-sectional views, which can be further reconstructed into 3D images if needed.
- The file format commonly associated with CT scans is DICOM.

# CT Planes

1. **Axial**: Axial planes are horizontal planes that divide the body into upper and lower sections. Axial CT scans are obtained by taking cross-sectional images parallel to the ground, providing a view from the top looking down or from the bottom looking up. These images display structures as if you're looking from the feet toward the head or vice versa.

2. **Coronal**: Coronal planes divide the body into front and back sections. Coronal CT scans are acquired by taking images perpendicular to the ground, providing a view from the front to the back or vice versa. These images display structures as if you're looking from one side of the body to the other.

3. **Sagittal**: Sagittal planes divide the body into left and right sections. Sagittal CT scans are acquired by taking images perpendicular to both the axial and coronal planes, providing a view from the side. These images display structures as if you're looking from one side of the body or the other. Sagittal views are helpful for examining structures such as the spinal cord or joints.

  ![image](https://github.com/Vivek-BioCliq/potential-journey/assets/154883282/07a898f6-0dcb-417a-8db7-5cf2812aaee0)


# CT Sequences
## Plain CT Sequence
- This sequence involves taking images without the use of a contrast agent.
- It provides a baseline view of the body's structures, showing anatomical details like bones, organs, and tissues without the use of any additional substance.

## Contrast CT Sequence
 - This involves administering a contrast agent, typically **iodine-based, orally or through an IV injection**.
 - The contrast agent helps to highlight blood vessels, organs, and other structures by making them more visible on the CT images.
 - It improves the visualization of certain conditions like tumors, inflammation, or vascular irregularities.
