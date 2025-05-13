#!/usr/bin/python3
import sys, os
from math import sin, cos, pi
os.system('clear')



__tamanho_lista = 10 # numero de linhas na lista final
__velocidade_aprox = 3 # velocidade na qual x se aproxima de a
a=0 # ponto na qual x deve se aproximar cada vez mais
def f(x): # funcao a ser calculada
    '''f(x)=x^2'''
    return x**2




banner = f"Calcula limite de {f.__doc__} para x tendendo a {a}"
print( "╔"  + "═"*(len(banner)+4) + "╗")
print(f"║  "+      banner       + "  ║")
print( "╚"  + "═"*(len(banner)+4) + "╝")

if len(sys.argv) < 2:
    print(f"{sys.argv[0]} precisa de um argumento:\n",
          f"Use '{sys.argv[0]} +' para um limite pela direita\n",
          f"Use '{sys.argv[0]} -' para um limite pela esquerda.")
    quit()
try:    
    assert sys.argv[1]=="+" or sys.argv[1]=="-"    
except:
    print("O programa aceita apenas + ou - como primeiro argumento.");quit()
    
sinal = 1 if sys.argv[1]=="+" else -1
x = [a + sinal/(i**__velocidade_aprox) for i in range(2,__tamanho_lista+1)]
y = [f(a) for a in x]


Titulo = "Limite pela " + ("direita" if sys.argv[1]=="+" else "esquerda")
print(Titulo.center(len(banner)+6))
print( "╔═══════════════╦═══════════════╗".center(len(banner)+6))
print( "║       x       ║     f(x)      ║".center(len(banner)+6))
print( "╠═══════════════╬═══════════════╣".center(len(banner)+6))
for i in range(0,len(y)):
    print( f"║{str('{:.6f}').format(x[i]).center(15)}║{str('{:.6f}').format(y[i]).center(15)}║".center(len(banner)+6))
print( "╚═══════════════╩═══════════════╝".center(len(banner)+6))
    
