import discord
from discord.ext import commands

prefix = "" #nombre de tu prefix

client = commands.Bot(command_prefix=prefix)

@client.command()
async def verificame(ctx):
  nombre = "Verificado" #nombre del bot
  autor = ctx.message.author
  rol = discord.utils.get(autor.guild.roles, name=nombre)
  await autor.add_roles(rol)
  await ctx.reply('Fuiste verificado!')
  
def correrBot():
  print('El bot esta corriendo...')
  client.run(token)
  
correrBot()
