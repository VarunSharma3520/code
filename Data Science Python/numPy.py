
import numpy as np

#? Array has homogenous memory allocation


#! Creating array in np
# l1 = [1, 2, 3, 4]
# print(np.array(l1))
# print('shape: ', np.array(l1).shape)
# print('size: ', np.array(l1).size)
# print('type: ', np.array(l1).dtype)
# print('dtype: ',np.array(l1).dtype)


# print(type(np.array(l1)))

#! numpy array intialise
# print(np.zeros((5,4),dtype=int)) # ((rows,column))
# print(np.full((4, 4),10 , dtype=int))  # ((rows,column))
# print(np.ones((2,2)))
# print(np.arange(10,51,5)) # start stop step
# print(np.linspace(10, 51, 5))  # creates linear space between start stop space

#! random interger in numpy
# print(np.random.randint(1,100,5)) # start end total_num

#! shape And re-shaping in np
# print(np.array(l1).shape)
# np.array(l1).shape = (2,2)
# print(l1)

#! joining numpy array
# l1 = np.array([10, 20, 30, 40, 50])
# l2 = np.array([40, 50, 60, 70, 80])
# print(np.vstack((l1,l2)))
# print(np.hstack((l1,l2)))
# print(np.column_stack((l1,l2)))

#! intersection in np
# print(np.intersect1d(l1,l2))
# print(np.setdiff1d(l2,l1))

#! sum in np
# print(np.sum([l1, l2]))
# print(np.sum([l1, l2], axis=0))
# print(np.sum([l1, l2], axis=1))

#! basic arthematic in np
# l3 = l2+1
# l4 = l2-1
# l5 = l2*2
# l6 = l2/2
# print(l3, l4, l5, l6)

#! basic statics in np
# l7 = np.mean(l1)
# l8 = np.median(l1)
# l9 = np.std(l1)
# print(l7, l8, l9)

#! save & load np arry
# l10 = np.save('numbu',l1)
# l11 = np.load('numbu.npy')
# print(l11)

#! element-wise operation on mulitiple arrays
la = np.array([3,7,9,1])
ka = np.array([4,8,10,2])
ta = la +ka
# print(ta)

#! max, sum, mean, min, cumsum
# print(ta.max(axis = 0))
# print(ta.min())
# print(ta.mean())
# print(ta.sum())
# print(ta.sort())
# print(ta.cumsum())

#! random with numpy
# print(np.random.choice(ta))
# print(np.random.choice(ta,2))
# print(np.random.choice(ta,(2,3)))
# print(np.random.randn(3,3))
# print(np.random.randint(2,5))
# print(np.random.uniform(2,4,(3,3)))
# print(np.random.uniform((3,10,1)))
# print(np.random.randrange())