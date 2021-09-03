import logging
import discord 
from discord.utils import get
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True

token = open("key.txt", "r")
bot = commands.Bot(command_prefix='$', intents=intents)

#Start of events==========================================================================================

@bot.event
async def on_connect():
    print ('I have successfully logged in as {0.user}'.format(bot))


@bot.event 
async def on_disconnect():
    print ("I have lost connection, please troubleshoot")


@bot.event
async def on_ready():
    server = bot.get_guild (692127526071566387)
    print ('I have fully initialized as {0.user}'.format(bot))
    print ('joined '+ str(server))

@bot.event
async def on_member_join(member):
    await member.send("Hello I am the official AI Academy bot, Reginald!\n"
    "You might notice that the AI Academy discord is empty, but that's not the case. The channels are hidden and require specific tags to see\n" 
    await member.send("please be sure to read the wiki for my commands prior to requesting assistance from the TAs:\n"
    "```[https://github.com/znpuyn/Reginald-discord-bot/wiki]```\n"
    "I accept commands in all text channels that you can type into so do not worry about channel specific restrictions place onto myself")

#End of events=========================================================================================
#Start of commands=====================================================================================

@bot.command()
async def commands(ctx):
    await ctx.send("A list of my commands can be found on my wiki: ```[https://github.com/znpuyn/Reginald-discord-bot/wiki/Commands]```")

@bot.command()
async def TAs(ctx):
    server = bot.get_guild(ctx.guild.id)
    await ctx.send("The following TAs are online:")
    async with ctx.typing():
        TA_position = 0
        for x in server.roles:
            if x.id == 692130820411883601:
                break
            if x != 692130820411883601:
                TA_position += 1
        
        for TA in server.roles[TA_position].members:
            if f'{TA.status}' == 'online':
                await ctx.send(f'```{TA.display_name}```')

@bot.command()
async def staff(ctx):
    server = bot.get_guild (ctx.guild.id)  
    await ctx.send("I'll notify one of the TAs to assign this role to you. Unfortunately it's for the best that I don't assign staff roles out like they were candy without some verification")
    await ctx.send(f'{ctx.author} is requesting to be designed as staff')
    TA_position = 0
    for x in server.roles:
        if x.id == 692130820411883601:
                break
        if x != 692130820411883601:
                TA_position += 1
    for TA in server.roles[TA_position].members:
        if f'{TA.status}' == 'online':
            await ctx.send(f'{TA.mention}')

@bot.command()
async def student(ctx):
    server = bot.get_guild (ctx.guild.id)
    member = server.get_member(ctx.author.id)
    student_position = 0
    for x in server.roles:
        if x.id == 692130778582089878:
                break
        if x != 692130778582089878:
                student_position += 1
    await member.add_roles(server.roles[student_position], reason = 'user indicated they were a student', atomic = True)
    await ctx.send("You are now tagged as a student")
        
@bot.command()
async def password(ctx, arg):
    await ctx.send(f"I will notify one of our TAs that you need assistance with your password for {arg}")
    server = bot.get_guild (ctx.guild.id)
    TA_position = 0
    for x in server.roles:
        if x.id == 692130820411883601:
                break
        if x != 692130820411883601:
                TA_position += 1

    for name in server.roles[TA_position].members: 
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
    else:
        print("I'm sorry, you forgot to provide an argument so I can't provide assistance. Please refer to my wiki on what arguments to use. To see my wiki use the $wiki command and follow the link provided.3")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello there {ctx.author.name}")

@bot.command()
async def students(ctx):
    server = bot.get_guild (ctx.guild.id)
    student_role = 0
    for x in  server.roles:
        if x.id == 692130778582089878:
            break
        if x.id != 692130778582089878:
            student_role += 1
        
    x = server.roles[student_role].members
    await ctx.send(f" AI Academy currently has:```{len(x)} students```")

@bot.command()
async def roles(ctx): 
    server = bot.get_guild (ctx.guild.id)
    member = server.get_member(ctx.author.id)
    member_roles = member.roles[1:]
    for name in member_roles:
        await ctx.send(f'```{name.name}```')

@bot.command()
async def purge(ctx, arg):
    server = bot.get_guild (ctx.guild.id)
    ops = 0
    for x in server.roles:
        if x.id == 692131193151291412:
                break
        if x.id != 692131193151291412:
                ops += 1
    ops_list = server.roles[ops].members
    print (ops_list)
    author_is_op = 0
    for x in ops_list:
        if ctx.author == x:
            author_is_op = 1
    
    if author_is_op == 1:
        if arg == ("server"):
            await ctx.send(f"ok purging the discord now. please wait a moment")

            #purge code, possbibly unstable until live tested. 
            student_role = 0
            for x in  server.roles:
                if x.id == 692130778582089878:
                     break
                if x.id != 692130778582089878:
                    student_role += 1
            students = server.roles[student_role].members
            num_kicked = 0
            num_kicked += len(students)
            for x in students:
                await server.kick (x, reason="Program has ended for the year")
            await ctx.send(f"The purge is complete, all users with " + (server.roles[student_role].name) + " have been purged from the discord.")
            await ctx.send(f"That's "+str(num_kicked)+" students removed from this server.")
            
    if author_is_op == 0:
        await ctx.send(f"You don't have the right permissions for that")

@bot.command()
async def wiki(ctx):
    await ctx.send(f"My wiki can be found at this URL: https://github.com/znpuyn/Reginald-discord-bot/wiki")




#End of commands=============================================================================================================

logging.basicConfig(level=logging.INFO)
bot.run(token.read())