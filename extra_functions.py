def get_server_name(ctx, extension):
    lista_car_invalidos = ("?","(",")","-","¿",".",",","¿")
    server_name = ctx.message.guild.name
    for letra in server_name:
        if letra in lista_car_invalidos:
            server_name = server_name.replace(letra,"")
    server_name = server_name.replace(" ","_")
    server_name = (server_name+extension).replace(" ","")
    return server_name



def lector_csv(archivo):
    FIN_ARCHIVO = ""
    registro = archivo.readline()
    if registro == FIN_ARCHIVO:
        nombre, fecha = FIN_ARCHIVO, FIN_ARCHIVO
    else:
        nombre, fecha = registro.rstrip("\n").split(",")
    return nombre, fecha

def lector_txt(archivo):
    FIN_ARCHIVO = ""
    registro = archivo.readline()
    if registro == FIN_ARCHIVO:
        nombre, fecha = FIN_ARCHIVO, FIN_ARCHIVO
    else:
        nombre, fecha = registro.rstrip("\n").split(":")
    return nombre, fecha

def lector_server_txt(archivo):
    FIN_ARCHIVO = ""
    registro = archivo.readline()
    if registro == FIN_ARCHIVO:
        status = FIN_ARCHIVO
    else:
        status = registro.rstrip("\n")
    return status

def lector_diccionario_txt(servername):
    dic = {}
    servername = "dependencias/" + servername
    with open(servername, "r") as archivo:
        nombre, fecha = lector_txt(archivo)
        while not nombre == "":
            dic[nombre] = str(fecha).replace(" ","")
            nombre,fecha = lector_txt(archivo)   
    return dic
#print(lector_diccionario_txt("Proyectos\\botdiscord\\U_WANNA_GO_M8.txt"))
def imprimir_dic_txt(servername, diccionario_cumpleaños):
    servername = "dependencias/" + servername
    with open(servername,"w") as cumples_txt:
        for persona in diccionario_cumpleaños:
            cumples_txt.write(f"{str(persona)}: {diccionario_cumpleaños[persona]}\n")


def get_server_name_fuera(message, extension):
    lista_car_invalidos = ("?","(",")","-","¿",".",",","¿")
    server_name = message.guild.name
    for letra in server_name:
        if letra in lista_car_invalidos:
            server_name = server_name.replace(letra,"")
    server_name = server_name.replace(" ","_")
    server_name = (server_name+extension).replace(" ","")
    return server_name

def leer_dic_csv(message):
    diccionario = {}
    servername = get_server_name_fuera(message,".csv")
    servername = "dependencias/" + servername
    with open(servername,"r") as archivo:
        nombre, cantidad = lector_csv(archivo)
        diccionario[nombre] = cantidad
        while not nombre == "":
            diccionario[nombre] += cantidad
            nombre, cantidad = lector_csv(archivo)
    return diccionario

def imprimir_csv(message, diccionario):
    servername = get_server_name_fuera(message,".csv")
    servername = "dependencias/" + servername
    kappa = message.content()
    with open(servername) as csv:
        for kappa in diccionario:
            csv.write(f"{str(kappa)},{str((int(diccionario[kappa])+1))}")

        
