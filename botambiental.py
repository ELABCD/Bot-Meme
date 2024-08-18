import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$mem'):
        with open('imagenes/mem1.jpg', 'rb') as f:#fijar que la imagen se llame igual aca que en la carpeta imagenes
            picture = discord.File(f)
        await message.channel.send(file=picture)
    else:
        await message.channel.send(message.content)

client.run("MTI2NjUwNzQ1OTYwMjgwODg3Mg.GaWujy.yo8dxrEbTPp7jS_QsEV8OzJE5fLqlu2nD4N_K8")