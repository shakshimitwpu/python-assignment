import numpy as np
arr1=np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
arr2=np.array([[9, 8, 7, 4],[3, 12, 4, 8]])
arr3=arr1+arr2
print("Matrix A= ",arr1)
print("Matrix B= ",arr2)
print("Addition of two matrices: ",arr3)
arr4=np.array([[[1,2,3],[4,5,6]],[[6,7,8],[9,10,11]]])
arr5=np.array([[[16,17,18],[15,16,17]],[[3,4,5],[7,8,9]]])
arr6=arr4+arr5
print("Matrix C= ",arr4)
print("Matrix D= ",arr5)
print("Addition of two matrices= ",arr6)