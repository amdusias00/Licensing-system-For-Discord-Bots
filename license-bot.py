import discord
from discord.ext import commands
from datetime import datetime
from datetime import timedelta
import yaml
from discord_webhook import DiscordWebhook
from datetime import date
import os
def date1(ct1, ct2):
    ctstr1 = str(ct1)
    ctstr2 = str(ct2)
    Begindatestring = date.today()
    directory_path = os.getcwd()
    Enddate = Begindatestring + timedelta(days=ct1)
    x47 = "./licexp/"+str(Enddate)+".txt"
    with open(x47, 'a') as f:
        f.writelines("\n"+ctstr2)




def chekexp():
    Begindatestring = date.today()
    directory_path = os.getcwd()
    Enddate = Begindatestring
    x4 = "./licexp/"+str(Enddate)+".txt"
    if os.path.exists(x4):
        webhook = DiscordWebhook(url=config['webhook'], username="FLAVO shop On top !",content='The useranames ON This txt musnt have role anymore !')


        with open(x4, "rb") as f:
            webhook.add_file(file=f.read(), filename=x4)


        response = webhook.execute()
    else:


        webhook = DiscordWebhook(url=config['webhook'], content='No Lics Expires To day')
        response = webhook.execute()



def regdateyear():
    from datetime import date
    Begindatestring = date.today()
    Enddate = Begindatestring + timedelta(days=365)

    x4 = "./licexp/"+str(Enddate)+".txt"
    if os.path.exists(x4):
        print("Ex")
    else:
        fp = open(x4, 'x')
        fp.close()
def regdate6month():
    from datetime import date
    Begindatestring = date.today()
    Enddate = Begindatestring + timedelta(days=180)

    x4 = "./licexp/"+str(Enddate)+".txt"
    if os.path.exists(x4):
        print("Ex")
    else:
        fp = open(x4, 'x')
        fp.close()
def regdate3month():
    from datetime import date
    Begindatestring = date.today()
    Enddate = Begindatestring + timedelta(days=90)

    x4 = "./licexp/"+str(Enddate)+".txt"
    if os.path.exists(x4):
        print("Ex")
    else:
        fp = open(x4, 'x')
        fp.close()
def regdate1month():
    from datetime import date
    Begindatestring = date.today()
    Enddate = Begindatestring + timedelta(days=30)

    x4 = "./licexp/"+str(Enddate)+".txt"
    if os.path.exists(x4):
        print("Ex")
    else:
        fp = open(x4, 'x')
        fp.close()

    

with open("./config.yml", 'r') as file:
    config = yaml.load(file, Loader = yaml.Loader)


client = commands.Bot(command_prefix =config['Prefix'])
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Flavo shop"))
    print('License Bot - READY !')
@client.command()
async def chektodayexplics(ctx):
    chekexp()
@client.command()
async def redeemyear(ctx, arg1):
    await ctx.message.delete()
    with open(config['SerialFile']) as license_file:
        if arg1 in license_file.read():
            embed2=discord.Embed(title=config['ValidTitle'], color=0x00ff00)
            embed2.add_field(name=config['ValidName'], value=config['ValidValue'], inline=False)
            embed2.set_author(
                            name = ctx.author.name,
                            icon_url = ctx.author.avatar_url)
            embed2.set_footer(text=config['ValidFooter'])
            await ctx.send(embed=embed2)
            role = discord.utils.get(ctx.guild.roles, name=config['RoleName'])
            user = ctx.message.author
            await user.add_roles(role)
            print('Valid license: ', str(user), arg1)
        else:
            embed2=discord.Embed(title=config['InvalidTitle'], color=0xFF0000)
            embed2.set_author(
                            name = ctx.author.name,
                            icon_url = ctx.author.avatar_url)
            embed2.set_footer(text=config['InvalidFooter'])
            await ctx.send(embed=embed2)
            print('Invalid license: ', str(user), arg1)
        with open(config['SerialFile'],"r+") as f:
            file_content = f.readlines()
            f.seek(0)
            for line in file_content:
                if arg1 not in line:
                    f.write(line)
            f.truncate()
    x87 = int(ctx.message.author.id)
    regdateyear()
    date1(365,x87)
    chekexp(365)
@client.command()
async def redeem6month(ctx, arg1):
    await ctx.message.delete()
    with open(config['SerialFile6month']) as license_file:
        if arg1 in license_file.read():
            embed2=discord.Embed(title=config['ValidTitle'], color=0x00ff00)
            embed2.add_field(name=config['ValidName'], value=config['ValidValue6'], inline=False)
            embed2.set_author(
                            name = ctx.author.name,
                            icon_url = ctx.author.avatar_url)
            embed2.set_footer(text=config['ValidFooter'])
            await ctx.send(embed=embed2)
            role = discord.utils.get(ctx.guild.roles, name=config['RoleName'])
            user = ctx.message.author
            await user.add_roles(role)
            print('Valid license: ', str(user), arg1)
        else:
            embed2=discord.Embed(title=config['InvalidTitle'], color=0xFF0000)
            embed2.set_author(
                            name = ctx.author.name,
                            icon_url = ctx.author.avatar_url)
            embed2.set_footer(text=config['InvalidFooter'])
            await ctx.send(embed=embed2)
            print('Invalid license: ', str(user), arg1)
        with open(config['SerialFile6month'],"r+") as f:
            file_content = f.readlines()
            f.seek(0)
            for line in file_content:
                if arg1 not in line:
                    f.write(line)
            f.truncate()    
    regdate6month()
@client.command()
async def redeem3month(ctx, arg1):
    await ctx.message.delete()
    with open(config['SerialFile3month']) as license_file:
        if arg1 in license_file.read():
            embed2=discord.Embed(title=config['ValidTitle'], color=0x00ff00)
            embed2.add_field(name=config['ValidName'], value=config['ValidValue3'], inline=False)
            embed2.set_author(
                            name = ctx.author.name,
                            icon_url = ctx.author.avatar_url)
            embed2.set_footer(text=config['ValidFooter'])
            await ctx.send(embed=embed2)
            role = discord.utils.get(ctx.guild.roles, name=config['RoleName'])
            user = ctx.message.author
            await user.add_roles(role)
            print('Valid license: ', str(user), arg1)
        else:
            embed2=discord.Embed(title=config['InvalidTitle'], color=0xFF0000)
            embed2.set_author(
                            name = ctx.author.name,
                            icon_url = ctx.author.avatar_url)
            embed2.set_footer(text=config['InvalidFooter'])
            await ctx.send(embed=embed2)
            print('Invalid license: ', str(user), arg1)
        with open(config['SerialFile3month'],"r+") as f:
            file_content = f.readlines()
            f.seek(0)
            for line in file_content:
                if arg1 not in line:
                    f.write(line)
            f.truncate() 
    regdate3month()            
@client.command()   
async def redeem1month(ctx, arg1):
    await ctx.message.delete()
    with open(config['SerialFile1month']) as license_file:
        if arg1 in license_file.read():
            embed2=discord.Embed(title=config['ValidTitle'], color=0x00ff00)
            embed2.add_field(name=config['ValidName'], value=config['ValidValue1'], inline=False)
            embed2.set_author(
                            name = ctx.author.name,
                            icon_url = ctx.author.avatar_url)
            embed2.set_footer(text=config['ValidFooter'])
            await ctx.send(embed=embed2)
            role = discord.utils.get(ctx.guild.roles, name=config['RoleName'])
            user = ctx.message.author
            await user.add_roles(role)
            print('Valid license: ', str(user), arg1)
        else:
            embed2=discord.Embed(title=config['InvalidTitle'], color=0xFF0000)
            embed2.set_author(
                            name = ctx.author.name,
                            icon_url = ctx.author.avatar_url)
            embed2.set_footer(text=config['InvalidFooter'])
            await ctx.send(embed=embed2)
            print('Invalid license: ', str(user), arg1)
        with open(config['SerialFile1month'],"r+") as f:
            file_content = f.readlines()
            f.seek(0)
            for line in file_content:
                if arg1 not in line:
                    f.write(line)
            f.truncate()      
    regdate1month()      
client.run(config['TOKEN'])
