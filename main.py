
# ideas
# 
# buscador y reproductor youtube
# 
# porcentaje error pong minijuego
# juego pool / wallpaper engine
# google meet link send
# kappa counter
# cronometro

from datetime import date
import discord
from discord import channel
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from discord.ext.commands import context
from discord.ext.commands import CommandNotFound
from discord.ext.commands.errors import PrivateMessageOnly
from discord.ext.commands.help import HelpCommand
from discord.ext.commands import Bot
from googleapiclient.discovery import build
import random
from extra_functions import *

client = commands.Bot(command_prefix=".", help_command= None)
api_key = "AIzaSyCsPj0Mb3F4Vf9AyFeZj4UkOr1wl2SKeg4"

@client.event
async def on_ready():    
    print('Buenas, soy agustin bot')


@client.event
async def on_message(message):
    # message = <Message id=872504377368268852 channel=<TextChannel id=428750903617519626 name='autistic-music' position=1 nsfw=False news=False category_id=426909566387617804> 
    # type=<MessageType.default: 0> author=<Member id=285496526397243404 name='agustín' discriminator='6300' bot=False nick='s̢̠̈́e͆̿̍x̛̑̐o͋̓́' 
    # guild=<Guild id=426909566387617802 name='U WANNA GO M8?' shard_id=None chunked=False member_count=69>>
    # flags=<MessageFlags value=0>>

    if message.author == client.user:
        return   
        
    if (message.content.startswith('.') and message.content.find("..") == -1):
        await client.process_commands(message)

    elif(message.content.find("kapp") != -1 or message.content.find("Kapp") != -1):    
        kappa_counter(message)

    elif (message.content.find("ty bot" ) != -1 or message.content.find("gracias bot" ) != -1 or message.content.find("thank you bot" ) != -1):
        await message.channel.send("de nada pa, besos en la cola")

@client.command(aliases = ["kapasstats","kappatats","kappastats","kappstats","kappa"])
async def kapastats(ctx):
    with open("dependencias/kappa_counter.json", "r+") as jsonfile:
            diccionario = json.load(jsonfile)

    await ctx.send(diccionario)

@client.command()
async def registrar_cumpleaños(ctx, *mensaje):
    #<discord.ext.commands.context.Context object at 0x0000024FA7F11AC0>
    diccionario_cumpleaños = {}
    separador = " "
    server_name = get_server_name(ctx, ".txt")
 
    with open(server_name,"a") as cumples_txt:
        mensaje = list(mensaje)
        diccionario_cumpleaños[mensaje[0]] = mensaje[1]
        texto_diccionario_cumpleaños = separador.join(diccionario_cumpleaños)
        texto_diccionario_cumpleaños_llaves = separador.join(diccionario_cumpleaños.values())
        cumples_txt.write(f"\n{str(texto_diccionario_cumpleaños)}: {texto_diccionario_cumpleaños_llaves}")
    
    await ctx.send("Cumpleaños registrado con exito.")

@client.command()
async def tabla_cumpleaños(ctx):
    server_name = get_server_name(ctx, ".txt")
    dir = "dependencias\\" + server_name
    await ctx.send("Acá están los cumpleaños registrados para este server",file= discord.File(dir))

@client.command()
async def cumpleaños(ctx):
    servername = get_server_name(ctx, ".txt")
    dic_cumpleaños = lector_diccionario_txt(servername)
    fecha_hoy = date.today()
    fecha_hoy = fecha_hoy.strftime("%d/%m") # d1 = 25/06
    for nombre in dic_cumpleaños:
        if dic_cumpleaños[nombre] == fecha_hoy:
            await ctx.send(f"FELIZ CUMPLEAÑOS {nombre}!!")
            return
    await ctx.send("Hoy no cumple años nadie registrado, consulte con .tabla_cumpleaños")

@client.command()
async def proximo_cumpleaños(ctx):
    fecha_hoy = date.today()
    fecha_hoy = fecha_hoy.strftime("%d/%m")
    servername = get_server_name(ctx, ".txt")
    dic_cumpleaños = lector_diccionario_txt(servername)
    lista_fechas = []
    for persona in dic_cumpleaños:
        lista_fechas.append([dic_cumpleaños[persona]])

    lista_resta_fechas = []
    for fecha in lista_fechas:
        resultado = fecha_hoy - fecha
    await ctx.send("La función está en desarrollo.")


@client.command()
async def borrar_cumpleaños(ctx, *mensaje):
    server_name = get_server_name(ctx, ".txt")
    dic_cumpleaños = lector_diccionario_txt(server_name)
    dic_cumpleaños = { key : value for key,value in dic_cumpleaños.items() if key != mensaje[0]}
    imprimir_dic_txt(server_name,dic_cumpleaños)
    
    await ctx.send("Borrado con éxito.")


@client.command()
async def ordenar_cumpleaños(ctx):
    server_name = get_server_name(ctx, ".txt")
    await ctx.send("En desarrollo...")


@client.command()
async def editar_cumpleaños(ctx):
    server_name = get_server_name(ctx, ".txt")
    dic_cumpleaños = lector_diccionario_txt(server_name)
    print(dic_cumpleaños)
    await ctx.send("Función todavía en desarrollo")


@client.command(aliases=["td", "tiempo_hasta", "th"])
async def tiempo_desde(ctx, *datos):
    if(len(datos) != 3):
        await ctx.send("Error, el formato es: dia mes año")
        return
    
    datos_num = []
    for dato in datos:
        if not dato.isdigit():
            await ctx.send("Error, el formato es: dia mes año")
            return
        else:
            datos_num.append(int(dato))
    
    error = False
    if (datos_num[0] < 0 or datos_num[0] > 31):
        error = True
    if (datos_num[1] < 0 or datos_num[1] > 12):
        error = True
    if (datos_num[2] < 0 ):
        error = True
    if(error):
        await ctx.send("Fecha invalida")
        return
    
    fecha_x = date(datos_num[2],datos_num[1],datos_num[0])
    fecha_hoy = date.today()
    fecha_delta = fecha_hoy - fecha_x
    
    dias = int(str(fecha_delta).split()[0])
    if (dias < -365 or dias > 365):
        años = int(dias//365.25)
    else: 
        años = 0
    dias_finales = dias - int(365.25*años)

    if(dias > 0):
        await ctx.send(f"pasaron {años} años y {dias_finales} días desde {datos_num[0]}-{datos_num[1]}-{datos_num[2]}")
    else: 
        await ctx.send(f"falta {años*-1} años y {dias_finales*-1} días para {datos_num[0]}-{datos_num[1]}-{datos_num[2]}")


@client.command(aliases=["whotfis","whois","who","whatis"])
async def showpic(ctx, *, search= "No ingresaste texto"):
        messageRancio = (
            "SETTXXAYAH","SETT X XAYAH", "XAYAHXSETT", "XAYAH X SETT","XAYAH AND SETT", "SETTANDXAYAH","XAYAHANDSETT","PORNO DE AMOGUS",
            "SETTXAYAH","XAYAHSETT","RULE 34", "RULE34","R34"
        )
        messageMayus = search.upper()
        if messageMayus in messageRancio:
            await ctx.send("rancio del orto")
        
        else: 
            try:
                ran = random.randint(0, 9)
                resource = build("customsearch", "v1", developerKey=api_key).cse()
                result = resource.list(q=f"{search}", cx="7a66f552d52dca626", searchType="image").execute()
                url = result["items"][ran]["link"]
                embed1 = discord.Embed(title=f"Acá está tu {search} pa: (Imagen numero {ran} de la api)") #{search.title()}
                embed1.set_image(url=url)
                await ctx.send(embed=embed1)
            except Exception:
                discord.ext.commands.errors.MissingRequiredArgument("te falto que buscar pa")

@client.command()
async def help(ctx):
    embed1 = discord.Embed(title="Lista de comandos terminados:")
    embed1.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed1.add_field(name=".whotfis .who .whatis", value="Usa CustomSearchAPI de google para buscar imagenes, su input es .whotfis busqueda, DESHABILITADO PORQUE ME DA PAJA LA API DE GOOGLE", inline=False)
    embed1.add_field(name=".sum .prom y .resta", value="regresa la operacion de todos los numeros separados por espacio.", inline=True)
    embed1.add_field(name=".emanuel", value="Literalmente emanuel.", inline=True)
    embed1.add_field(name=".conic", value="literalmente conic", inline=True)
    embed1.add_field(name=".impuesto", value="regresa su valor en impuestos, valor actual 66%", inline=True)
    embed1.add_field(name=".ran", value="regresa un valor aleatorio de todo item separado por espacio.", inline=True)
    embed1.add_field(name=".conictexto", value="literalmente conic texto", inline=True)
    embed1.add_field(name=".convertir_tiempo", value="devuelve en gmt-3 depende la hora dada con su zona, ej 12:00 pst", inline=True)
    embed1.add_field(name=".kappastats", value="devuelve el contador de kappas", inline=True) 

    #embed2 = discord.Embed(title = "BetaStatus")
    #embed2.add_field(name="En progreso:", value="contador de kappa, cumpleaños.", inline=False)
    #embed2.add_field(name="Planes futuros:", value="si", inline=False)
    await ctx.send(embed=embed1)
    #await ctx.send(embed=embed2)


@client.command(aliases = ["time_converter","gmt"])
async def convertir_tiempo(ctx, *datos:str):
    zonas = ["gmt","utc","pst", "cet", "est"]
    if(len(datos) != 2 or datos[1].lower() not in zonas):
        await ctx.send("Error, el formato correcto es -> .convertir_tiempo 11:30 utc ")
    else:
        aux = datos[0]
        aux = aux.split(':')
        hora = int(aux[0])
        minutos = int(aux[1])
        if(minutos < 10):
            minutos = f"0{minutos}"
        
        if(datos[1].lower() == "gmt" or datos[1].lower() == "utc"):
            await ctx.send(f"{hora}:{minutos} {datos[1]} -> {hora-3}:{minutos} UTC-3 (buenos aires)")
        elif (datos[1].lower() == "pst"):
            await ctx.send(f"{hora}:{minutos} {datos[1]} -> {hora+5}:{minutos} UTC-3 (buenos aires)")
        elif (datos[1].lower() == "est"):
            await ctx.send(f"{hora}:{minutos} {datos[1]} -> {hora+2}:{minutos} UTC-3 (buenos aires)")
        elif (datos[1].lower() == "cet"):
            await ctx.send(f"{hora}:{minutos} {datos[1]} -> {hora-4}:{minutos} UTC-3 (buenos aires)")

@client.command(alisases=["suma"])
async def sum(ctx, *num:float):
    value = 0
    for n in num:
        value += n
    await ctx.send(value)

@client.command(alisases=["substract"])
async def resta(ctx, *num:float):
    value = num[0]
    for n in num[1:]:
        value -= n
    await ctx.send(value)

@client.command(aliases=["impuestos", "imp","argentinizame"])
async def impuesto(ctx, num):
    impuesto = 1.66
    try:
        await ctx.send(f"Sería {round(float(num)*impuesto,2)}:mate: con un impuesto de {round((impuesto-1)*100)}%")
    except ValueError:
        num = num.split(",")
        num = num[0]+"."+num[1]
        await ctx.send(f"Sería {round(float(num)*impuesto,2)}:mate: con un impuesto de {round((impuesto-1)*100)}% ")

@client.command()
async def prom(ctx, *num:float):
    value = 0
    cont = 0
    for n in num:
        value += n
        cont += 1
    promedio = value / cont
    await ctx.send(promedio)

@client.command(aliases = ["puntos"])
async def puntosteam(ctx,valor:str,num:float=None):
    # 104 puntos = 100 ars
    await ctx.send("Función OUTDATED ya que la conversión se volvió simple (101 puntos-> 100 ars)")
    peso = ("PESO","PESOS")
    puntos = ("PUNTOS","PUNTO")
    if valor.upper() in peso:
        # 104 puntos -------- 100 ars
        # 1 punto --------- 0.96 ars
        valor_pesos = num * 0.96  
        await ctx.send(f"{num} puntos son {valor_pesos} pesos")
        return
    if valor.upper() in puntos:
        # 104 puntos -------- 100 ars
        # 1.04 punto --------- 1 ars
        valor_pesos = num * 1.04  
        await ctx.send(f"{num} pesos son {valor_pesos} puntos")
        return
    else: 
        await ctx.send("Por favor ingrese así: .puntos Peso/Puntos cantidad")
        await ctx.send("Recuerde que 104 puntos --------> 100 ars ")

@client.command()
async def ran(ctx, *element):
    elegido = random.choice(element)
    await ctx.send(elegido)

@client.command()
async def conic(ctx):
    #Proyectos\botdiscord\874.png
    file = discord.File("dependencias/874.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://874.png")
    await ctx.send(file=file, embed=embed)


@client.command(aliases=["retarded"])
async def emanuel(ctx):
    await ctx.send(file = discord.File("dependencias/emanuel.png"))

@client.command(aliases=["conictext", "conicsez","conictexto"])
async def conicsays(ctx,*,oracion = "No ingresaste texto"):
    if oracion == "nigga":
        oracion = "__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___"
        conica = Image.open("dependencias/874-white.png")
        letra = ImageFont.truetype("arial.ttf",24)
        dibuje = ImageDraw.Draw(conica)
        dibuje.text((285,214), oracion, (0,0,0), font=letra)
        conica.save("dependencias/text.png")
        await ctx.send(file= discord.File("dependencias/text.png"))
    else:
        conica = Image.open("dependencias/874-white.png")
        letra = ImageFont.truetype("arial.ttf",24)
        dibuje = ImageDraw.Draw(conica)
        dibuje.text((285,214), oracion, (0,0,0), font=letra)
        conica.save("dependencias/text.png")
        await ctx.send(file= discord.File("dependencias/text.png"))

@client.command(pass_context = True)
async def erase(ctx, number):
    mgs = [] 
    number = int(number) 
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)


@client.command()
async def online(ctx):
    await ctx.send("👍")

@client.command()
async def letspeedup(ctx):
    await ctx.send("https://youtu.be/5PyWmpQvkiM?t=6")

@client.command(aliases = ["sisi","SISI","si_si", "si si"])
async def SI_SI(ctx):
    await ctx.send(file= discord.File("dependencias/SI_SI.mp3"))

@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        await ctx.send("Comando no encontrado...")
        await ctx.send("Usá .help")
        

client.run('NDI5OTk0OTk1OTI0MDc0NDk3.WsDeCw.qxx57GV0RjX-T9S64HFkq_RiBuk')


