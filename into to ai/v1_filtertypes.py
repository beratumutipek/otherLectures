import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_convolution(input_image, kernel):
    output_image = cv2.filter2D(input_image, -1 , kernel)
    return output_image

image = cv2.imread("into to ai/picture1.jpg")
image = cv2.resize(image, (224, 224))

sharpen_kernel = np.array([[0, -1, 0],
                           [-1,5,-1],
                           [0,-1,0]
])
blur_kernel = np.array([[1, 2, 1],
                        [2,4,2],
                        [1, 2, 1]
])/16
edge_detection_kernel = np.array([[0, -1, 0],
                                  [-1,4,-1],
                                  [0,-1,0]
])
sharpened_image = apply_convolution(image, sharpen_kernel)
blurred_image = apply_convolution(image, blur_kernel)
edge_image = apply_convolution(image, edge_detection_kernel)

plt.figure(figsize=(12,4))
plt.subplot(141)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.subplot(142)
plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
plt.title("Sharpened")
plt.subplot(143)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title("Blurred")
plt.subplot(144)
plt.imshow(cv2.cvtColor(edge_image, cv2.COLOR_BGR2RGB))
plt.title("Edge")





plt.show()


