import discord
from discord.ext import commands
import os
from oyun import *
import random 
import asyncio


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
game = Game()

@client.event
async def on_ready():
    print("Merhaba, ben hazırım!")

  
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"{member} aramıza katıldı, hoşgeldin :)")
    print(f"{member} aramıza katıldı, hoşgeldin :)")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"{member} aramızdan ayrıldı :(")
    print(f"{member} aramızdan ayrıldı :(")

#kullanıcı bilgileri
@ client.command ( aliases = [ 'kullanıcı' , 'kimo' ] ) 
async def kullanıcı_bilgisi ( ctx , member : discord.Member = None ) :
  if member == None :
    member = ctx.message.author 
  roles = [ role for role in member.roles ] 
  embed = discord.Embed ( title= " User info " , description = f" Kullanıcı bilgileri { member.mention } " , color = discord.Color.green ( ) , timestamp = ctx.message.created_at ) 
  embed.set_thumbnail ( url=member.avatar ) 
  embed.add_field (name= " ID " , value = member.id ) 
  embed.add_field (name= " Name ", value = f" { member.name } # { member.discriminator } " ) 
  embed.add_field (name= " Nickname " , value = member.display_name ) 
  embed.add_field (name= " Status " , value = member.status ) 
  embed.add_field (name= f" Roles ( { len ( roles ) } ) " , value = " " .join ( [ role.mention for role in roles ] ) ) 
  embed.add_field (name= " Top Role " , value = member.top_role.mention ) 
  embed.add_field (name= " Bot ? " , value=member.bot )
  await ctx.send ( embed=embed )

#hesap yaptırma
@ client.command(aliases = ['hesap', 'işlem'] ) 
async def mat(ctx, expression): 
  symbols = ['+', '-', '/', '*', '%']
  if any(s in expression for s in symbols): 
    calculated = eval(expression) 
    embed = discord.Embed(title="Matematik İşlemi", description = f" Soru=  {expression}\nCevap=  {calculated}", color= discord.Color.green(), timestamp=ctx.message.created_at) 
  else: 
      await ctx.send("Bu bir matematik işlemi değil") 
  await ctx.send(embed=embed)


@client.command(aliases=['topaç'])
async def zar(ctx, yuz:int=6):
  number=random.randint(1,yuz)
  await ctx.send(number)
  

@client.command(aliases=['karar'])
async def seç(ctx, *, args):
  arguments = args.split(" ")
  choice = random.choice(arguments)
  thinking = await ctx.send(":clock12: Bi Düşüneyim...")
  await asyncio.sleep(0.2)
  for i in range(4):
    await thinking.edit(content=f":clock{i+1}: Düşüneyim...")
    await asyncio.sleep(0.2)
  await ctx.send(choice)


@client.command(aliases=['atmak', 'para']) 
async def yazı_tura(ctx, seçim): 
  values = ['yazı', 'tura'] 
  computerChoice = random.choice(values) 
  if seçim not in values: 
    await ctx.send("Tahminini alayım: ") 
  else : 
    if computerChoice == seçim:
      await ctx.send(f"Doğru tahmin, {seçim }") 
    elif computerChoice != seçim: 
      await ctx.send(f"Yanlış tahmin, {computerChoice}")


@client.command()
async def bilgi(ctx, *args):
  if "küçük" in args:
    await ctx.send(game.küçük_sayı())
  elif "büyük" in args:
    await ctx.send(game.büyük_sayı())
  else:
    await ctx.send('Merhaba. Bu bot için kullanılabilir kodlar: !bilgi ,  !bilgi küçük ,  !bilgi büyük , !kullanıcı @... , !kimo @... , !mat ...,!seç ... ... !yazı_tura ...')
                    
client.run(os.getenv("TOKEN"))