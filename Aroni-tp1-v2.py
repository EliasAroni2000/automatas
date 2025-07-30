estado_final = "estado final"
estadoNoFinal = "estado no aceptado"
estadoTrampa = "estado trampa"

def tokenId(lexema):
    caracterAceptado = {0:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,
                               'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,
                               'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,
                               'y':1,'z':1,'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
                               'I':1,'J':1,'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,
                               'Q':1,'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,
                               'Y':1,'Z':1},
                        1:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,
                               'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,
                               'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,
                               'y':1,'z':1,'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
                               'I':1,'J':1,'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,
                               'Q':1,'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,
                               'Y':1,'Z':1,'0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,
                               '8':1,'9':1},
                   }
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if caracter in caracterAceptado[estado]:
            estado = caracterAceptado[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenNumero(lexema):
    vectorNumero = {0:{'0':1,'1':1,'2':1,'3':1,'4':1,'5':1,
                       '6':1,'7':1,'8':1,'9':1},
                    1:{'0':1,'1':1,'2':1,'3':1,'4':1,'5':1,
                       '6':1,'7':1,'8':1,'9':1}
                       }
    estado = 0
    estadoFinal = [1,2]
    for caracter in lexema:
        if caracter in vectorNumero[estado]:
            estado = vectorNumero[estado][caracter]
        else:
            estado = -1
            break 

    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenAsignacion(lexema):
    estado = 0
    estadoFinal =[1]
    vector = ['=']
##cantidad de estado 2
    if lexema in vector[estado]:
        estado = 1
    else:
        estado = -1

    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenPunto(lexema):
    estado = 0
    estadoFinal =[1]
    vector = ['.']
##cantidad de estado 2
    if lexema in vector[estado]:
        estado = 1
    else:
        estado = -1

    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenVar(lexema):
    estado = 0
    estadoFinal = [3]
    caracter = {0:{'v':1},1:{'a':2},2:{'r':3},3:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal
def tokenProgram(lexema):
    estado = 0
    estadoFinal = [7]
    caracter = {0:{'p':1},1:{'r':2},2:{'o':3},3:{'g':4},4:{'r':5},
                5:{'a':6},6:{'m':7},7:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenPuntoComa(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{';':1},1:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenBegin(lexema):
    estado = 0
    estadoFinal = [5]
    caracter = {0:{'b':1},1:{'e':2},2:{'g':3},3:{'i':4},4:{'n':5},
                5:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenEnd(lexema):
    estado = 0
    estadoFinal = [3]
    caracter = {0:{'e':1},1:{'n':2},2:{'d':3},3:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenInt(lexema):
    estado = 0
    estadoFinal = [3]
    caracter = {0:{'i':1},1:{'n':2},2:{'t':3},3:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenBool(lexema):
    estado = 0
    estadoFinal = [4]
    caracter = {0:{'b':1},1:{'o':2},2:{'o':3},3:{'l':4},4:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenTrue(lexema):
    estado = 0
    estadoFinal = [4]
    caracter = {0:{'t':1},1:{'r':2},2:{'u':3},3:{'e':4},4:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenNot(lexema):
    estado = 0
    estadoFinal = [3]
    caracter = {0:{'n':1},1:{'o':2},2:{'t':3},3:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenFalse(lexema):
    estado = 0
    estadoFinal = [5]
    caracter = {0:{'f':1},1:{'a':2},2:{'l':3},3:{'s':4},4:{'e':5},
                5:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenGoto(lexema):
    estado = 0
    estadoFinal = [4]
    caracter = {0:{'g':1},1:{'o':2},2:{'t':3},3:{'o':4},4:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenLet(lexema):
    estado = 0
    estadoFinal = [3]
    caracter = {0:{'l':1},1:{'e':2},2:{'t':3},3:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenOperadoSuma(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{'+':1},1:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal
def tokenOperadoResta(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{'-':1},1:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal
def tokenOperadoProducto(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{'*':1},1:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenOperadoOr(lexema):
    estado = 0
    estadoFinal = [2]
    caracter = {0:{'o':1},1:{'r':2},2:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado =-1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal
def tokenOperadoAnd(lexema):
    estado = 0
    estadoFinal = [3]
    caracter = {0:{'a':1},1:{'n':2},2:{'d':3},3:{}}  
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenIf(lexema):
    estado = 0
    estadoFinal = [2]
    caracter = {0:{'i':1},1:{'f':2},2:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenElse(lexema):
    estado = 0
    estadoFinal = [4]
    caracter = {0:{'e':1},1:{'l':2},2:{'s':3},3:{'e':4},4:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenDobleIgual(lexema):
    estado = 0
    estadoFinal = [2]
    caracter = {0:{'=':1},1:{'=':2},2:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal
def tokenDesigual(lexema):
    estado = 0
    estadoFinal = [2]
    caracter = {0:{'<':1},1:{'>':2},2:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenMayor(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{'>':1},1:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenMenor(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{'<':1},1:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenMenorIgual(lexema):
    estado = 0
    estadoFinal = [2]
    caracter = {0:{'<':1},1:{'=':2},2:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenMayorIgual(lexema):
    estado = 0
    estadoFinal = [2]
    caracter = {0:{'>':1},1:{'=':2},2:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenDosPuntos(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{':':1},1:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenAbreParentesis(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{'(':1},1:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal

def tokenCierraParentesis(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{')':1},1:{}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado == -1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal
def tokenEspacioBlanco(lexema):
    estado = 0
    estadoFinal = [1]
    caracter = {0:{'\t':1,' ':1,'\n':1},1:{'\t':1,' ':1,'\n':1}}
    for c in lexema:
        if c in caracter[estado]:
            estado = caracter[estado][c]
        else:
            estado = -1
            break
    if estado ==-1:
        return estadoTrampa
    if estado in estadoFinal:
        return estado_final
    else:
        return estadoNoFinal
    

TOKENS_POSIBLES = [("punto",tokenPunto),
                   ("var",tokenVar),("program",tokenProgram),("puntoComa",tokenPuntoComa),
                   ("asignacion",tokenAsignacion),("begin",tokenBegin),("end",tokenEnd),
                   ("int",tokenInt),
                   ("bool",tokenBool),("true",tokenTrue),("not",tokenNot),
                   ("false",tokenFalse),("goto",tokenGoto),("let",tokenLet),
                   ("suma",tokenOperadoSuma),("resta",tokenOperadoResta),
                   ("producto",tokenOperadoProducto),("or",tokenOperadoOr),
                   ("and",tokenOperadoAnd),("if",tokenIf),("else",tokenElse),
                   ("dobleigual",tokenDobleIgual),("desigual",tokenDesigual),
                   ("menor",tokenMenor),("mayor",tokenMayor),
                   ("menorigual",tokenMenorIgual),("mayorigual",tokenMayorIgual),
                   ("abreparentesis",tokenAbreParentesis),
                   ("cierraparentesis",tokenCierraParentesis),
                   ("dospuntos",tokenDosPuntos),("numero",tokenNumero),
                   ("espacioBlanco",tokenEspacioBlanco),
                   ("id",tokenId)]



def lexer(codigo_fuente):
    tokens = [] 
    posicion_actual = 0
    posicion_a_utilizar = 0
    while posicion_actual < len(codigo_fuente):
        comienzo_lexema = posicion_actual
        posibles_tokens = []
        posibles_tokens_con_un_caracter_mas = [] 
        lexema = "" 
        var_aux_todos_en_estado_trampa = False
        
##Agrego en la condicion del while una condicion mas con un operador logico(and). Para controlar el fin de la cadena
        while var_aux_todos_en_estado_trampa == False and posicion_actual<=len(codigo_fuente):
            var_aux_todos_en_estado_trampa = True
            lexema = codigo_fuente[comienzo_lexema:posicion_actual + 1]
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []
            

            for (un_tipo_de_token, afd) in TOKENS_POSIBLES:
                simulacion_afd = afd(lexema)
                if simulacion_afd == estado_final:
                    posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token)
                    var_aux_todos_en_estado_trampa = False
                elif simulacion_afd == estadoNoFinal:
                    var_aux_todos_en_estado_trampa = False
##si luego de pasar por todos los automatas, cayo en un pozo, guardo el lexema anterior, sin el ultimo caracter con el que fue al pozo y rompo el ciclo
##como codigo_fuente[comienzo_lexema:posicion_actual] va del principio de una cadena y [] no incluye posicion_actual
            if var_aux_todos_en_estado_trampa == True:
                lexema = codigo_fuente[comienzo_lexema:posicion_actual]
                break
##para el proximo ciclo comienzo_lexema empieza en la posicion con la cual el lexema anterior cayo en el pozo
            posicion_actual = posicion_actual + 1
            
        if len(posibles_tokens) == 0:
##Supongo que tengo la cadena "program?". siendo program una palabra reservada
##cuando var_aux_todos_en_estado_trampa es Verdadero,
##por lexema = codigo_fuente[comienzo_lexema:posicion_actual] solo devuelve codigo_fuente[0:7], siendo posicion_actual = 7 cuando cae en el pozo
##sin incluir el '?'(ya que no incluye la posicion 7)
##la siguiente vuelta analizara '?' con posicion_actual = 7, entonces lexema = codigo_fuente[7:7 + 1], luego cuando se pregunte si estan todos en estado
##trampa devolvera lexema[7:7] lo cual sera una cadena vacia.
##por ello redefino la variable lexema aqui para que devuelva esa cadena no valida.
##luego incremento posicion_actual, de no hacer aqui caigo en un bucle inifinito con posicion_actual = 7
            lexema = codigo_fuente[posicion_actual]
            token = ('error',lexema)
            tokens.append(token)
            posicion_actual = posicion_actual+1
            
##como se analiza caracter a caracter de manera incremental en el ciclo, la mayoria de palabras caen en un token "id",
##luego de varias iteraciones podria caer en otra palabra reservada(token) y como en la tupla esta declarado el token "id"
##en ultima posicion, en esa ultima vuelta el token distinto a "id" que acepta la cadena, se añade al vector "posibles_tokens",
##antes que "id", por ello se toma el que esta en primera posicion
        else:
            un_tipo_de_token = posibles_tokens[0] 
            token = (un_tipo_de_token, lexema)
            tokens.append(token)
##recorrido de la lista tokens, para agregar al vector tokens2 los tokens que son distintos a 'espacioBlanco'
    tokens2 = []
    for t in tokens:
        if t[0] != 'espacioBlanco':
            tokens2.append(t)
            
    return tokens2

cadena1 = "programid\n.beginend"
cadena2 = "programid.\tbeginid:gotoid;end"
cadena3 = "programid.beginid:ifid==idgotoid;elsegotoid;"
cadena4 = "program?##++40juego.\n\tbegin valor:if 4<5 goto#verdadero;\n\telse goto falso;"
cadena5 = "program id.\n\tbegin id:if true==true goto id;\n\telse goto id;"
cadena6 = "program tarea4. begin id:if40>20goto id;else goto id;"
cadena7 = "program tarea20.var id:int(30...10)= 40; begin end"
cadena8 = "program id.var id : bool = true; begin end"
cadena9 = "program id. begin:let id = not false; begin end"
cadena10 = "program id . begin id : let valor = 40 ;\nend 1dfbfdnb"
cadena11 = "program id begin id:let valor=4+4;end"
cadena12 = "program id .begin id:if1<>1goto id; else goto id ; end"
cadena13 = "program id . begin id : if 1<=2 goto id ; else goto id ; end"

cadena14 = "program id . begin id : if 1 >= 0 goto id ; else goto id ; end"
cadena15 = "program id begin id : let valor = 4-4; end"
cadena16 = "program id begin id : let valor = 4*4 ; end"
cadena17 = "program id begin id : let valor = 4 or 5; end"
cadena18 = "program id begin id : let valor = 7 and 8; end"

print("//////cadena 1")
print(lexer(cadena1))
print("/////cadena 2")
print(lexer(cadena2))
print("////cadena 3")
print(lexer(cadena3))
print("////cadena 4")
print(lexer(cadena4))
print("////cadena 5")
print(lexer(cadena5))
print("///cadena 6")
print(lexer(cadena6))
print("////cadena 7")
print(lexer(cadena7))
print("////cadena 8")
print(lexer(cadena8))
print("////cadena 9")
print(lexer(cadena9))
print("////cadena 10")
print(lexer(cadena10))
print("////cadena 11")

print(lexer(cadena11))
print("////cadena 12")

print(lexer(cadena12))
print("////cadena 13")

print(lexer(cadena13))
print("////cadena 14")

print(lexer(cadena14))
print("////cadena 15")

print(lexer(cadena15))
print("///cadena 16")

print(lexer(cadena16))
print("///cadena 17")
print(lexer(cadena17))
print("////cadena 18")
print(lexer(cadena18))

