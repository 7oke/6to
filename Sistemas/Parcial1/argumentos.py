import sys

#argv 0 nombre del prograna
'''Este es un
comentario
multilinea'''

print(sys.argv[0])
pin = sys.argv[1]

#argv 1 primer argumento

try:
	print(sys.argv[1])
except Exception as e:
	print(e)



