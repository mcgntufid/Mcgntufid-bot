import os
os.system("color 04")
entry = input("Discord bot on off?")

if entry == 'on':
    import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='m!a', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Ace Communications | m!ahelp"))

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")


@bot.command()
async def report(ctx, DiscordMember, Reason):
    await ctx.send(f'✅Reported!: Report: {DiscordMember} Reason: {Reason} Thank you for reporting.')
    
@bot.command()
async def invite(ctx):
    await ctx.send("✅invite:https://discord.com/api/oauth2/authorize?client_id=1129013605505978469&permissions=8&scope=bot")

@bot.command()
async def embed(ctx, word3):
        embed.set_author(name=f'{word3}')

@bot.command()
async def google(ctx):
    embed = discord.Embed(title="Click me to open google",
                          url="https://google.com/",
                          colour=0x00b0f4)

    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="-------------------COMMANDS---------------",
                      description="m!acredits\nm!acustomwebsite\nm!adaily\nm!agif\nm!agoogle\nm!ahello\nm!ahelp                Shows this message\nm!ainvite\nm!aping\nm!apinguser {user} \nm!areport {user} {reason} \nm!aservers\nm!aembed {word}\nm!akick\nm!a\ban\nm!aunban\nm!amute ")

    embed.set_author(name="Help commands")

    embed.add_field(name="PREFIX",
                value="Bot prefix: m!a")
    embed.add_field(name="BOT INVITE",
                value="https://discord.com/api/oauth2/authorize?client_id=1129013605505978469&permissions=8&scope=bot")

    embed.set_image(url="https://cdn.discordapp.com/attachments/1137442027592765480/1138222817381466132/Screenshot_2023-08-08_001414.png")

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1137442027592765480/1138222817381466132/Screenshot_2023-08-08_001414.png")

    embed.set_footer(text="made by mcgntufid")

    await ctx.send(embed=embed)


@bot.command()
async def pinguser(ctx, DiscordMember):
    await ctx.send(f'{DiscordMember} ')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} kicked from the server.")

@bot.command()
async def mute(ctx, member: discord.Member = None, *, reason=None):

    guild = ctx.guild
    mute_role = discord.utils.get(ctx.guild.roles, name='Staff')
   
    await member.add_roles(Muted)
    await member.send("You were muted for reason: " + reason)

    await ctx.send(f'{member} has been muted because : ' + reason)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} banned from the server.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.User, *, reason=None):
    await ctx.guild.unban(member, reason=reason)
    await ctx.send(f"{member} unbanned.")

@bot.command()
async def servers(ctx):
    await ctx.send("انا 7 servers")


@bot.command()
async def customwebsite(ctx, Website):
    await ctx.send(f'https://{Website}')


@bot.command()
async def gif(ctx, nameandid):
    await ctx.send(f'https://tenor.com/view/{nameandid}')

@bot.command()
async def credits(ctx):
    await ctx.send("مالك bot: mcgntufid || كود : discord.py")

@bot.command()
async def daily(ctx):
    await ctx.send("✅فلوس: 1000 (fake) ")
bot.run('MTE5ODg3MzI0NDI3NTU5MzM1Nw.G3IWdM.JUyEX4E-KLuUosTenjALy90LMCqezzgS02jT5w')

if entry == 'off':
    print("Ok.")
    input()