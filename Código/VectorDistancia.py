# Matrices de adyasencia+costo
import struct
import numpy as np
#                           A                   B                   C                   D                   E                   F                   G                   H                   I
#                  A B C D E F G H I    A B C D E F G H I   A B C D E F G H I   A B C D E F G H I   A B C D E F G H I   A B C D E F G H I   A B C D E F G H I   A B C D E F G H I    A B C D E F G H I
matriz= np.array([[0,1,0,0,0,0,4,0,10],[1,0,9,0,8,0,0,0,0],[0,9,0,2,0,0,0,0,0],[0,0,2,0,9,4,0,0,2],[0,8,0,9,0,2,0,0,1],[0,0,0,4,2,0,0,6,0],[4,0,0,0,0,0,0,7,0],[0,0,0,0,0,6,7,0,3],[10,0,0,2,1,0,0,3,0]])

print matriz



# parte 2
print '---PARTE 2---'
e=3.0
resultado2=(a-e*d)+a
res2bin = binary(resultado2)
print 'resultado aritmetico computacional de (2) =' ,resultado2
print 'resultado aritmetico computacional de (2) en binario =' ,res2bin

zero= binary(0)
print 'representacion del 0 en binario',zero
