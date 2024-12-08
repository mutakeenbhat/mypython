import numpy as np
from PIL import Image as im
# creating three channels 
# red=np.full((512,512),255,dtype='uint8')
# green=np.full((512,512),0,dtype='uint8')
# blue=np.full((512,512),0,dtype='uint8')
# # stacking three channels 
# arr=np.stack((red,green,blue),axis=-1)
# # converting an image into array
# img=im.fromarray(arr)
# img.show()
# print(red)
#i=im.open(r'C:\\Users\\MUTAKEEN\\Pictures\\Saved Pictures.\\family.jpg')
# i.show()
# converting an image into array
# img=np.array(i)
# print(img)
# print(i.size)
# # adding a alpha channel to make the picture blur
# opc=np.full((img.shape[0], img.shape[1]),100,dtype='uint8') 
#  #need to use img.shape[0]This ensures opc matches the height and width of the loaded image.
# st_arr=np.stack((img[:,:,0],img[:,:,1],img[:,:,2],opc),axis=-1)
# st_img=im.fromarray(st_arr,mode='RGBA') #When creating the new image from the array, use RGBA mode since you’re adding an alpha channel.
# st_img.show()
# arr=np.dstack(img,opc)
# WEIGHTED BLENDING
i=im.open(r'C:\\Users\\MUTAKEEN\\Pictures\\Saved Pictures.\\family.jpg')
# i.show()
i2=im.open(r'C:\\Users\\MUTAKEEN\\Pictures\\Saved Pictures.\\kuttu.jpg')
# i2.show()
i=np.resize(i,(2268,4032))
i2=np.resize(i2,(2268,4032))
print(i.size)
print(i2.size)
img=np.array(i)
img2=np.array(i2)
blended_img=0.5*img+0.8*img2
print(blended_img)
blended_img=im.fromarray(blended_img)
blended_img.show()
