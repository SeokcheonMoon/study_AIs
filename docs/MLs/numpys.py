py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list
import numpy as np
np_array = np.array([[7, 8]
                    ,[9,10]
                    ,[11,12]])  # 행렬 = array

# =type 상태 확인=

type(py_list)
# <class 'list'>
type(np_array)
# <class 'numpy.ndarray'>

########################################################################################################



# list 클라스는 sum 안되는데 numpy에서는 sum이 가능하다. mean 등 나머지 기능들도 가능!


########################################################################################################



#sum 에 대한 결과가 같은데 방식을 다르게 하기

np_array.sum(axis=0)            # (1) row 단위로 sum
# array([27, 30])
np.sum(np_array,axis=0)         
# array([27, 30])

np_array.sum(axis=1)            # (2) column 단위로 sum
# array([15, 19, 23])
np.sum(np_array,axis=1)
# array([15, 19, 23])



########################################################################################################

np.array(py_list)               # py_list를 np의 array 클라스로 변경
# array([[1, 2],
#        [3, 4],
#        [5, 6]])

np_array_second = np.array(py_list)         # np array second라는 변수에 담음.

type(np_array_second)           # np array second 타입 확인
# <class 'numpy.ndarray'>

np.concatenate((np_array,np_array_second),axis=0)       # np_array와 np_array_second를 row단위로 병합
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])

np.concatenate((np_array,np_array_second),axis=1)       # np_array와 np_array_second를 column단위로 병합 
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])

######################################################################################################

# reshape() : 기존 배열을 재배열한다.
# 1차원 배열 생성
arr = np.arange(10)
print("원본 1차원 배열:")
print(arr)

arr.reshape(5,2)          # 총개수가 10면 reshape(x,y)일 때 x곱하기y는 10이어야 한다. 
# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])

arr.reshape(-1,2)         # x값이 -1이면 알아서 y에 따른 x가 자동적으로 선택된다.
# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])

pass