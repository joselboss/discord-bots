@client.command()
async def avatar(ctx,*,member:discord.Member):
  await ctx.reply(member.avatar_url)
  print(f'{ctx.author.name} corrio el comando avatar')
