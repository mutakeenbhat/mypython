import numpy as np
# ARRAY CREATION
arr=np.array([0,1,2,4,5,6,7,8,9])
# print(arr)
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2)
# arr3=np.array([[[1,2,3],[4,5,6],[8,9,10]],[[5,8,6],[6,2,9],[3,5,5]],[[4,5,8],[2,8,5],[3,4,1]]])
arr33=np.random.rand(3,3,3,)
# print(arr33)
arr6=np.array([1,2,3,4,5],ndmin=5)
# print(arr6.ndim)
arr4=np.zeros((4,5))
# print(arr4)
arr5=np.ones((3,2))
# print(arr5)
# slicing and indexing
# question 1
# print(arr2[1])
# print(arr2[0:3,2])
# print(arr2[1:3,0:2])
# question 2
# print(arr3[0])
# print(arr3[1:2,0:2,0:2]) 
# broadcasting
# q1
# add_arr=arr+5
# print(add_arr)
# q2
# mul_arr2=arr2*2
# print(mul_arr2)
# q3
# a1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# # print(a1.shape)
# a2=np.array([1,2,3,4])
# sum=a1+a2
# print(sum)
# manipualting 3d arrays
# q1
new=np.random.rand(4,4,4)
# new.np.random.uniform(0,1,size=(4,4,4))
# print(new.shape)
processed_array = np.where(new > 0.5, 1, 0) #replacing the elements 0.5 with 1 and others with 0
# print(new)
# print(processed_array)
# q2
# print(sum(processed_array))
# print(sum(new))
# q3
# compute_mean=processed_array.mean(axis=2)
# compute_mean2=new.mean(axis=2)
# print(compute_mean)
# print(compute_mean2)
# reshaping
# reshaping_arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(reshaping_arr.reshape(3,4))
# advanced examples?
ar1=np.array([1,2,3,4,5])
ar2=np.array([5,4,3,2,1])
# sum=sum(ar1,ar2)
# print(sum)
# diiv=ar1/ar2
# print(diiv)
# diff=ar1-ar2
# print(diff)
# product=ar1*ar2
# print(product)
# q2 dot product of two arrays
# dotproduct=np.dot(ar1,ar2)
# print(dotproduct)
# max,min,mean
# print(np.max(arr2))
# print(np.min(arr2))
# print(np.mean(arr2))
# PARTB
# new_d=np.random.randint(0,10,size=(2,3,4))
# print(new_d)
# swaped=np.swapaxes(new_d,0,1)
# print(swaped.shape)
# flatten=new_d.reshape(-1)
# print(flatten)