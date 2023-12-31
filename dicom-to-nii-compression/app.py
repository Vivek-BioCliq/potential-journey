import pydicom
import nibabel
import numpy as np
import matplotlib.pyplot as plt


def showDicom(dicom_path):
    dicom_file= pydicom.read_file(dicom_path)
    print(dicom_file.Rows)

    ct=dicom_file.pixel_array
    plt.figure()
    plt.imshow(ct, cmap='gray')
    plt.show()
    
showDicom('dicom-to-nii-compression\ID_0000_AGE_0060_CONTRAST_1_CT.dcm')   

def compress(dicom_path, nii_path):
    dicom_data = pydicom.dcmread(dicom_path)
    dicom_array = dicom_data.pixel_array.astype(np.float32)
    nii_image = nibabel.Nifti1Image(dicom_array, np.eye(4))
    nibabel.save(nii_image, nii_path)
    
# compress("dicom-to-nii-compression\ID_0000_AGE_0060_CONTRAST_1_CT.dcm", "./dicom-to-nii-compression/output_nii_file.nii.gz")
# compress("dicom-to-nii-compression\ID_0000_AGE_0060_CONTRAST_1_CT.dcm", "./dicom-to-nii-compression/output_nii_file.nii")    
    
def showNii(nii_path):
    nii_image = nibabel.load(nii_path)
    nii_data = nii_image.get_fdata()
    
    if len(nii_data.shape) == 3:
        middle_slice = nii_data.shape[2] // 2
        plt.imshow(nii_data[:, :, middle_slice], cmap='gray')
        plt.axis('off')
        plt.title('NIfTI Image')
        plt.show()
    elif len(nii_data.shape) == 2:
        plt.imshow(nii_data, cmap='gray')
        plt.axis('off')
        plt.title('NIfTI Image')
        plt.show()
    elif len(nii_data.shape) == 1:
        plt.plot(nii_data)
        plt.title('NIfTI Data')
        plt.show()
    else:
        print("The NIfTI data does not contain 1, 2, or 3 dimensions to display.")
    
showNii('dicom-to-nii-compression\output_nii_file.nii')    