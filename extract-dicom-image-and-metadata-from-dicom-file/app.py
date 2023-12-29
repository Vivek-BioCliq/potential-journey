import pydicom
import matplotlib.pyplot as plt

dicom_file= pydicom.read_file("ID_0000_AGE_0060_CONTRAST_1_CT.dcm")
print(dicom_file.Rows)

ct=dicom_file.pixel_array
plt.figure()
plt.imshow(ct, cmap='gray')

plt.show()

# print(dicom_file)
