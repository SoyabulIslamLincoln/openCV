
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('c41cd782b962e5ba758c9bb7104b9400.jpg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5), np.float32)/25 
dst=cv2.filter2D(img, -1, kernel)


title_m=['Image',"2d Comvolution"]
image=[img,dst]

for i in range(2):
    
    plt.subplot(2,1,i+1), 
    plt.imshow(image[i], 'gray')
    #plt.imshow(image[i], c_map='hot')
    plt.title(title_m[i])
    

plt.show()
