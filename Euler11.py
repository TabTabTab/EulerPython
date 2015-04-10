import IOMaestro
import NumericsMaestro
fileName="Input/EulerInput11.txt"
matrix= IOMaestro.readToIntMatrix(fileName)
for val in matrix:
	print val
print "------------"
xMax= len(matrix)
yMax=len(matrix[0])
seqLength=4
#directions to check: down, diagdownRight,diagDownLeft, right

valList=[]
arrays=[]
for y in xrange(0,yMax):
	checkDown = y<=yMax-seqLength
	for x in xrange(0,xMax):
		checkRight = x<=xMax-seqLength
		checkDiagSE=checkRight & checkDown
		checkDiagSW=checkDown & x>=(seqLength-1)
		if checkRight:
			riArray=matrix[y][x:x+seqLength]
			valList.append(NumericsMaestro.product(riArray))
			arrays.append(riArray)
		if checkDown:
			doArray=map(lambda line: line[x],matrix[y:y+seqLength])
			valList.append(NumericsMaestro.product(doArray))
			arrays.append(doArray)

		if checkDiagSE:
			diArray=[]
			currentX=x;
			currentY=y;
			for i in xrange(0,seqLength):
				diArray.append(matrix[currentY][currentX])
				currentX,currentY=currentX+1,currentY+1
			valList.append(NumericsMaestro.product(diArray))
			arrays.append(diArray)
		if checkDiagSW:
			diArray=[]
			currentX=x;
			currentY=y;
			for i in xrange(0,seqLength):
				diArray.append(matrix[currentY][currentX])
				currentX,currentY=currentX-1,currentY+1
			valList.append(NumericsMaestro.product(diArray))
			arrays.append(diArray)
			
maxVal= max(valList)
for i in xrange(0,len(valList)):
	if valList[i]==maxVal:
		print maxVal
		print "the array is"
		print i
		print arrays[i]

