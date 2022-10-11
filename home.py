import numpy as np
import random
import cv2

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
image = cv2.imread('D:\\MANU.jpeg',1)
[mr,mc,md]=image.shape
if md>1:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    gray = image
noise_image = sp_noise(gray,0.05)
data_final = np.zeros((len(noise_image),len(noise_image[0])))
#print(len(noise_image),len(noise_image[0]))
data_final = noise_image
#for x in range (1,(len(noise_image)+1)):
#    for y in range (1,(len(noise_image[0])+1)):
#         data_final[x-1][y-1] = noise_image[x-1][y-1]
#print(data_final)
#data_noise_padding = np.zeros((len(noise_image)+2,len(noise_image[0])+2))
#[mr1,mc1] = data_noise_padding.shape
  
#print(data_noise_padding.shape)
#for x in range (mr1):
#  for y in range (mc1):
        #print(data_noise_padding[x][y])
#        data_noise_padding[x][y] = data_final[x-1][y-1]
#data_noise_padding [(1):-(-1),(1):-(-1)] = noise_image
top = bottom = 1
left = right = 1
data_noise_padding = cv2.copyMakeBorder(noise_image,top,bottom,left,right,cv2.BORDER_CONSTANT)
print(data_noise_padding.shape)

for i in range (1,len(data_noise_padding)-1): 
    for j in range (1,len(data_noise_padding[0])-1):
       
        kernal = [data_noise_padding[i-1][j-1],data_noise_padding[i-1][j],data_noise_padding[i-1][j+1],data_noise_padding[i][j-1],data_noise_padding[i][j],data_noise_padding[i][j+1],data_noise_padding[i+1][j-1],data_noise_padding[i+1][j],data_noise_padding[i+1][j+1]]
        if (data_noise_padding[i][j]==0) or (data_noise_padding[i][j]==255):
         kernal.sort()
         data_final[i-1][j-1]= kernal[len(kernal) // 2]
        #kernal=[]
        else:
            data_final[i-1][j-1]=data_noise_padding[i][j]
#  temp = np.reshape(kernal,(3,3))
        #print(temp)
#        for k in range (1,mr+1):
#           for l in range (1,mc+1):
#              if temp[2][2]==0 or 255:
                #median = cv2.medianBlur(temp,9)
#                kernal.sort()
#                data_final[k][l]= kernal[len(kernal) // 2]
#                kernal=[]
#              else:
#                data_final[k][l]= data_final[k][l]
            
        #median = cv2.medianBlur(temp,3)
        #kernal = []
            
   


#cv2.imwrite('input image', image)

cv2.imshow('input image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('after adding noise', noise_image)

cv2.imshow('after adding noise', data_noise_padding)
cv2.waitKey(0)
cv2.destroyAllWindows()
#removed_noise = median_filter(noise_image) 
cv2.imshow('final image',data_final)
cv2.waitKey(0)
cv2.destroyAllWindows()