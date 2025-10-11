import LEXER

##No_terminales, luego de las correcciones en las producciones
VN = {"TCode","Body","DecVarList","DecVarList2","DecVar","DecVarBody",
      "DecVarBody2","Statement","StatementList", 
      "StatementList2","StatementBody", "Goto", "Assignment",
      "Assignment2","Assignment3","Op","MatOp",
      "BoolOp","Lvalue","Conditional",
      "Conditional2","CompExpr","CompOp","Rvalue"}

##Terminales
VT = {"id","program","var","puntoComa","asignacion",
      "int","bool","numero",
      "true","false", "begin","end",
      "if","else","not",
      "mayor","menor","desigual",
      "menorigual","mayorigual",
      "suma","resta",
      "producto","dobleigual",
      "abreparentesis","cierraparentesis",
      "punto","and","or","let","goto","dospuntos"}


#No terminales   : {simbolos Directrices} : cuerpo de la produccion
SD = {  "TCode" : { "program" : ["program","id","punto","Body"]},
      
        "Body"  : {"begin" : ["begin","StatementList","end"],
                  "var" : ["var","DecVar","DecVarList","begin","StatementList","end"]},

        "DecVarList" : {"tokenId": ["DecVarList2"],
                        "begin":["DecVarList2"] },

        "DecVarList2" : {"id" : ["DecVar", "DecVarList2"],
                         "begin" : []},
        "DecVar"      : {"id" : ["id","dospuntos","DecVarBody"]},

        "DecVarBody"  : {"int" : ["int","abreparentesis","numero","punto","punto","punto","numero","cierraparentesis","asignacion","numero","puntoComa"],
                         "bool" : ["bool","asignacion","DecVarBody2","puntoComa"]},
        "DecVarBody2" : {"false" : ["false"],
                         "true" : ["true"]},

        "StatementList" : {"end" : ["StatementList2"],
                           "id" : ["StatementList2"],
                           "let" : ["StatementList2"],
                           "if" : ["StatementList2"],
                           "goto" : ["StatementList2"]},

        "StatementList2" : {"id" : ["Statement","StatementList2"],
                        "let" : ["Statement","StatementList2"],
                        "if" : ["Statement","StatementList2"],
                       "goto" : ["Statement","StatementList2"],
                       "end" : []},

        "Statement" : { "id" : ["id","dospuntos","StatementBody"],
                        "let" : ["StatementBody"],
                        "if" : ["StatementBody"],
                        "goto" : ["StatementBody"],
                    },
        "StatementBody" : { "let" : ["Assignment"],
                           "if"  : ["Conditional"],
                            "goto" : ["Goto"]},
        "Goto" : {"goto": ["goto","id","puntoComa"]},

        "Assignment"  : { "let" : ["let","Lvalue","asignacion","Assignment2"]},

        "Assignment2" : {"id": ["Rvalue","Assignment3","puntoComa"],
                        "numero" : ["Rvalue","Assignment3","puntoComa"],
                        "true": ["Rvalue","Assignment3","puntoComa"],
                        "false": ["Rvalue","Assignment3","puntoComa"],
                        "not": ["not","Rvalue","puntoComa"]},

        "Assignment3" : {"suma" : ["Op","Rvalue"],
                          "resta" : ["Op","Rvalue"],
                          "producto" : ["Op","Rvalue"],
                          "and" : ["Op","Rvalue"],
                          "or" : ["Op","Rvalue"],
                          "puntoComa" : []},
        
        "Op"    : { "suma" : ["MatOp"],
                    "resta" : ["MatOp"],
                    "producto" : ["MatOp"],
                    "and" : ["BoolOp"],
                    "or" : ["BoolOp"]
        },

        "Lvalue" : {"id" : ["id"] },
        "Rvalue" : {"id" : ["id"],
                    "numero" : ["numero"],
                    "false" : ["false"],
                    "true" : ["true"] },
        "Conditional" : {"if" : ["if","CompExpr", "goto","id","puntoComa","Conditional2"]},

        "Conditional2" : {"id" : [],
                          "let" : [],
                          "if" : [],
                          "goto" : [],
                          "end" : [],
                          "else" : ["else","goto","id","puntoComa"]},
        
        "CompExpr" : { "id" : ["Rvalue","CompOp","Rvalue"],
                      "numero" : ["Rvalue","CompOp","Rvalue"],
                      "true" : ["Rvalue","CompOp","Rvalue"],
                      "false" : ["Rvalue","CompOp","Rvalue"]},

        "CompOp" : {"dobleigual" : ["dobleigual"],
                    "desigual" : ["desigual"],
                    "mayor" : ["mayor"],
                    "menor" : ["menor"],
                    "menorigual" : ["menorigual"],
                    "mayorigual" : ["mayorigual"]

                    },
        "MatOp" : { "suma" :["suma"],
                    "resta" : ["resta"],
                    "producto" : ["producto"]
        },

        "BoolOp" : {"and" : ["and"],
                    "or" : ["or"]}


}


def predictivo(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,  ##lista de tuplas
        'index': 0,         ##posicion de la lista
        'error': False,     
    }
    ##Para guardar los no terminales que uso la cadena
    coleccionNT =[]
    ##Guarda el cuerpo de la produccion a usar del no terminal 
    coleccion = []

    ##simbolo es un no terminal y hay que tener en cuenta la lista de tuplas
    ##palabra es el primer elemento de la tupla.  el [0] queda fijo, porque quiero su identificador devuelto por el lexer
    def pni(simbolo): 
        if datos_locales['index'] >= len(datos_locales['lista_tokens']):
            datos_locales['error'] = True
        else:
            palabra = datos_locales['lista_tokens'][datos_locales['index']][0]
            ##Pregunto si palabra coincide con algun simbolo directriz del simbolo(no terminal)
            ##si palabra coincide, guardo el simbolo y su cuerpo de produccion.Este ultimo tambien se lo paso a procesar()
            if palabra in SD[simbolo]:
                coleccionNT.append(simbolo)
                coleccion.append(SD[simbolo][palabra])
                procesar(SD[simbolo][palabra])
 

    
    def procesar(cuerpo_produccion): 
        for simbolo in cuerpo_produccion:
            palabra = datos_locales['lista_tokens'][datos_locales['index']][0]  ##toma el primer elemento de la tupla
            datos_locales['error'] = False

            if simbolo in VT:
                if simbolo == palabra:
                    
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    
                    break
                
    
    def principal(): 
        pni("TCode")
        palabra = datos_locales['lista_tokens'][datos_locales['index']][0]
        if palabra != '#' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        print("Derivacion")
        for i in range(0,len(coleccionNT)):
            print(coleccionNT[i],end="-->")
            print(coleccion[i])
                       

        return True
    
    return principal()



##Agrego esta funcion, para agregar a la lista de tuplas que devuelve el lexer,
##el simbolo de fin de cadena, que servira com evaluacion para reconocer la cadena
##En esta funcion usara el lexer
def agregar_simbolo_fin_cadena(cadena):
    lista  = LEXER.lexer(cadena)
    lista2 = lista + [('#','#')]
    return lista2 

##cadena de pruebas

cadena1 = "program id\n.begin end"
cadena2 = "programid.\tbeginid:gotoid;end"                                                  ##no pertenece
cadena3 = "programid.beginid:ifid==idgotoid;elsegotoid;"                                    ##no pertenece
cadena4 = "program?##++40juego.\n\tbegin valor:if 4<5 goto#verdadero;\n\telse goto falso;"  ##no pertenece
cadena5 = "program id.\n\tbegin id:if true==true goto id;\n\telse goto id; end"
cadena6 = "program tarea4. begin id:if40>20goto id;else goto id;end"                           ##no pertenece 
cadena7 = "program tarea20.var id:int(30...10)= 40; begin end"                             
cadena8 = "program id.var id : bool = true; begin end"
cadena9 = "program id. begin:let id = not false; begin end"                                     ##no pertenece
cadena10 = "program id . begin id : let valor = 40 ;\nend 1dfbfdnb"                             ##no pertenece
cadena11 = "program id .begin id:let valor=4+4;end"
cadena12 = "program id .begin id:if 1<>1 goto id; else goto id ; end"
cadena13 = "program id . begin id : if 1<=2 goto id ; else goto id ; end"
cadena14 = "program id . begin id : if 1 >= 0 goto id ; else goto id ; end"
cadena15 = "program id .begin id : let valor = 4-4; end"
cadena16 = "program id .begin id : let valor = 4*4 ; end"
cadena17 = "program id .begin id : let valor = 4 or 5; end"
cadena18 = "program id .begin id : let valor = 7 and 8; end"

print("cadena1###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena1)))

print("cadena2###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena2)))

print("cadena3###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena3)))

print("cadena4###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena4)))

print("cadena5###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena5)))


print("cadena6###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena6)))

print("cadena7###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena7)))

print("cadena8###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena8)))


print("cadena9###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena9)))

print("cadena10###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena10)))


print("cadena11###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena11)))

print("cadena12###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena12)))

print("cadena13###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena13)))

print("cadena14###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena14)))

print("cadena15###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena15)))

print("cadena16###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena16)))

print("cadena17###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena17)))

print("cadena18###################################")
print(predictivo(agregar_simbolo_fin_cadena(cadena18)))