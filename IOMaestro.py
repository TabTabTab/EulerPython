import sys


#def readToIntMatrix(fileName):
#	with open(fileName) as f:
 #   	content = f.readlines();


def readToIntMatrix(fileName):
	with open(fileName) as f:
		strippedMatrix=map(lambda line: line.strip().split(" "),f)
		integerMatrix=map (lambda intList: map(int,intList),strippedMatrix)
		return integerMatrix





