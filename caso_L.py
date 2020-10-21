from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *

def caso_L():
    

    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa
    
    
    
    #Parametros
    L = 5.0 * m
    B = 2.0 * m
    H = 3 * m
    
    #Inicializar modelo
    ret = Reticulado()
    
    
    
    #------------------------------------------------------------------------------------------------------------------------
    #                   NODOS
    #------------------------------------------------------------------------------------------------------------------------
    
    
    
    # --------   NODOS PLANTA INFERIOR
    
    Nodos_corrida_1_tablero = 45
    for i in range(Nodos_corrida_1_tablero+1):
        ret.agregar_nodo( L*(1 + i) , 0 ,  100*m )
    
    Nodos_corrida_2_tablero = 91 -46
    for i in range(Nodos_corrida_2_tablero+1):
        ret.agregar_nodo( L*(1 + i) , B ,  100*m )
    
    
    # --------   NODOS PLANTA SUPERIOR
    
    Nodos_corrida_3_tablero = 135 - 92
    for i in range(Nodos_corrida_3_tablero+1):
        ret.agregar_nodo( L*(i+2) , 0 , 100*m + H )
    
    
    Nodos_corrida_4_tablero = 179 - 136
    for i in range(Nodos_corrida_4_tablero+1):
        ret.agregar_nodo( L*(i+2) , B , 100*m + H )
    
    
    
    
    # --------   NODOS COLUMNA 1     (BASE EN NODO GLOBAL 10)
    
    # CARA 1
    ret.agregar_nodo( 22*m , 0 , 83*m ) # 180
    ret.agregar_nodo( 22*m , 0 , 93*m ) # 181
    ret.agregar_nodo( 21*m , 0 , 96.5*m ) # 182
    ret.agregar_nodo( 23.5*m , 0 , 96.5*m ) # 183
    
    # CARA 2
    ret.agregar_nodo( 22*m , B , 83*m ) # 184
    ret.agregar_nodo( 22*m , B , 93*m ) # 185
    ret.agregar_nodo( 21*m , B , 96.5*m ) # 186
    ret.agregar_nodo( 23.5*m , B , 96.5*m ) # 187
    
    
    
    
    
    
    
    
    
    
    # # --------   NODOS COLUMNA 2     (BASE EN NODO GLOBAL 14)
    
    # CARA 1
    ret.agregar_nodo( 65*m , 0 , 47*m ) # 188 CENTRAL
    ret.agregar_nodo( 65*m , 0 , 90*m ) # 189 CENTRAL
    
    ret.agregar_nodo( (55 + 2.5) *m , 0 , (90 + 7.5 )*m ) # 190 
    ret.agregar_nodo( (55 +   5) *m , 0 , (90 + 5   )*m ) # 191
    ret.agregar_nodo( (55 + 7.5) *m , 0 , (90 + 2.5 )*m ) # 192
    
    ret.agregar_nodo( (65 + 2.5) *m , 0 , (90 + 2.5 )*m ) # 193
    ret.agregar_nodo( (65 +   5) *m , 0 , (90 +   5 )*m ) # 194
    ret.agregar_nodo( (65 + 7.5) *m , 0 , (90 + 7.5 )*m ) # 195
    
    #CARA 2
    ret.agregar_nodo( 65*m , B , 47*m ) # 196 CENTRAL
    ret.agregar_nodo( 65*m , B , 90*m ) # 197 CENTRAL
    
    ret.agregar_nodo( (55 + 2.5) *m , B , (90 + 7.5 )*m ) # 198 
    ret.agregar_nodo( (55 +   5) *m , B , (90 + 5   )*m ) # 199
    ret.agregar_nodo( (55 + 7.5) *m , B , (90 + 2.5 )*m ) # 200
    
    ret.agregar_nodo( (65 + 2.5) *m , B , (90 + 2.5 )*m ) # 201
    ret.agregar_nodo( (65 +   5) *m , B , (90 +   5 )*m ) # 202
    ret.agregar_nodo( (65 + 7.5) *m , B , (90 + 7.5 )*m ) # 203
    
    
    
    
    
    
    # # --------   NODOS COLUMNA 3     (BASE EN NODO GLOBAL 17)
    
    # CARA 1
    ret.agregar_nodo( 105*m , 0 , 65*m )       # 204 CENTRAL
    ret.agregar_nodo( 105*m , 0 , 90*m )       # 205 CENTRAL
    
    
    ret.agregar_nodo( (95 + 2.5) *m , 0 , (90 + 7.5 )*m )  # 206
    ret.agregar_nodo( (95 +   5) *m , 0 , (90 + 5   )*m )  # 207
    ret.agregar_nodo( (95 + 7.5) *m , 0 , (90 + 2.5 )*m )  # 208
    
    ret.agregar_nodo( (105 + 2.5) *m , 0 , (90 + 2.5 )*m ) # 209
    ret.agregar_nodo( (105 +   5) *m , 0 , (90 +   5 )*m ) # 210
    ret.agregar_nodo( (105 + 7.5) *m , 0 , (90 + 7.5 )*m ) # 211
    
    
    #CARA 2
    
    ret.agregar_nodo( 105*m , B , 65*m )       # 212 CENTRAL
    ret.agregar_nodo( 105*m , B , 90*m )       # 213 CENTRAL
    
    ret.agregar_nodo( (95 + 2.5) *m , B , (90 + 7.5 )*m )  # 214
    ret.agregar_nodo( (95 +   5) *m , B , (90 + 5   )*m )  # 215
    ret.agregar_nodo( (95 + 7.5) *m , B , (90 + 2.5 )*m )  # 216
    
    ret.agregar_nodo( (105 + 2.5) *m , B , (90 + 2.5 )*m ) # 217
    ret.agregar_nodo( (105 +   5) *m , B , (90 +   5 )*m ) # 218
    ret.agregar_nodo( (105 + 7.5) *m , B , (90 + 7.5 )*m ) # 219
    
    
    
    
    
    
    
    
    
    
    # # --------   NODOS COLUMNA 4    (BASE EN NODO GLOBAL 20)
    
    # CARA 1
    ret.agregar_nodo( 135*m , 0 , 66*m )       # 220 CENTRAL
    ret.agregar_nodo( 135*m , 0 , 90*m )       # 221 CENTRAL
    
    
    
    
    ret.agregar_nodo( (125 + 2.5) *m , 0 , (90 + 7.5 )*m )  # 222
    ret.agregar_nodo( (125 +   5) *m , 0 , (90 + 5   )*m )  # 223
    ret.agregar_nodo( (125 + 7.5) *m , 0 , (90 + 2.5 )*m )  # 224
    
    ret.agregar_nodo( (135 + 2.5) *m , 0 , (90 + 2.5 )*m ) # 225
    ret.agregar_nodo( (135 +   5) *m , 0 , (90 +   5 )*m ) # 226
    ret.agregar_nodo( (135 + 7.5) *m , 0 , (90 + 7.5 )*m ) # 227
    
    
    # CARA 2
    ret.agregar_nodo( 135*m , B , 66*m )       # 228 CENTRAL
    ret.agregar_nodo( 135*m , B , 90*m )       # 229 CENTRAL
    
    ret.agregar_nodo( (125 + 2.5) *m , B , (90 + 7.5 )*m )  # 230
    ret.agregar_nodo( (125 +   5) *m , B , (90 + 5   )*m )  # 231
    ret.agregar_nodo( (125 + 7.5) *m , B , (90 + 2.5 )*m )  # 232
    
    ret.agregar_nodo( (135 + 2.5) *m , B , (90 + 2.5 )*m ) # 233
    ret.agregar_nodo( (135 +   5) *m , B , (90 +   5 )*m ) # 234
    ret.agregar_nodo( (135 + 7.5) *m , B , (90 + 7.5 )*m ) # 235
    
    
    
    
    
    
    # # --------   NODOS COLUMNA 5   (BASE EN NODO GLOBAL 24)
    
    
    
    ret.agregar_nodo( 172*m , 0 , 79*m )       # 236 CENTRAL
    ret.agregar_nodo( 172*m , 0 , 90*m )       # 237 CENTRAL
    
    ret.agregar_nodo( 171*m , 0 , 95*m )       # 238 
    ret.agregar_nodo( 173.5*m , 0 , 95*m )     # 239 
    
    ret.agregar_nodo( 172*m , B , 79*m )       # 240 CENTRAL
    ret.agregar_nodo( 172*m , B , 90*m )       # 241 CENTRAL
    
    ret.agregar_nodo( 171*m , B , 95*m )       # 242
    ret.agregar_nodo( 173.5*m , B , 95*m )     # 243 
    
    
    
    
    
    # # --------   NODOS COLUMNA 6   (BASE EN NODO GLOBAL 24)
    
    
    
    ret.agregar_nodo( 198*m , 0 , 93*m )       # 244 
    ret.agregar_nodo( 198*m , B , 93*m )       # 245 
    
    
    
    
    
    
    
    #------------------------------------------------------------------------------------------------------------------------
    #                   BARRAS
    #------------------------------------------------------------------------------------------------------------------------
    
    
    # PROPIEDADES 
    
    A = (1.1*cm)**2
    r = sqrt(A/3.141593)
    
        
        
    props_C = [8*cm, 1.76*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]
    
    props_C_BIG = [16*cm, 3.5*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]
    
    props_C_BIG2 = [30*cm, 3.57*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]

    props_C_BIG5 = [14*cm, 1.5*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]

    props_C_BIG4 = [26*cm, 1.4*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]

    
    props_elevacion_cruzadas = [8*cm, 2*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]
    
    props_elevacion_longitudinales = [5.5*cm, 2*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]

    props_elevacion_verticales = [5.3*cm, 1*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]

    


    props_tablero_inferior_cruzadas = [8*cm, 3*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]
    props_tablero_superiores_cruzadas = [6.9*cm, 3*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]
    

    props_tablero_inferior_horizontales =   [8*cm, 1*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]
    props_tablero_superiores_horizontales = [5.5*cm, 1*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]





    # ALA 1 - BARRAS ELEVACION CRUZADAS
    
    # CARA 1 
    Nodos_tablero = 42 
    for i in range(Nodos_tablero +1 ):
        if i%2 ==0:
            ret.agregar_barra(Barra(i, i + 92, *props_elevacion_cruzadas))
            
    for i in range(Nodos_tablero +1 ):
        if i%2 ==0:
            ret.agregar_barra(Barra(i+2, i + 92, *props_elevacion_cruzadas))
    ret.agregar_barra(Barra(45, 135, *props_elevacion_cruzadas))
    
    
    
    
    # ALA 2 - BARRAS ELEVACION CRUZADAS
    
    # CARA 2
    Nodos_tablero = 42 
    for i in range(Nodos_tablero +1 ):
        if i%2 ==0:
            ret.agregar_barra(Barra(i+46, i + 136, *props_elevacion_cruzadas))
            
    for i in range(Nodos_tablero +1 ):
        if i%2 ==0:
            ret.agregar_barra(Barra(i+48, i + 136, *props_elevacion_cruzadas))
    ret.agregar_barra(Barra(91, 179, *props_elevacion_cruzadas))
    
    
    
    
    
    
    
    
    
    
    
    
    #BARRAS LONGITUDINALES INFERIORES
    
    for i in range (45):
        # print (i,i+1)
        ret.agregar_barra(Barra(i,i+1, *props_elevacion_longitudinales))
    for i in range (45):
        # print (i+46,i+1+46)
        ret.agregar_barra(Barra(i+46,i+1+46, *props_elevacion_longitudinales))
    
    
    
    
    #BARRAS LONGITUDINALES SUPERIORES
    
    for i in range (43):
        # print (i+92,i+93)
        ret.agregar_barra(Barra(i+92,i+93, *props_elevacion_longitudinales))
    
    for i in range (43):
        # print (i+136,i+137)
        ret.agregar_barra(Barra(i+136,i+137, *props_elevacion_longitudinales))
    
       
    
    
    #BARRAS ELEVACION VERTICALES
    
    for i in range (44):
        # print (i+1,i+92)
        ret.agregar_barra(Barra(i+1, i+1+91, *props_elevacion_verticales))
    for i in range (44):
        # print (i+46, i+1+135)
        ret.agregar_barra(Barra(i+47, i+1+135, *props_elevacion_verticales))
    
    
    
    
    
    
    
    
    
    
    
    

    
    # Barras planta inferior
    
    nodos_planta_inferior = 45
    
    for j in range(nodos_planta_inferior + 1):              #Barras horizontales
        # print (j,  j + 46)
        ret.agregar_barra(Barra(j,  j + 46 ,  *props_tablero_inferior_horizontales))
        
    
    for j in range(nodos_planta_inferior):              #Barras cruzadas
        # print (j,  j + 47)
        ret.agregar_barra(Barra(j,  j + 47 ,  *props_tablero_inferior_cruzadas ))
        
    print (" ")
    for j in range(nodos_planta_inferior):                      #Barras cruzadas
        # print (j + 1 ,  j + 46 )
        ret.agregar_barra(Barra(j + 1 ,  j + 46 ,  *props_tablero_inferior_cruzadas ))    
    
    
    #Barras planta superior
    
    nodos_planta_superior = 135-91
    
    for j in range(nodos_planta_superior):              #Barras horizontales
        # print (j + 92 ,  j + 92 + 44)
        ret.agregar_barra(Barra(j + 92 ,  j + 92 + 44,  *props_tablero_superiores_horizontales))
        
    
    for j in range(nodos_planta_superior - 1):              #Barras cruzadas
        # print (j+ 93 ,  j + 136)
        ret.agregar_barra(Barra(j+ 93 ,  j + 136 ,  *props_tablero_superiores_cruzadas ))
        
    for j in range(nodos_planta_superior -1 ):                      #Barras cruzadas
        # print (j+ 92 ,  j + 137)
        ret.agregar_barra(Barra(j+ 92 ,  j + 137,  *props_tablero_superiores_cruzadas))
    
   
    
    
    
    
    
    
    # --------   BARRAS COLUMNA 1     (BASE EN NODO GLOBAL 10)
    
    
    
    
    ret.agregar_barra(Barra(180 , 181,  *props_C_BIG ))  # CENTRAL
    ret.agregar_barra(Barra(181 , 182,  *props_C ))
    ret.agregar_barra(Barra(181 , 183,  *props_C ))
    ret.agregar_barra(Barra(182 , 183,  *props_C ))
    ret.agregar_barra(Barra(3 , 182,  *props_C ))
    ret.agregar_barra(Barra(4 , 183,  *props_C ))
    ret.agregar_barra(Barra(3 , 183,  *props_C ))
    ret.agregar_barra(Barra(4 , 182,  *props_C ))
    
    
    ret.agregar_barra(Barra(180+4 , 181+4,  *props_C_BIG )) # CENTRAL
    ret.agregar_barra(Barra(181+4, 182+4,   *props_C ))
    ret.agregar_barra(Barra(181+4, 183+4,   *props_C ))
    ret.agregar_barra(Barra(182+4 , 183+4,  *props_C ))
    ret.agregar_barra(Barra(3+46 , 182+4,   *props_C ))
    ret.agregar_barra(Barra(4+46 , 183+4,   *props_C ))
    ret.agregar_barra(Barra(3+46 , 183+4,   *props_C ))
    ret.agregar_barra(Barra(4+46 , 182+4,   *props_C ))
    
    
    
    
    
    
    # --------   BARRAS COLUMNA 2     (BASE EN NODO GLOBAL 14)
    
    
    ret.agregar_barra(Barra( 188 , 189,  *props_C_BIG2 )) # CENTRAL INFERIOR
    ret.agregar_barra(Barra( 12 , 189,   *props_C_BIG2 )) # CENTRAL SUPERIOR
    
    ret.agregar_barra(Barra( 10 , 190,   *props_C ))  
    ret.agregar_barra(Barra( 190 , 191,  *props_C ))  
    ret.agregar_barra(Barra( 191 , 192,  *props_C ))  
    ret.agregar_barra(Barra( 189 , 192,  *props_C ))  
    ret.agregar_barra(Barra( 189 , 193,  *props_C ))  
    ret.agregar_barra(Barra( 193 , 194,  *props_C ))  
    ret.agregar_barra(Barra( 194 , 195,  *props_C ))  
    ret.agregar_barra(Barra( 14 ,  195,   *props_C ))  
    ret.agregar_barra(Barra( 11 ,  191,   *props_C ))  
    ret.agregar_barra(Barra( 13 ,  194,   *props_C ))  
    ret.agregar_barra(Barra( 11 ,  190,   *props_C ))  
    ret.agregar_barra(Barra( 13 ,  195,   *props_C ))  
    ret.agregar_barra(Barra( 12 ,  192,   *props_C ))  
    ret.agregar_barra(Barra( 12 ,  193,   *props_C ))  
    ret.agregar_barra(Barra( 11 ,  192,   *props_C ))  
    ret.agregar_barra(Barra( 13 ,  193,   *props_C ))  
    
    
    
    ret.agregar_barra(Barra( 188+8 , 189+8,  *props_C_BIG2 )) # CENTRAL INFERIOR
    ret.agregar_barra(Barra( 12+46    , 189+8,   *props_C_BIG2 )) # CENTRAL SUPERIOR
    ret.agregar_barra(Barra( 10 +46   , 190+8,   *props_C ))  
    ret.agregar_barra(Barra( 190+8 , 191+8,  *props_C ))  
    ret.agregar_barra(Barra( 191+8 , 192+8,  *props_C ))  
    ret.agregar_barra(Barra( 189+8 , 192+8,  *props_C ))  
    ret.agregar_barra(Barra( 189+8 , 193+8,  *props_C ))  
    ret.agregar_barra(Barra( 193+8 , 194+8,  *props_C ))  
    ret.agregar_barra(Barra( 194+8 , 195+8,  *props_C ))  
    ret.agregar_barra(Barra( 14 +46  ,  195+8,   *props_C ))  
    ret.agregar_barra(Barra( 11+46 ,  191+8,   *props_C ))  
    ret.agregar_barra(Barra( 13+46 ,  194+8,   *props_C ))  
    ret.agregar_barra(Barra( 11+46 ,  190+8,   *props_C ))  
    ret.agregar_barra(Barra( 13+46 ,  195+8,   *props_C ))  
    ret.agregar_barra(Barra( 12+46 ,  192+8,   *props_C ))  
    ret.agregar_barra(Barra( 12+46 ,  193+8,   *props_C ))  
    ret.agregar_barra(Barra( 11 +46,  192+8,   *props_C ))  
    ret.agregar_barra(Barra( 13 +46,  193+8,   *props_C )) 
    
    
    
    
    
    
    
    
    
    
    # --------   BARRAS COLUMNA 3     (BASE EN NODO GLOBAL 17)
    
    
    ret.agregar_barra(Barra( 188+16 , 189+16,  *props_C_BIG4 )) # CENTRAL INFERIOR
    ret.agregar_barra(Barra( 12 +8, 189+16,   *props_C_BIG4 )) # CENTRAL SUPERIOR
    
    ret.agregar_barra(Barra( 10+8 , 190+16,   *props_C ))  
    ret.agregar_barra(Barra( 190+16 , 191+16,  *props_C ))  
    ret.agregar_barra(Barra( 191+16 , 192+16,  *props_C ))  
    ret.agregar_barra(Barra( 189+16 , 192+16,  *props_C ))  
    ret.agregar_barra(Barra( 189+16 , 193+16,  *props_C ))  
    ret.agregar_barra(Barra( 193+16 , 194+16,  *props_C ))  
    ret.agregar_barra(Barra( 194+16 , 195+16,  *props_C ))  
    ret.agregar_barra(Barra( 14+8,  195+16,   *props_C ))  
    ret.agregar_barra(Barra( 11+8,  191+16,   *props_C ))  
    ret.agregar_barra(Barra( 13+8,  194+16,   *props_C ))  
    ret.agregar_barra(Barra( 11+8,  190+16,   *props_C ))  
    ret.agregar_barra(Barra( 13+8,  195+16,   *props_C ))  
    ret.agregar_barra(Barra( 12+8 ,  192+16,   *props_C ))  
    ret.agregar_barra(Barra( 12+8 ,  193+16,   *props_C ))  
    ret.agregar_barra(Barra( 11+8 ,  192+16,   *props_C ))  
    ret.agregar_barra(Barra( 13+8 ,  193+16,   *props_C ))  
    
    
    
    ret.agregar_barra(Barra( 188+16+8 , 189+16+8,  *props_C_BIG4 )) # CENTRAL INFERIOR
    ret.agregar_barra(Barra( 12+8+46, 189+16+8,   *props_C_BIG4 )) # CENTRAL SUPERIOR
    
    ret.agregar_barra(Barra( 10+8+46 , 190+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 190+16+8 , 191+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 191+16+8 , 192+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 189+16+8 , 192+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 189+16+8 , 193+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 193+16+8 , 194+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 194+16+8 , 195+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 14+8+46,  195+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 11+8+46,  191+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 13+8+46,  194+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 11+8+46,  190+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 13+8+46,  195+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 12+8+46 ,  192+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 12+8+46 ,  193+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 11+8+46 ,  192+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 13+8+46,  193+16+8,   *props_C ))  
    
    
    
    # --------   BARRAS COLUMNA 4     (BASE EN NODO GLOBAL 20)
    
    #CARA 1
    
    ret.agregar_barra(Barra( 188+16+16 , 189+16+16,  *props_C_BIG4 )) # CENTRAL INFERIOR
    ret.agregar_barra(Barra( 12+8+6, 189+16+16,   *props_C_BIG4 )) # CENTRAL SUPERIOR
    
    ret.agregar_barra(Barra( 10+8+6 , 190+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 190+16+16 , 191+16+16,  *props_C ))  
    ret.agregar_barra(Barra( 191+16+16 , 192+16+16,  *props_C ))  
    ret.agregar_barra(Barra( 189+16 +16, 192+16+16,  *props_C ))  
    ret.agregar_barra(Barra( 189+16 +16, 193+16+16,  *props_C ))  
    ret.agregar_barra(Barra( 193+16 +16, 194+16+16,  *props_C ))  
    ret.agregar_barra(Barra( 194+16+16 , 195+16+16,  *props_C ))  
    ret.agregar_barra(Barra( 14+8+6,  195+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 11+8+6,  191+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 13+8+6,  194+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 11+8+6,  190+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 13+8+6,  195+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 12+8+6 ,  192+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 12+8 +6,  193+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 11+8 +6,  192+16+16,   *props_C ))  
    ret.agregar_barra(Barra( 13+8 +6,  193+16+16,   *props_C ))  
    
    
    
    
    #CARA 2
    ret.agregar_barra(Barra( 188+16+16+8 , 189+16+16+8,  *props_C_BIG4 )) # CENTRAL INFERIOR
    ret.agregar_barra(Barra( 12+8+6+46, 189+16+16+8,   *props_C_BIG4 )) # CENTRAL SUPERIOR
    
    ret.agregar_barra(Barra( 10+8+6+46 , 190+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 190+16+16+8 , 191+16+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 191+16+16+8 , 192+16+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 189+16 +16+8, 192+16+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 189+16 +16+8, 193+16+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 193+16 +16+8, 194+16+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 194+16+16+8 , 195+16+16+8,  *props_C ))  
    ret.agregar_barra(Barra( 14+8+6+46,  195+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 11+8+6+46,  191+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 13+8+6+46,  194+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 11+8+6+46,  190+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 13+8+6+46,  195+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 12+8+6+46 ,  192+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 12+8+6+46,  193+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 11+8+6+46,  192+16+16+8,   *props_C ))  
    ret.agregar_barra(Barra( 13+8+6+46,  193+16+16+8,   *props_C ))  
    
    
    
    
    
    
    
    # --------   BARRAS COLUMNA 5     (BASE EN NODO GLOBAL 24)
    
    
    #CARA 1
    
    ret.agregar_barra(Barra(236 , 237,  *props_C_BIG5 ))  #CENTRAL
    ret.agregar_barra(Barra(237 , 238,  *props_C )) 
    ret.agregar_barra(Barra(237 , 239,  *props_C )) 
    ret.agregar_barra(Barra(238 , 239,  *props_C )) 
    
    ret.agregar_barra(Barra(33 , 238,  *props_C )) 
    ret.agregar_barra(Barra(33 , 239,  *props_C )) 
    ret.agregar_barra(Barra(34 , 238,  *props_C )) 
    ret.agregar_barra(Barra(34 , 239,  *props_C )) 
    
    
    #CARA 2
    
    ret.agregar_barra(Barra(236+4 , 237+4,  *props_C_BIG5 ))  #CENTRAL
    ret.agregar_barra(Barra(237+4 , 238+4,  *props_C )) 
    ret.agregar_barra(Barra(237+4 , 239+4,  *props_C )) 
    ret.agregar_barra(Barra(238+4, 239+4,  *props_C )) 
    
    ret.agregar_barra(Barra(33+46 , 238+4,  *props_C )) 
    ret.agregar_barra(Barra(33+46 , 239+4,  *props_C )) 
    ret.agregar_barra(Barra(34+46 , 238+4,  *props_C )) 
    ret.agregar_barra(Barra(34+46 , 239+4,  *props_C )) 
    
    
    
    
    
    # --------   BARRAS COLUMNA 6     (BASE EN NODO GLOBAL 26)
    
    ret.agregar_barra(Barra(38 , 244,  *props_C )) 
    ret.agregar_barra(Barra(39 , 244,  *props_C )) 
    ret.agregar_barra(Barra(38+46 , 245,  *props_C )) 
    ret.agregar_barra(Barra(39+46 , 245,  *props_C )) 
    
    
    
    
    
    
 
    
    
    
    
    
    
    #------------------------------------------------------------------------------------------------------------------------
    #                   RESTRICCIONES
    #------------------------------------------------------------------------------------------------------------------------
    
    
    # ------- APOYOS DEL TABLERO
    
    
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    
    
    ret.agregar_restriccion(1, 0, 0)
    ret.agregar_restriccion(1, 1, 0)
    ret.agregar_restriccion(1, 2, 0)
    
    
    ret.agregar_restriccion(44, 0, 0)
    ret.agregar_restriccion(44, 1, 0)
    ret.agregar_restriccion(44, 2, 0)
    
    
    ret.agregar_restriccion(45, 0, 0)
    ret.agregar_restriccion(45, 1, 0)
    ret.agregar_restriccion(45, 2, 0)
    
    ret.agregar_restriccion(46, 0, 0)
    ret.agregar_restriccion(46, 1, 0)
    ret.agregar_restriccion(46, 2, 0)
    
    
    ret.agregar_restriccion(47, 0, 0)
    ret.agregar_restriccion(47, 1, 0)
    ret.agregar_restriccion(47, 2, 0)
    
    ret.agregar_restriccion(90, 0, 0)
    ret.agregar_restriccion(90, 1, 0)
    ret.agregar_restriccion(90, 2, 0)
    
    ret.agregar_restriccion(91, 0, 0)
    ret.agregar_restriccion(91, 1, 0)
    ret.agregar_restriccion(91, 2, 0)
    
    
    
    # ------- APOYOS COLUMNAS
    
    
    
    # --- COLUMNA 1
    
    ret.agregar_restriccion(180, 0, 0)
    ret.agregar_restriccion(180, 1, 0)
    ret.agregar_restriccion(180, 2, 0)
    
    ret.agregar_restriccion(180+4, 0, 0)
    ret.agregar_restriccion(180+4, 1, 0)
    ret.agregar_restriccion(180+4, 2, 0)
    
    for i in range (181,188):
        ret.agregar_restriccion(i, 1, 0)
    
    
    
    
    # --- COLUMNA 2
    
    ret.agregar_restriccion(188, 0, 0)
    ret.agregar_restriccion(188, 1, 0)
    ret.agregar_restriccion(188, 2, 0)
    
    ret.agregar_restriccion(188+8, 0, 0)
    ret.agregar_restriccion(188+8, 1, 0)
    ret.agregar_restriccion(188+8, 2, 0)
    
    
    for i in range (189,204):
        ret.agregar_restriccion(i, 1, 0)
    
    
    
    # --- COLUMNA 3
    
    ret.agregar_restriccion(204, 0, 0)
    ret.agregar_restriccion(204, 1, 0)
    ret.agregar_restriccion(204, 2, 0)
    
    ret.agregar_restriccion(204+8, 0, 0)
    ret.agregar_restriccion(204+8, 1, 0)
    ret.agregar_restriccion(204+8, 2, 0)
    
    
    for i in range (204,220):
        ret.agregar_restriccion(i, 1, 0)
    
        
    
    
    
    
    
    
    
    # --- COLUMNA 4
    
    ret.agregar_restriccion(220, 0, 0)
    ret.agregar_restriccion(220, 1, 0)
    ret.agregar_restriccion(220, 2, 0)
    
    ret.agregar_restriccion(220+8, 0, 0)
    ret.agregar_restriccion(220+8, 1, 0)
    ret.agregar_restriccion(220+8, 2, 0)
    
    
    for i in range (220,236):
        ret.agregar_restriccion(i, 1, 0)
    
        
    
    
    
    # --- COLUMNA 5
    
    
    ret.agregar_restriccion(236, 0, 0)
    ret.agregar_restriccion(236, 1, 0)
    ret.agregar_restriccion(236, 2, 0)
    
    ret.agregar_restriccion(236+4, 0, 0)
    ret.agregar_restriccion(236+4, 1, 0)
    ret.agregar_restriccion(236+4, 2, 0)
    
    
    for i in range (236,244):
        ret.agregar_restriccion(i, 1, 0)
    
    
    # --- COLUMNA 6
    
    ret.agregar_restriccion(244, 0, 0)
    ret.agregar_restriccion(244, 1, 0)
    ret.agregar_restriccion(244, 2, 0)
    
    
    ret.agregar_restriccion(245, 0, 0)
    ret.agregar_restriccion(245, 1, 0)
    ret.agregar_restriccion(245, 2, 0)
    
    
    
    
    
    
    
    
    
    q = 400 * kg / m**2
    KGF = 9.8067*N
    F_int = L*B/2*  q*KGF
    F_ext = L/2*B/2*q*KGF
    
    nodos_cargas = 91
    nodos_exteriores = [0,45,46,91]
    
    
    for i in range(nodos_cargas+1):
    
        if i in nodos_exteriores:
            ret.agregar_fuerza(i,  2, -F_ext)
        else: 
            ret.agregar_fuerza(i,  2, -F_int)
    
    
        
        
        
            
    
        
    
    
            
    return ret

