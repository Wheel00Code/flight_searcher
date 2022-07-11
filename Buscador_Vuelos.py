# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:54:09 2022
    
    
"""
import pandas as pd
import math
import tkinter as tk

# Llegir la informació del excel:
df_V = pd.read_excel("Vols.xlsx")
df_A = pd.read_excel("Aeroports_2.0.xlsx")

# CREAR DICIONARI_________________________________________________________________________________________
# Optenir la informació dels destins del df:
"""Obtiene la información de los destinos posibles desde un aeropuerto
    
    Registro de cambios: Creación de la función - 16/03/22
        
    Parámetros: IATA --> Código IATA del aeropuerto de origen
                df_vols --> Data a frame de los vuelos (tabla)
        
    Retorna: Los destinos (en código IATA)
"""
def destins(IATA, df_Vols):
    
    desti_1 = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["IATA_DESTI"].iloc[0]
    
    desti_2 = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["IATA_DESTI 2"].iloc[0]
    
    desti_3 = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["IATA_DESTI 3"].iloc[0]
        
    return(desti_1, desti_2, desti_3)

# Obtenir preu del df:
    """Obtiene la información del coste de los destinos posibles desde un aeropuerto

    Registro de cambios: Creación de la función - 16/03/22
        
    Parámetros: IATA --> Código IATA del aeropuerto de origen
                df_vols --> Data a frame de los vuelos (tabla)
        
    Retorna: El coste de los posiles destinos
    """
def destins_preu(IATA, df_Vols):
    
    desti_1_Cost = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["COST 1,PREU"].iloc[0]
    
    desti_2_Cost = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["COST 2,PREU "].iloc[0]
    
    desti_3_Cost = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["COST 3,PREU"].iloc[0]
    
    return(desti_1_Cost, desti_2_Cost, desti_3_Cost)

# Obtenir distancia:
    """Obtiene la información de la distancia entre el aeropuerto de origen y los posibles destinos

    
    Registro de cambios: Creación de la función - 16/03/22
        
    Parámetros: IATA --> Código IATA del aeropuerto de origen
                df_vols --> Data a frame de los vuelos (tabla)
        
    Retorna: La distancia entre el aeropuerto de origen y los destinos
    """
def destins_dist(IATA, df_Vols):
    
    desti_1_dist = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["COST 1, DIST"].iloc[0]
    
    desti_2_dist = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["COST 2,DIST"].iloc[0]
    
    desti_3_dist = df_Vols[df_Vols["IATA_ORIGEN"]==IATA]["COST 3,DIST"].iloc[0]
    
    return(desti_1_dist, desti_2_dist, desti_3_dist)


# Crear el dicionar amb el que treballarem:
"""Se crea un diccionario para almacenar las iteraciones que va ejecutando el algoritmo

Registro de cambios:
    
Parámetros: df_V --> Contiene los vuelos que contiene la tabla Excel
    
Retorna: Devuelve el diccionario con la información almacenada.
    
    
"""
def create_dic(df_V):
    # Crear un dicionari buit
    dic_costos = {}
    # Contar numero de aeoroports
    total = df_V["IATA_ORIGEN"].count()
    i = 0
    # Loop que llegeix totes els aeoroports
    while i < total:
        # Nom del aeorport origen:
        name = df_V["IATA_ORIGEN"].iloc[i]
        
        # Funcció que retorna els destins del aeorport origen
        desti_1, desti_2, desti_3 = destins(name, df_V)
        
        # Funcció que retorna els preus dels destins des de l'aeorport origen
        desti_1_Cost, desti_2_Cost, desti_3_Cost= destins_preu(name, df_V)
        
        # Funcció que retorna la distancia dels destins des de l'aeorport origen
        desti_1_dist, desti_2_dist, desti_3_dist = destins_dist(name, df_V)
        
        # Ompli el dicionari amb la informació
        dic_costos[name] =  [[desti_1, desti_1_Cost, desti_1_dist], [desti_2, desti_2_Cost, desti_2_dist], [desti_3, desti_3_Cost, desti_3_dist]]
    
        i = i + 1
    
    # Retorna el dicionari
    return dic_costos
# HEULISTICA___________________________________________________________
"""Esta función indica la heurística que hemos utilizado en nuestro programa,
en este caso la hemos sacado de internet

Registro de cambios:
    
Parámetros: lon1, lon2, lat1 y lat2--> Indican las coordenadas de los distintos aeropuertos de
                                        de nuestra red (para calcular las distancias).
    
Retorna: La distancia entre dos aeropuertos.
"""
def heuristica(lon1,lon2, lat1 ,lat2  ):
    
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    
    return distancia

# Obtenir longitut i latitud d'un aeroport:
"""
Esta función sirve para tener registrado la latitud y longitud de los aeropuertos registrados.

Registro de cambios:
    
Parámetros: IATA --> Código IATA del aeropuerto de la línea que indique el .iloc
            df_Vols --> Data a frame de los vuelos (tabla)
            
Retorna: La longitud y latitud de un determinado aeropuerto.
"""
def longitud_i_latitud(IATA, df_Vols):    

    latitud= df_Vols[df_Vols["CODI_IATA"]==IATA]["LATITUD"].iloc[0]
    longitud = df_Vols[df_Vols["CODI_IATA"]==IATA]["LONGITUD"].iloc[0]
    
    return(latitud, longitud ) 

# obtenir la key amb el value de un diccionari:
    """
Esta función sirve para obter la key de un dicionario mediante su valor.

Registro de cambios:
    
Parámetros: val --> valor del que se quiere la key
            dict_resulsts --> dicionari.
            
Retorna: La longitud y latitud de un determinado aeropuerto.
"""
def get_key(val, dict_resulsts):
    for key, value in dict_resulsts.items():
         if val == value:             
            return key 
    return "There is no such Key"

# AlGORISME DE A ESTRELLA:
    
# Obrir els nous origens:    
""" 
La función te pide el origen, el diccionario de destinos, el destino, el recorrido y el coste acumulado
 y la opcion y devuelve la posición, el nombre del destino, el mínimo y el diccionario de resultados.
"""
def obrir_opcio_aestrella(origen,dic_costos, destino, recorido, cost_acumulado, opcio ):
    
    fin = False
    orige_des = dic_costos[origen]
    
    # lista distancia destins
    list_dist_destins = []

    #dictionaramb tots results:
    dict_resulsts = {}
    
    
    
    list_recorido = str(recorido).split("'")
    #print("recorido:", recorido, "Lista : ", list_recorido)                    
                        
    
    # bucle ficar distancia destins en una llista
                    
    for des in orige_des:
        
        name = des[0]
        
        # que no passi pel mateix lloc                
        if name in list_recorido:
            pass
        if name not in list_recorido:
                    
            cost_dest_taula = des[opcio]

            
            latitud_Origen, longitud_Origen = longitud_i_latitud(name, df_A)
            latitud_Destino, longitud_Destino = longitud_i_latitud(destino, df_A)
            
            
            helistica = heuristica(longitud_Origen, longitud_Destino,  latitud_Origen, latitud_Destino)


            #print("Calcul costdes + heul:", cost_dest_taula ,"+", helistica )
            
            cost_dest = cost_dest_taula + cost_acumulado + helistica
            print("Calcular a estrella per",name,"-->",  cost_dest_taula ,"+",cost_acumulado, "+", helistica, "=" ,cost_dest)
            #print("Dsglos amb cost + acum :", cost_dest_taula ,"+", cost_acumulado , "=", cost_dest)
            


            list_dist_destins.append(cost_dest)
            name = des[0]

            recorido_optimo = recorido , name


            dict_resulsts[recorido_optimo] = cost_dest


    
    # agafar el valor minim y treure la direcció
    minimo  = min(list_dist_destins)
    pos = list_dist_destins.index(minimo)
    
    name_des = dic_costos[origen][pos][0]

    
    
    return pos,name_des,minimo, dict_resulsts 

# Algorisme:<--------------------------------------------------------
"""
Esta función te pide el destino, el origen, el diccionario de costes y la opción 
y devuelve  un diccionario con los resultados, otro con los valores
guardados, el valor mínimo, la ruta óptima, i el número de iteraciones.

"""
def A_ESTRELLA_(destino, origen, dic_costos, opcio):
    

    dict_save = {}
    recorido = origen
    df_redundancies = pd.DataFrame(columns = ["IATA","COST"])
    add = 0
    count = 0
    count_Iteracions= 0
    fin = False
    dic_saved = {}
    value_del = ""
    
    while fin != True:
        
        try:
            del dic_saved[value_del]

        except: 
            
            pass

        count_Iteracions = count_Iteracions +1
        print("Iteració:", count_Iteracions)
        pos, name_des ,minimo, dict_resulsts = obrir_opcio_aestrella(origen,dic_costos, destino, recorido, add, opcio  )       
        

    
        
        dic_saved.update(dict_resulsts)
     
        
        
        #Ha de ser despues de donar la llista final --> DOnar llista final y  de la borar de la nova
        value_min = min(list(dic_saved.values()))
        value_del = get_key(value_min, dic_saved)  
        
        
        
        desti_min = str(str(value_del).split(",")[-1]).split("'")[1]  

        
        

        # canviar el minim de open per el minim de total       
        latitud_Origen, longitud_Origen = longitud_i_latitud(desti_min, df_A)
        latitud_Destino, longitud_Destino = longitud_i_latitud(destino, df_A)
        helistica_restar = heuristica(longitud_Origen, longitud_Destino, latitud_Origen, latitud_Destino)
        

        value_add = value_min - helistica_restar
        
        
        
        print("Rutes possibles:",dic_saved )
        print("Ruta optima:", value_del, "km de la ruta", value_add)
        
        
        add = value_add 
    
        
        
        # detectar el desti amb haulistica mes petita y converitlo e origen 
        origen = desti_min
        
        
        recorido = value_del
        
        if desti_min == destino:
            fin = True
        
        print("S'ha arribat a la solució final ?", fin)
        print("")    
        
        
        
        desti_final = str(value_del)
        
        
    return dict_resulsts, dic_saved, count_Iteracions, value_min, desti_final

# Obtenir el dicionari
dic_costos = create_dic(df_V)


# Alghorime A estrella eliminant redundancies:
""" 
La función te pide el origen, destino, opciín a elegir, y el diccionario de costes 
y devuelve  un diccionario con los resultados, otro con los valores
guardados, el valor mínimo, la ruta óptima, i el número de iteraciones. """
def A_ESTRELLA_SENSE_REDUNDANCIES(destino, origen, dic_costos, opcio):
    
    # declarar variables:
    dict_save = {}
    recorido = origen
    df_redundancies = pd.DataFrame(columns = ["IATA","COST"])
    add = 0
    count = 0
    count_Iteracions= 0
    fin = False
    dic_saved = {}
    value_del = ""
    
    while fin != True:
        
        try:
            del dic_saved[value_del]

        except: 
            
            pass

        count_Iteracions = count_Iteracions + 1
        print("Iteració:", count_Iteracions)
        
        # Funció de obrir nou origen ruta:
        pos, name_des ,minimo, dict_resulsts = obrir_opcio_aestrella(origen,dic_costos, destino, recorido, add, opcio  )       
        

        # No treballar amb el dicionary original:
        dic_Saved_old = dic_saved
      
        
        ## Eliminar redundancies:        
        # Crear un df amb els les destins i el cost per mirar si es repeteixen i saber quin cost es inferior:
        list_keys = list(dic_Saved_old.keys())      
        
        #Contador:
        count = 0
        
        
        for i in list_keys:    

            last_aer= str(i).split("'")[-2]
            cost = dic_saved[i]

            # Anñadir nueva row el df
            count = count + 1  
            # entra el aeripuerto destino i su coste
            df_redundancies.loc[count] = pd.Series({'IATA': last_aer, 'COST': cost })

        print("")
        print("DF amb els destins ja oberts i els km:")
        print(df_redundancies)
        
        # Comparar els resultats obtinguts amb els historics:
        
        
        loopdict_resulsts = dict_resulsts
        lista_nevos_destinos_redundantes = []
        
        for i in loopdict_resulsts:  
            
            
            # Obtener lel ultimo destino
            last_aer= str(i).split("'")[-2]
            # Obtener el coste de dicho destino
            cost = loopdict_resulsts[i]
            
            
            saved_destins = list(df_redundancies["IATA"])
            
            if last_aer in saved_destins:
                cost_historic = df_redundancies[df_redundancies["IATA"]== last_aer]["COST"].iloc[0]

                if cost_historic > cost:
                    #("Coste historic pitjor, delet del dictionari  i introduir el nou al df")
                    # delet del dic_saved el historic
                    redundant = get_key(cost_historic, dic_saved)
                    del dic_saved[redundant]
                    
                    # Canviar el valor del df_re
                    df_redundancies.loc[ df_redundancies["IATA"] == last_aer, "COST"] = cost                    
                    
                    
                    
                if cost_historic < cost:
                    #("Coste new pitjor, delet de la llsita de añadir al dic_resultados")
                    # delet del dic_resulys
                    lista_nevos_destinos_redundantes.append(i)
                    
                
                
                
        
    
        # Eliminar els camins redundants de la llista de resultats
        for red in lista_nevos_destinos_redundantes:
            del dict_resulsts[red]

            
            
        dic_saved.update(dict_resulsts)
        print("")
        print("Totes les rutes:", dic_saved)
        
        #dic_saved.pop('uno')
        
        
        #Ha de ser despues de donar la llista final --> DOnar llista final y  de la borar de la nova
        value_min = min(list(dic_saved.values()))
        value_del = get_key(value_min, dic_saved) 
        
        desti_min = str(str(value_del).split(",")[-1]).split("'")[1]        
        
        
        # canviar el minim de open per el minim de total       
        latitud_Origen, longitud_Origen = longitud_i_latitud(desti_min, df_A)
        latitud_Destino, longitud_Destino = longitud_i_latitud(destino, df_A)
        helistica_restar = heuristica(longitud_Origen, longitud_Destino, latitud_Origen, latitud_Destino)
        
        value_add = value_min - helistica_restar
        
        
        print("Ruta optima -->", value_del, "km de la ruta optima -->", value_add)
        
        
        add = value_add 
    
        
        
        # detectar el desti amb haulistica mes petita y converitlo e origen 
        origen = desti_min
        
        #print(add, value_min)
        recorido = value_del
        
        if desti_min == destino:
            fin = True
        
        print("S'ha arribat a la solució final ?", fin)
        print("")
        
        
        ruta_optima = str(value_del)
        
        
    return dict_resulsts, dic_saved, count_Iteracions, value_min, ruta_optima

# algorisme CCU_______________________________________________________________________________________________
## Obrir nou origen del CCU
"""
La función te pide el origen, el diccionario de destinos, el destino, el recorrido y el coste acumulado
 y devuelve la posición, el nombre del destino, el mínimo y el diccionario de resultados.
"""
def obrir_opcio_2(origen, dic_costos, destino, recorido, cost_acumulado ):
    
    fin = False
    orige_des = dic_costos[origen]
    
    # lista distancia destins
    list_dist_destins = []

    #dictionaramb tots results:
    dict_resulsts = {}
    
    # bucle ficar distancia destins en una llista
    for des in orige_des:
    
        cost_dest = des[2]
        
        cost_dest = cost_dest + cost_acumulado
        print("Calcul obrir:", cost_dest ,"+", cost_acumulado , "=", cost_dest)
        
        
        list_dist_destins.append(cost_dest)
        name = des[0]
                
        recorido_optimo = recorido , name
        
    
        dict_resulsts[recorido_optimo] = cost_dest

    
    # agafar el valor minim y treure la direcció
    minimo  = min(list_dist_destins)
    pos = list_dist_destins.index(minimo)
    
    name_des = dic_costos[origen][pos][0]

    
    
    return pos,name_des,minimo, dict_resulsts 

#alghorimse:
    
""" 
La función te pide el origen y el destino y el diccionario dónde están 
situados los costes y devuelve un diccionario con los resultados, otro con los valores
guardados, el valor mínimo, la ruta óptima, i el número de iteraciones.
    """
def A_CCU_(destino, origen, dic_costos):

    dict_save = {}
    recorido = origen
    add = 0
    count = 0
    fin = False
    dic_saved = {}
    value_del = ""
    while fin != True:
        
        try:
            del dic_saved[value_del]

        except: 
            
            pass

        count = count +1
        print("Iteració:", count)
        pos, name_des ,minimo, dict_resulsts = obrir_opcio_2(origen,dic_costos, destino, recorido, add  )       
        
        
        opened = list(list(dict_resulsts.keys())[pos])
    
        
        
        
        dic_saved.update(dict_resulsts)
        
        
        
        #Ha de ser despues de donar la llista final --> DOnar llista final y  de la borar de la nova
        value_min = min(list(dic_saved.values()))
        value_del = get_key(value_min, dic_saved)        
       
        
        desti_min = str(str(value_del).split(",")[-1]).split("'")[1]
        
        
        
        
        
        
        
        
        print("")
        print("Todas las rutas  --> ", dic_saved)
        
        print("Ruta optima -->", value_del, "Km -->", value_min)
        
        # canviar el minim de open per el minim de total
        add = value_min 
    
        
        #print( "Resultado del abierto:", dict_resulsts, fin)
        
        # detectar el desti amb haulistica mes petita y converitlo e origen 
        origen = desti_min
        
        
        recorido = value_del
        
        if desti_min == destino:
            fin = True
        
        print(fin)
        print("")
        
        ruta_optima = str(value_del)
        
        
        
    return dict_resulsts, dic_saved, count, value_min, ruta_optima

#OBTENIR INFORMACIÓ___________________________________________________________________________
# Converir ruta a text i numero de escales:
    # Converir ruta a text i numero de escales:
    """
    La función te pide la ruta óptima y te devuelve los aeropuertos por los que
    pasa y su número de escalas
    """ 
def convert_ruta_to_text(ruta_optima):
    # Clean la tubla de ruta final:
    ruta_optima = ruta_optima.replace("(", "")
    ruta_optima = ruta_optima.replace("'", "")
    ruta_optima = ruta_optima.replace(")", "")
    ruta_optima = ruta_optima.replace(" ", "")
    # Obtenir llista amb IATA dels aeropots
    lista_ruta = ruta_optima.split(",")
    
    numero_numero_escales = (len(lista_ruta)) - 1
    llistas_aeroports = ""
    
    # Converir IATA a llistat dels noms 
    for i in lista_ruta:
        
        aero = get_Aerport_Name_from_IATA(i)
    
        llistas_aeroports = llistas_aeroports + aero + " --> "
    
    llistas_aeroports = llistas_aeroports[:-5]
    
    return llistas_aeroports, numero_numero_escales


# Obtenir el nom dels aeroports per el nom de la ciutat
""" 
Te pide el nombre de la ciudad y te devuelve el nombre del aeropuerto
"""
def get_Aerport_Name(city):      
    name_aerport = df_A[df_A["CIUTAT"]== city]["NOM"].iloc[0]    
    
    return name_aerport   

# Obtenir el Codi IATA dels aeroports per el nom de la ciutat
""" 
Te pide el nombre de la ciudad y te devuelve el código IATA del aeropuerto
"""
def get_Aerport_IATA(city):       
    iata_aerport = df_A[df_A["CIUTAT"]== city]["CODI_IATA"].iloc[0]   
    
    return iata_aerport  

# Obtenir el nom dels aeroports per el IATA de la aeroport
"""
LA función pide el código de IATA y retorna el nombre del aeropuerto
"""
def get_Aerport_Name_from_IATA(IATA):    
    name_aerport = df_A[df_A["CODI_IATA"]== IATA]["NOM"].iloc[0]
    
    
    return name_aerport  

# Crear ventana
ventana = tk.Tk()
ventana.attributes('-fullscreen', True)

# Declarar Variables:
alghorimse_selecionat = tk.StringVar()
origen_selecionat = tk.StringVar()
desti_selecionat = tk.StringVar()
numero_iteracions = tk.StringVar()
ruta_optima_alhgorisme = tk.StringVar()
n_escales = tk.StringVar()
text_ruta_de_aeroports = tk.StringVar()
name_aerport = tk.StringVar()
cost_ruta = tk.StringVar()

"""
Esta función es la del botón. Calcula los diferentes algoritmos con el origen y el destino IATA y devuelve 
las métricas que se ven en el return
"""

def calcular():
    
    
    algorisme = var.get()
    origen = var_origen.get()
    desti = var_desti.get()
    
    # Obtener codi IATA
    origen_IATA = get_Aerport_IATA(origen)
    desti_IATA = get_Aerport_IATA(desti)
    
    
    # Executar alghorisme
    if algorisme == "A estrella":        
        dict_resulsts, dic_saved, count_iteracions, value_min, ruta_optima = A_ESTRELLA_(desti_IATA, origen_IATA, dic_costos, 2)
        
        
    if algorisme == "CCU":
        dict_resulsts, dic_saved, count_iteracions, value_min, ruta_optima = A_CCU_(desti_IATA, origen_IATA, dic_costos)
        
    
    if algorisme == "A estrella eliminant camins redudants":
        dict_resulsts, dic_saved, count_iteracions, value_min, ruta_optima = A_ESTRELLA_SENSE_REDUNDANCIES(desti_IATA, origen_IATA, dic_costos, 2)
    
    
    # Convertir la tubla en text:
    ruta_de_aeroport_text, num_escales = convert_ruta_to_text(ruta_optima)
     
    
    
    
    
    return alghorimse_selecionat.set(algorisme), ruta_optima_alhgorisme.set(ruta_optima), text_ruta_de_aeroports.set(ruta_de_aeroport_text), numero_iteracions.set(count_iteracions), n_escales.set(num_escales), cost_ruta.set(value_min)                      
"""La función retorna el algorismo que hay que elegir, la ruta más óptima, la ruta de los aeropuertos que va a seguir, el número de iteraciones que realiza, el número de escalas y finalmente el valor de la ruta óptima, que es el valor mínimo.
"""



# Titulo Ventana
titulo = tk.Label(ventana, text = "Projecte IA Group 2", bg="ivory3")
titulo.pack(padx = 5, pady = 10, ipadx = 5, fill = tk.X )
# Titulo:
text_Titul = tk.Label(ventana , text = "Cercador de vols:" )
text_Titul.config(font=("Courier", 44))
text_Titul.pack()
text_Titul.place( x = 250, y = 100, height=44 )


#__________________________________________________________________________________________________________________________
#Seleccionar algorismo
# Texto:
text_select_algh = tk.Label(ventana , text = "Seleciona el alghorismo deseado:" )
text_select_algh.pack()
text_select_algh.place( x = 50, y = 200, height=20 )

#Desplegable
var = tk.StringVar(ventana)
var.set('A estrella')
opciones = ['A estrella', 'CCU', 'A estrella eliminant camins redudants' ]
opcion = tk.OptionMenu(ventana, var, *opciones)
opcion.config ( width = 50)
opcion.pack( ) 
opcion.place( x = 300, y = 200, height=20 )


#__________________________________________________________________________________________________________________________
# Obtenir Origen i destí
# Origen:
#________________
# Texto:
text_select_Origen = tk.Label(ventana , text = "Seleciona el origen:" )
text_select_Origen.pack()
text_select_Origen.place( x = 50, y = 250, height=20 )

# Desplegable
var_origen = tk.StringVar(ventana)
var_origen.set('Barcelona')
opciones_Origen = list(df_A["CIUTAT"])
opcion_origen = tk.OptionMenu(ventana, var_origen, *opciones_Origen)
opcion_origen.config ( width = 30)
opcion_origen.pack( ) 
opcion_origen.place( x = 300, y = 250, height=20 )


# Destino:
#________________
# Texto:
text_select_Desti = tk.Label(ventana , text = "Seleciona el destino:" )
text_select_Desti.pack()
text_select_Desti.place( x = 50, y = 300, height=20 )

# Desplegable
var_desti = tk.StringVar(ventana)
var_desti.set('Hong Kong')
opciones_desti = tk.OptionMenu(ventana, var_desti, *opciones_Origen)
opciones_desti.config ( width = 30)
opciones_desti.pack( ) 
opciones_desti.place( x = 300, y = 300, height=20 )




# Aeoroport seleccionado:
boton = tk.Button(ventana, text = "Calcular", fg = "black", command = calcular )
boton.pack()
boton.place( x = 300, y = 350, height=20 )

##LABEL:
text_ruta_1 = tk.Label(ventana, text = "Kilometros de la ruta:" )
text_ruta_1.pack( ) 
text_ruta_1.place( x = 50, y = 450, height=20 )

# Resultst:
##Ruta:
###Tubla:
ruta_tub = tk.Label(ventana,  textvariable = cost_ruta )
ruta_tub.pack( ) 
ruta_tub.place( x = 250, y = 450, height=20 )

### Ruta en text:
text_ruta_2 = tk.Label(ventana,  text = "Aquestsa és la ruta de aeroport: " )
text_ruta_2.pack( ) 
text_ruta_2.place( x = 50, y = 500, height=20 )

ruta_text_ = tk.Label(ventana,  textvariable = text_ruta_de_aeroports )
ruta_text_.pack( ) 
ruta_text_.place( x = 250, y = 500, height=20 )

### Numero de escales:
text_ruta_2 = tk.Label(ventana,  text = "Numero d'escales: " )
text_ruta_2.pack( ) 
text_ruta_2.place( x = 50, y = 550, height=20 )

ruta_text_ = tk.Label(ventana,  textvariable = n_escales )
ruta_text_.pack( ) 
ruta_text_.place( x = 250, y = 550, height=20 )


### Numero de iteracions:
text_ruta_2 = tk.Label(ventana,  text = "Numero d'iteracionst: " )
text_ruta_2.pack( ) 
text_ruta_2.place( x = 50, y = 600, height=20 )

ruta_text_ = tk.Label(ventana,  textvariable = numero_iteracions )
ruta_text_.pack( ) 
ruta_text_.place( x = 250, y = 600, height=20 )










ventana.mainloop()







