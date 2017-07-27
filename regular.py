# coding: utf-8
import re
N1 = re.compile('(h|H)ola|HOLA|(Q|q)u(e|é)\stal|QU(É|E)\sTAL|((B|b)uenas)|BUENAS|(Q|q)u(e|é)\sonda|QU(E|É)\sONDA|(H|h)ello|HELLO|(H|h)i|HI|(Q|q)iubo|QUIUBO|(S|s)aludos|SALUDOS|(B|b)uenos\sd(i|í)as|BUENOS\sD(I|Í)AS')
N2 = re.compile('(H|h)asta\sluego|HASTA\sLUEGO|(A|a)di(o|ó)s|ADI(O|Ó)S|(N|n)os\svemos|NOS\sVEMOS|(C|c)hao|CHAO|(B|b)ye|BYE')