
# ideas
# 
# buscador y reproductor youtube
# 
# porcentaje error pong minijuego
#
#
#


import discord
from discord import channel
from discord.ext import commands
import os
from PIL import Image, ImageDraw, ImageFont
from discord.ext.commands import context
from discord.ext.commands.errors import PrivateMessageOnly
from discord.ext.commands.help import HelpCommand
from googleapiclient.discovery import build
import random
import json
import youtube_dl


client = commands.Bot(command_prefix=".", help_command= None)
api_key = "AIzaSyCsPj0Mb3F4Vf9AyFeZj4UkOr1wl2SKeg4"


@client.event
async def on_ready():
    print('Buenas, soy agustin bot')



@client.event
async def on_message(message):
    # mensajes
    #autodeteccion
    if message.author == client.user:
        return   
    """#ping/pong
    if message.content.find("Ping") != -1 or message.content.find("ping") != -1:
        await message.channel.send("Pong") 
    if message.content.find("Pong") != -1 or message.content.find("pong") != -1:
        await message.channel.send("Ping")
    """     
    if message.content.find("ty bot") != -1:
        await message.channel.send("de nada pa, besos en la cola")

    await client.process_commands(message)

        

    #if message.content.find(".play") != -1:
    #    await message.channel.send("*El pajero de mi programador no me programo para eso todavía*")

@client.command()
async def registrar_cumpleaños(ctx, *mensaje):
    #<discord.ext.commands.context.Context object at 0x0000024FA7F11AC0>
    lista_car_invalidos = ("?","(",")","-","¿",".",",","¿")
    diccionario_cumpleaños = {}
    separador = " "
    server_name = ctx.message.guild.name
    for letra in server_name:
        if letra in lista_car_invalidos:
            server_name = server_name.replace(letra,"")
    server_name = server_name.replace(" ","_")
    server_name = (server_name+".txt").replace(" ","")
 
    cumples_txt = open(server_name, "a")
    mensaje = list(mensaje)
    diccionario_cumpleaños[mensaje[0]] = mensaje[1]
    texto_diccionario_cumpleaños = separador.join(diccionario_cumpleaños)
    texto_diccionario_cumpleaños_llaves = separador.join(diccionario_cumpleaños.values())
    cumples_txt.write(f"\n{str(texto_diccionario_cumpleaños)}: {texto_diccionario_cumpleaños_llaves}")
    cumples_txt.close()
    
    # diccionario_cumpleaños = {}
    # lista_car_invalidos = ("?","(",")","-","¿",".",",","¿")
    # server_name = ctx.message.guild.name
    # for letra in server_name:
    #     if letra in lista_car_invalidos:
    #         server_name = server_name.replace(letra,"")
    # server_name = server_name.replace(" ","_")
    # server_name = (server_name+".json").replace(" ","")
    

    # mensaje = list(mensaje)
    
    # diccionario_cumpleaños[mensaje[0]] = mensaje[1]
    
    # data = json.dump(diccionario_cumpleaños)

    # file = open(server_name,"a")
    # file.write(data)
    # file.close

    await ctx.send("Cumpleaños registrado con exito.")

@client.command()
async def tabla_cumpleaños(ctx):
    lista_car_invalidos = ("?","(",")","-","¿",".",",","¿")
    server_name = ctx.message.guild.name
    for letra in server_name:
        if letra in lista_car_invalidos:
            server_name = server_name.replace(letra,"")
    server_name = server_name.replace(" ","_")
    server_name = (server_name+".txt").replace(" ","")
    await ctx.send("Acá están los cumpleaños registrados para este server",file= discord.File(server_name))

@client.command()
async def cumpleaños(ctx):
    await ctx.send("La función está en desarrollo.")

@client.command()
async def remove_cumpleaños(ctx):
    lista_car_invalidos = ("?","(",")","-","¿",".",",","¿")
    server_name = ctx.message.guild.name
    for letra in server_name:
        if letra in lista_car_invalidos:
            server_name = server_name.replace(letra,"")
    server_name = server_name.replace(" ","_")
    server_name = (server_name+".txt").replace(" ","")

    

    await ctx.send("La función está en desarrollo.")

@client.command()
async def ordenar_cumpleaños(ctx):
    lista_car_invalidos = ("?","(",")","-","¿",".",",","¿")
    server_name = ctx.message.guild.name
    for letra in server_name:
        if letra in lista_car_invalidos:
            server_name = server_name.replace(letra,"")
    server_name = server_name.replace(" ","_")
    server_name = (server_name+".txt").replace(" ","")

    diccionario_cumpleaños = {}
    with open(server_name, "r") as archivo:
        for linea in archivo:
            #['21/07: bromuro']
            linea = linea.strip().split(",")
            (llave,valor) = linea[0].split()
            diccionario_cumpleaños[llave] = valor

    with open(server_name,"w") as archivo:    
        diccionario_cumpleaños_ordenado = {}
        for llave, valor in diccionario_cumpleaños.items():
            diccionario_cumpleaños_ordenado[valor] = llave
        for cumpleaño in diccionario_cumpleaños_ordenado:
            archivo.write(f"{str(cumpleaño)}: {str(diccionario_cumpleaños_ordenado[cumpleaño])}\n")

    await ctx.send("Listo, verificar con tabla_cumpleaños")

@client.command()
async def editar_cumpleaños(ctx, *mensaje):
    lista_car_invalidos = ("?","(",")","-","¿",".",",","¿")
    server_name = ctx.message.guild.name
    for letra in server_name:
        if letra in lista_car_invalidos:
            server_name = server_name.replace(letra,"")
    server_name = server_name.replace(" ","_")
    server_name = (server_name+".txt").replace(" ","")

    diccionario_cumpleaños = {}
    with open(server_name, "r") as archivo:
        for linea in archivo:
            #['21/07: bromuro']
            linea = linea.strip().split(",")
            (llave,valor) = linea[0].split()
            diccionario_cumpleaños[llave] = valor
        
    diccionario_cumpleaños[mensaje[0]] = mensaje[1]
    if mensaje[0] in diccionario_cumpleaños:
        diccionario_cumpleaños=diccionario_cumpleaños.pop(mensaje[0])
        diccionario_cumpleaños[mensaje[0]] = mensaje[1]
        print(diccionario_cumpleaños)

    # with open(server_name, "w") as archivo:
    #     for cumpleaño in diccionario_cumpleaños:
    #         archivo.write(f"{str(cumpleaño)} {str(diccionario_cumpleaños[cumpleaño])}\n")

    await ctx.send("Función todavía en desarrollo")

@client.command(aliases=["whotfis","whois","who","whatis"])
async def showpic(ctx, *, search= "No ingresaste texto"):
        messageRancio = (
            "SETTXXAYAH","SETT X XAYAH", "XAYAHXSETT", "XAYAH X SETT","XAYAH AND SETT", "SETTANDXAYAH","XAYAHANDSETT","PORNO DE AMOGUS","SETTXAYAH","XAYAHSETT",
            "RULE 34", "RULE34","R34"
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
    embed1.add_field(name=".whotfis .who .whatis", value="Usa CustomSearchAPI de google para buscar imagenes, su input es .whotfis busqueda", inline=False)
    embed1.add_field(name=".sum", value="regresa la suma, input = num1 num2 numN...", inline=True)
    embed1.add_field(name=".prom", value="regresa su promedio, input = num1 num2 numN...", inline=True)
    embed1.add_field(name=".conic", value="literalmente conic", inline=True)
    embed1.add_field(name=".impuesto", value="regresa su valor en impuestos, valor actual 65%", inline=True)
    embed2 = discord.Embed(title = "BetaStatus")
    embed2.add_field(name="En progreso:", value="Juego pingpong, random choice, conictexto (joer encima texto), cumpleaños.", inline=False)
    embed2.add_field(name="Planes futuros:", value="Reproductor youtube.", inline=False)
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)

@client.command()
async def sum(ctx, *num:float):
    value = 0
    for n in num:
        value += n
    await ctx.send(value)

@client.command(aliases=["impuestos", "imp","argentinizame"])
async def impuesto(ctx, num):
    impuesto = 1.65
    await ctx.send(f"Sería {int(num)*impuesto} con un impuesto de {round((impuesto-1)*100)}%")


@client.command()
async def prom(ctx, *num:float):
    value = 0
    cont = 0
    for n in num:
        value += n
        cont += 1
    promedio = value / cont
    await ctx.send(promedio)

@client.command()
async def ran(ctx, *element):
    elegido = random.choice(element)
    await ctx.send(elegido)

@client.command()
async def conic(ctx):
    #Proyectos\botdiscord\874.png
    file = discord.File("874.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://874.png")
    await ctx.send(file=file, embed=embed)

@client.command(aliases=["conictext", "conicsez"])
async def conicsays(ctx,*,oracion = "No ingresaste texto"):
    if oracion == "nigga":
        oracion = "__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___"
        conica = Image.open("874-white.png")
        letra = ImageFont.truetype("arial.ttf",24)
        dibuje = ImageDraw.Draw(conica)
        dibuje.text((285,214), oracion, (0,0,0), font=letra)
        conica.save("text.png")
        await ctx.send(file= discord.File("text.png"))
    else:
        conica = Image.open("874-white.png")
        letra = ImageFont.truetype("arial.ttf",24)
        dibuje = ImageDraw.Draw(conica)
        dibuje.text((285,214), oracion, (0,0,0), font=letra)
        conica.save("text.png")
        await ctx.send(file= discord.File("text.png"))

@client.command()
async def online(ctx):
    #cambiar a reacción '👍'
    await ctx.send("https://www.youtube.com/watch?v=pQ-bjZD1EnI")

"""
@client.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')
"""


client.run('NDI5OTk0OTk1OTI0MDc0NDk3.WsDeCw.qxx57GV0RjX-T9S64HFkq_RiBuk')


