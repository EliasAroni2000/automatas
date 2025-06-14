estadoFinal = "estado final"
estadoNoFinal = "estado no final"
estadoTrampa = "estado trampa"


def tokenId(lexema):
    letras =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
             'w','x','y','z','A','B','C','D''E','F','G','H''I','J','K','L''M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z']
    letraNumeros = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
             'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L''M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    estado = 0
    estadoFinal = [1]
    ##para obtener la longitud de la cadena
    logitud = len(lexema)
    ##empieza en 1, ya que se tiene en cuenta el primer ciclo
    cantidad = 1
    
    ##consulto que el primer caracter sea una letra mayuscula o minuscula
    for i in range(0,len(letras)):
        if letras[i] == lexema[0]:
            estado = 1
            
    if estado == 1:
        ##el ciclo empieza en 1, por ciclo for anterior, resta comprobar el resto de la cadena
        for i in range(1,len(lexema)):
            for j in range(0,len(letraNumeros)):
                if letraNumeros[j] == lexema[i]:
                    cantidad = cantidad + 1
                    print(letraNumeros[j])
    
    if cantidad == logitud:
        estado = 1
    else:
        estado = 2
    
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
        
    return aux
           
    

def tokenNumero(lexema):
    estado = 0
    cantidad = 1
    estadoFinal = [0,1]
    caracteres = ['0','1','2','3','4','5','6','7','8','9']
    
    if lexema[0] == '-':
        estado = 1
        
    for i in range(0,len(caracteres)):
        if lexema[0] == caracteres[i]:
            estado = 0
    print(estado)
    
    for i in range(1,len(lexema)):
        for j in range(0,len(caracteres)):
            if lexema[i] == caracteres[j]:
                cantidad = cantidad + 1
                print(lexema[i])
    
    
    if cantidad != len(lexema):
        estado = 2 
                  
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
        
    return aux
            
def tokenPunto(lexema):
    estado = 0
    estadoFinal = [1]
    
    if lexema == '.':
        estado = 1
    else:
        estado = 2
        
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux

def tokenVar(lexema):
    estado = 0
    estadoFinal = [3]
    longitudCadena = len(lexema)
    
    if longitudCadena != 3:
        estado = 4
    else:
        if lexema[0] == 'v':
            estado = 1
        else: 
            estado = 4
        if lexema[1] == 'a' and estado==1:
            estado = 2
        else: 
            estado = 4
        if lexema[2] == 'r' and estado == 2:
            estado = 3
        else: 
            estado = 4 
         
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux


def tokenProgram(lexema):
    estado = 0
    estadoFinal = [7]
    longitudCadena = len(lexema)
    
    if longitudCadena != 7:
        estado = 8
    else:
        if lexema[0] == 'p':
            estado = 1
        else: 
            estado = 8
        if lexema[1] == 'r' and estado == 1:
            estado = 2
        else: 
            estado = 8
        
        if lexema[2] == 'o' and estado == 2:
            estado = 3
        else: 
            estado = 8
        if lexema[3] == 'g'and estado ==3 :
            estado = 4
        else: 
            estado = 8
        if lexema[4] == 'r' and estado==4:
            estado = 5
        else: 
            estado = 8
        
        if lexema[5] == 'a' and estado == 5:
            estado = 6
        else: 
            estado = 8
        if lexema[6] == 'm' and estado ==6:
            estado = 7
        else: 
            estado = 8
        
      
         
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux

def tokenPuntoComa(lexema):
    estado = 0
    estadoFinal = [1]
    
    if len(lexema)!=1:
        estado = 2
    else:
        if lexema == ';':
            estado = 1
        else:
            estado = 2
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux   

def tokenAsignacion(lexema):
    estado = 0
    estadoFinal = [1]
    
    if len(lexema)!=1:
        estado = 2
    else:
        if lexema == '=':
            estado = 1
        else:
            estado = 2
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux

def tokenBegin(lexema):
    estado = 0
    estadoFinal = [5]
    longitudCadena = len(lexema)
    
    if longitudCadena != 5:
        estado = 6
    else:
        if lexema[0] == 'b':
            estado = 1
        else: 
            estado = 6
        if lexema[1] == 'e' and estado == 1:
            estado = 2
        else: 
            estado = 6
        
        if lexema[2] == 'g' and estado == 2:
            estado = 3
        else: 
            estado = 6
        if lexema[3] == 'i'and estado ==3 :
            estado = 4
        else: 
            estado = 6
        if lexema[4] == 'n' and estado==4:
            estado = 5
        else: 
            estado = 6
        
         
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux

def tokenEnd(lexema):
    estado = 0
    estadoFinal = [3]
    longitudCadena = len(lexema)
    
    if longitudCadena != 3:
        estado = 4
    else:
        if lexema[0] == 'e':
            estado = 1
        else: 
            estado = 4
        if lexema[1] == 'n' and estado == 1:
            estado = 2
        else: 
            estado = 4
        
        if lexema[2] == 'd' and estado == 2:
            estado = 3
        else: 
            estado = 4
        
         
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
        
    return aux
    
    
def tokenEspacioBlanco(lexema):
    estado = 0
    estadoFinal=[1]
    
    if lexema == " ":
        estado = 1
    else: 
        estado = 2
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux

def tokenInt(lexema):
    estado = 0
    estadoFinal = [3]
    
    if len(lexema)!=3:
        estado = 4
    else:
        if lexema[0] == 'i':
            estado = 1
        else: 
            estado = 4
        if lexema[1] == 'n' and estado == 1:
            estado = 2
        else: 
            estado = 4
        
        if lexema[2] == 't' and estado == 2:
            estado = 3
        else: 
            estado = 4
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux
        
def tokenBool(lexema):
    estado = 0
    estadoFinal = [4]
    
    if len(lexema)!=4:
        estado = 5
    else:
        if lexema[0] == 'b':
            estado = 1
        else: 
            estado = 5
        if lexema[1] == 'o' and estado == 1:
            estado = 2
        else: 
            estado = 5
        
        if lexema[2] == 'o' and estado == 2:
            estado = 3
        else: 
            estado = 5
        if lexema[3] == 'l' and estado == 3:
            estado = 4
        else: 
            estado = 5
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux
     
def tokenTrue(lexema):
    estado = 0
    estadoFinal = [4]
    
    if len(lexema)!=4:
        estado = 5
    else:
        if lexema[0] == 't':
            estado = 1
        else: 
            estado = 5
        if lexema[1] == 'r' and estado == 1:
            estado = 2
        else: 
            estado = 5
        
        if lexema[2] == 'u' and estado == 2:
            estado = 3
        else: 
            estado = 5
        if lexema[3] == 'e' and estado == 3:
            estado = 4
        else: 
            estado = 5
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux

def tokenNot(lexema):
    estado = 0
    estadoFinal = [3]
    
    if len(lexema)!=3:
        estado = 4
    else:
        if lexema[0] == 'n':
            estado = 1
        else: 
            estado = 4
        if lexema[1] == 'o' and estado == 1:
            estado = 2
        else: 
            estado = 4
        
        if lexema[2] == 't' and estado == 2:
            estado = 3
        else: 
            estado = 4
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux

def tokenFalse(lexema):
    estado = 0
    estadoFinal = [5]
    
    if len(lexema)!=5:
        estado = 6
    else:
        if lexema[0] == 'f':
            estado = 1
        else: 
            estado = 6
        if lexema[1] == 'a' and estado == 1:
            estado = 2
        else: 
            estado = 6
        
        if lexema[2] == 'l' and estado == 2:
            estado = 3
        else: 
            estado = 6
        if lexema[3] == 's' and estado == 3:
            estado = 4
        else: 
            estado = 6
        if lexema[4] == 'e' and estado == 4:
            estado = 5
        else: 
            estado = 6
        
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux       

def tokenGoto(lexema):
    estado = 0
    estadoFinal = [4]
    
    if len(lexema)!=4:
        estado = 5
    else:
        if lexema[0] == 'g':
            estado = 1
        else: 
            estado = 5
        if lexema[1] == 'o' and estado == 1:
            estado = 2
        else: 
            estado = 5
        
        if lexema[2] == 't' and estado == 2:
            estado = 3
        else: 
            estado = 5
        if lexema[3] == 'o' and estado == 3:
            estado = 4
        else: 
            estado = 5
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux      

def tokenLet(lexema):
    estado = 0
    estadoFinal = [3]
    
    if len(lexema)!=3:
        estado = 4
    else:
        if lexema[0] == 'l':
            estado = 1
        else: 
            estado = 4
        if lexema[1] == 'e' and estado == 1:
            estado = 2
        else: 
            estado = 4
        
        if lexema[2] == 't' and estado == 2:
            estado = 3
        else: 
            estado = 4
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux   

def tokenOperadorS(lexema):
    estado = 0
    estadoFinal = [1]
    
    if len(lexema)!=1:
        estado = 2
    else:
        if lexema == '+':
            estado = 1
        else:
            estado = 2
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux

def tokenOperadorR(lexema):
    estado = 0
    estadoFinal = [1]
    
    if len(lexema)!=1:
        estado = 2
    else:
        if lexema == '-':
            estado = 1
        else:
            estado = 2
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux

def tokenOperadorP(lexema):
    estado = 0
    estadoFinal = [1]
    
    if len(lexema)!=1:
        estado = 2
    else:
        if lexema == '*':
            estado = 1
        else:
            estado = 2
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux

def tokenOperadorOr(lexema):
    estado = 0
    estadoFinal = [2]
    
    if len(lexema)!=2:
        estado = 3
    else:
        if lexema[0] == 'o':
            estado = 1
        else: 
            estado = 3
        if lexema[1] == 'r' and estado==1:
            estado = 2
        else:
            estado = 3
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux    

def tokenOperadorAnd(lexema):
    estado = 0
    estadoFinal = [3]
    
    if len(lexema)!=3:
        estado = 4
    else:
        if lexema[0] == 'a':
            estado = 1
        else: 
            estado = 3
        if lexema[1] == 'n' and estado==1:
            estado = 2
        else:
            estado = 3
        if lexema[2] == 'd' and estado==2:
            estado = 3
        else:
            estado = 4
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux  

def tokenIf(lexema):
    estado = 0 
    estadoFinal = [2]
    if len(lexema) !=2:
        estado = 3
    else: 
        if lexema[0] == 'i':
            estado = 1
        else:
            estado = 3 
        if lexema[1] =='f' and estado ==1:
            estado = 2
        else: 
            estado = 3
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada"
    return aux   

def tokenElse(lexema):
    estado = 0
    estadoFinal = [4]
    
    if len(lexema)!=4:
        estado = 5
    else:
        if lexema[0] == 'e':
            estado = 1
        else: 
            estado = 5
        if lexema[1] == 'l' and estado == 1:
            estado = 2
        else: 
            estado = 5 
        if lexema[2] == 's' and estado == 2:
            estado = 3
        else: 
            estado = 5
        if lexema[3] == 'e' and estado == 3:
            estado = 4
        else: 
            estado = 5          
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux      

def tokenDobleIgual(lexema):
    estado = 0
    estadoFinal = [2]
    if len(lexema)!= 2:
        estado = 3
    else:
        if lexema[0] == '=':
            estado = 1
        else:
            estado = 3
        if lexema[1] == '=':
            estado = 2  
        else:
            estado = 3
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux  
     
def tokenCierre(lexema):
    estado = 0
    estadoFinal = [2]
    
    if len(lexema)!=2:
        estado = 3
    else:
        if lexema[0] == '<':
            estado = 1
        else: 
            estado = 3
        if lexema[1] == '>' and estado == 1:
            estado = 2
        else: 
            estado = 3
         
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux      
def tokenMenor(lexema):
    estado = 0
    estadoFinal = [1]
    if lexema == '<':
        estado = 1
    else:
        estado = 2
        
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux      
def tokenMayor(lexema):
    estado = 0
    estadoFinal = [1]
    if lexema == '>':
        estado = 1
    else:
        estado = 2
        
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux 

def tokenMenorIgual(lexema):
    estado = 0
    estadoFinal = [2]
    if len(lexema)!=2:
        estado = 3
    else:
        if lexema[0] == '<':
            estado = 1
        else: 
            estado = 3
        if lexema[1] == '=' and estado ==1:
            estado = 2
        else:
            estado = 3
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux 

def tokenMayorIgual(lexema):
    estado = 0
    estadoFinal = [2]
    if len(lexema)!=2:
        estado = 3
    else:
        if lexema[0] == '>':
            estado = 1
        else: 
            estado = 3
        if lexema[1] == '=' and estado == 1:
            estado = 2
        else:
            estado = 3
            
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux 

def tokenParentesisAbre(lexema):
    estado = 0
    estadoFinal = [1]
    if lexema == '(':
        estado = 1
    else:
        estado = 2
        
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux 

def tokenParentesisCierra(lexema):
    estado = 0
    estadoFinal = [1]
    if lexema == ')':
        estado = 1
    else:
        estado = 2
        
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux 

def tokenDosPuntos(lexema):
    estado = 0
    estadoFinal = [1]
    if lexema == ':':
        estado = 1
    else:
        estado = 2
        
    if estado in estadoFinal:
        aux = "cadena aceptada"
    else:
        aux = " cadena no aceptada" 
    return aux 

posiblesTokens = [("id",tokenId),("num",tokenNumero),("punto",tokenPunto),("var",tokenVar),
                  ("program",tokenProgram),("puntoComa",tokenPuntoComa),("asignacion",tokenAsignacion),
                  ("begin", tokenBegin),("end",tokenEnd),("espacioBlanco",tokenEspacioBlanco),
                  ("int",tokenInt),("bool",tokenBool),("true",tokenTrue),("not",tokenNot),
                  ("false",tokenFalse),("goto",tokenGoto),("let",tokenLet),("operadorS",tokenOperadorS),
                  ("operadorR",tokenOperadorR),("operadorP",tokenOperadorP),
                  ("operadorOR",tokenOperadorOr),("operadorAnd",tokenOperadorAnd),
                  ("if",tokenIf),("else",tokenElse),("dobleIgual",tokenDobleIgual),
                  ("cierre",tokenCierre), ("menor",tokenMenor),("mayor",tokenMayor),
                  ("menorIgual",tokenMenorIgual),("mayorIgual",tokenMayorIgual),
                  ("parentesisAbre",tokenParentesisAbre),("parentesisCierra",tokenParentesisCierra),
                  ("dospuntos",tokenDosPuntos)]

def iniciar(cadena):
    tokens = [] 
    posicion_actual = 0 
    cadenaAnterior = ""
    i = 0
    while posicion_actual < len(cadena)+1:
        if cadena[i] != " ":
            cadenaAnterior = cadenaAnterior + cadena[i] 
        else:
            if cadenaAnterior != "":
                token_hallado = False
                for (nombreToken,automata) in posiblesTokens:
                    if automata(cadenaAnterior):
                        tokens.append((nombreToken,cadenaAnterior))
                        print(tokens[0])
                        token_hallado = True
                        break
        i = i +1
                
            
            
    
    
    
##################Program Principal#########################################
iniciar("<> ")
        
