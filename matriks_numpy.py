import numpy as np

def soal1():
	a = np.matrix([[3, -2], [4, -1]])
	b = np.matrix([[4, 3], [-2, -1]])
	c = np.matrix([[4, 10], [9, 12]])

	res = np.linalg.det((a.dot(b)) - c)
	print "jawaban no.1 : \n", res

def soal2():
	a = np.matrix([[-5, 3], [-2, 1]])
	b = np.matrix([[1, -1], [1, -3]])

	res = np.linalg.inv(a.dot(b))
	print "jawaban no.2 : \n", res

def soal3():
	a = np.matrix([[4, -3], [-1, 5]])
	b = np.matrix([[7, 18], [-6, 21]])

	res = (np.linalg.inv(a)).dot(b)
	print "jawaban no.3 : \n", res

def soal4():
	a = np.matrix([[1, 2], [3, 4]])
	b = np.matrix([[1, 1], [0, 1]])
	c = np.matrix([[2, 5], [3, 7]])

	res = np.linalg.det((a.dot(b)+c))
	print "jawaban no.4 : \n", res

def soal5():
	A = np.matrix([[2, -1], [3, 4]])
	C = np.matrix([[1, 2], [-1, 3]])
	res = np.matrix([[10, 25], [5, 28]])

	for i in range (12) :
		for z in range (12) :
			B = np.matrix([[(i-1), 1], [3, z]])
			cal = A+(2*B*C) 
			cal.astype(int)
			res.astype(int)
			if np.linalg.det(cal) == np.linalg.det(res) :
				#print np.linalg.det(cal), " ", np.linalg.det(res)
				print "Jawaban no.5 :\n", i+z

def soal7():
	x = -2
	for i in range (10):
		A = np.matrix([[(2*x) + 1, 3], [(6*x)-1, 5]])
		res = np.linalg.det(A)
		#print res.astype(int)
		if res.astype(int) == 0 :
			print "Jawaban no.7 : \n", x
			break
		x+=1

def soal8():
	C = np.matrix([[4, -1], [-1, 2]])
	B = np.matrix([[28, 14], [14, 56]])
	A = np.linalg.inv(C)

	res = np.linalg.det(A.transpose().dot(B))
	print "Jawaban no.8 : \n", res

def soal9():
	A = np.matrix([[-2, 4], [3, 1]])
	B = np.matrix([[5, 3], [1, 2]])

	res = np.linalg.det(A*B)
	print "Jawbaan no.9 : \n", res

def soal12():
	finalResult = []
	for i in range (22):
		for z in range (22):
			A = np.matrix([[3, z], [5, -1]])
			B = np.matrix([[i, 5], [-3, 6]])
			C = np.matrix([[-3, -1], [z, 9]])
			res = np.matrix([[8, 5*i], [-i, -4]])

			if (np.linalg.det(A+B-C).astype(int) == np.linalg.det(res).astype(int)) :
				finalResult.append((2*i*z)+z)
	print "Jawaban no.12 : \n", finalResult

def soal14():
	x = -2
	A = np.matrix([[2, 1], [-1, 3]])
	C = np.matrix([[2, -1], [1, 1]])
	D = np.matrix([[0, 1], [2, 4]])

	for i in range (10):
		B = np.matrix([[-6, 2*x], [4, -1]])
		if np.linalg.det((2*A)+B).astype(int) == np.linalg.det(C*D).astype(int):
			print "Jawaban no.14 : \n", x
			break
		x+=1

soal1()
soal2()
soal3()
soal4()
soal5()
soal7()
soal8()
soal9()
soal12()
soal14()