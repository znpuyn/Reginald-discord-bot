import discord 
from discord.utils import get
from discord.ext import commands

token = open("key.txt", "r")
bot = commands.Bot(command_prefix='$')

#Start of events==========================================================================================

@bot.event
async def on_connect():
    print ('I have successfully logged in as {0.user}'.format(bot))


@bot.event 
async def on_disconnect():
    print ("I have lost connection, please troubleshoot")


@bot.event
async def on_ready():
    server = bot.get_guild (715077503948947500)
    print ('I have fully initialized as {0.user}'.format(bot))
    print ('joined '+ str(server))

@bot.event
async def on_member_join(member):
    await member.send("Hello I am the official AI Academy bot, Reginald!\n"
    "You might notice that the AI Academy discord is empty, but that's not the case.\n" 
    "First, let me ask you, what locationg are you from?\n"
    "1. Nautilus Middle\n" 
    "2. Kinloch Park Middle\n"
    "3. NMB Library\n")
    await member.send("In addition, please be sure to read the wiki for my commands prior to calling me at:\n"
    "```[link to wiki]```")

#End of events=========================================================================================
#Start of commands=====================================================================================

@bot.command()
async def commands(ctx):
    await ctx.send("A list of my commands can be found on my wiki: ```[Link will go here]```")

@bot.command()
async def TAs(ctx):
    server = bot.get_guild(ctx.guild.id)
    await ctx.send("The following TAs are online:")
    async with ctx.typing():
        for TA in server.roles[9].members:
            if f'{TA.status}' == 'online':
                await ctx.send(f'```{TA.display_name}```')

@bot.command()
async def staff(ctx):
    server = bot.get_guild (ctx.guild.id)  
    await ctx.send("I'll notify one of the TAs to assign this role to you. Unfortunately it's for the best that I don't assign staff roles out like they were candy without some verification")
    await ctx.send(f'{ctx.author} is requesting to be designed as staff')
    for TA in server.roles[9].members:
        if f'{TA.status}' == 'online':
            await ctx.send(f'{TA.mention}')

@bot.command()
async def student(ctx):
    server = bot.get_guild (ctx.guild.id)
    member = server.get_member(ctx.author.id)
    await member.add_roles(server.roles[4], reason = 'user indicated they were a student', atomic = True)
    await ctx.send("You are now tagged as a student")
        
@bot.command()
async def password(ctx):
    await ctx.send(f"I will notify one of our TAs that you need assistance with your password for {arg}")
    server = bot.get_guild (ctx.guild.id)
    for name in server.roles[9].members: 
        if f'{name.status}' == 'online': 
            TA = bot.get_user(name.id)
    await TA.send(f"{ctx.author} requires assistance with their password for {arg}.")

@bot.command()
async def locations(ctx, arg):
    server = bot.get_guild (ctx.guild.id)
    member = server.get_member(ctx.author.id)
    if arg == 'info':
        await ctx.send("The following locations are available:\n 1. Kinloch Park Middle\n 2. Nautilus Middle\n 3. NMB Library")
    if arg == "1":
        for kp in member.roles[1:]:
            if kp.name == "Nautilus" or "NMB Library":
                await member.remove_roles(member.roles[1], reason='user attempted to enroll in multiple locations')
                await ctx.send(f"You can't be enrolled in multiple locations")
        await member.add_roles(server.roles[1], reason='user indicated they attend Kinloch Park', atomic = True)
        await ctx.send(f"You are now enrolled at {server.roles[1]} {ctx.author.mention}")
            
    if arg == "2":
        for naut in member.roles[1:]:
            if naut.name == "Kinloch Park" or "NMB Library":
                await member.remove_roles(member.roles[1], reason='user attempted to enroll in multiple locations')
                await ctx.send(f"You can't be enrolled in multiple locations")
        await member.add_roles(server.roles[2], reason='user indicated they attend Kinloch Park', atomic = True)
        await ctx.send(f"You are now enrolled at {server.roles[2]} {ctx.author.mention}")

    if arg == "3":
        for nmb in member.roles[1:]:
            if nmb.name == "Kinloch Park" or "Nautilus":
                await ctx.send(f"You can't be enrolled in multiple locations")
                await member.remove_roles(member.roles[1], reason='user attempted to enroll in multiple locations')
        await member.add_roles(server.roles[3], reason='user indicated they attend Kinloch Park', atomic = True)
        await ctx.send(f"You are now enrolled at {server.roles[3]} {ctx.author.mention}")

    if arg == 'purge':
        for n in member.roles[1:]:
            if n.name == "Kinloch Park" or n.name == "Nautilus"or n.name =="NMB Library":
                await member.remove_roles(member.roles[1], reason ='user requested a purge of location tags')
        await ctx.send(f"Purge completed")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello there {ctx.author.name}")

@bot.command()
async def students(ctx):
    server = bot.get_guild (ctx.guild.id)
    x = server.roles[4].members
    await ctx.send(f" AI Academy currently has:```{len(x)} students```")

@bot.command()
async def roles(ctx): 
    server = bot.get_guild (ctx.guild.id)
    member = server.get_member(ctx.author.id)
    member_roles = member.roles[1:]
    for name in member_roles:
        await ctx.send(f'```{name.name}```')

#End of commands=============================================================================================================

bot.run(token.read())