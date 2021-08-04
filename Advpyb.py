#Importing the Libraries which are used

import discord
import tok as tokenid
from discord import colour
from discord.ext import commands
import random
from aiohttp import request
import json
import requests

#Setting A Prefix to Run the Bot 
cli=commands.Bot(command_prefix="@")

#Command:1 To show the Simple Output 
@cli.command()
async def Welcome(ctx):
    await ctx.send("Welcome :Thanks For using Bot")
    
#Command:2 To show the Random Value in Store this List
@cli.command(aliases=['ran22','rando1'])

async def Ask(ctx,*,question):
    ran_var_list=["he is a devil","Yes","No","Not Sure","he is Not a human"]
    var_ran=random.choice(ran_var_list)
    await ctx.send(var_ran)

#Command:3 To Ban the People who are in our group (Creating permission command )
@cli.command()
@commands.has_permissions(ban_members=True)
async def Ban(ctx,member:discord.User=None,*, reason=None):
    if reason == None:
        reason ="Go in trashbin"
    if member==None or member ==ctx.message.author:
        await ctx.channel.send("can't ban yourself")
    await member.ban(reason=reason)
    await ctx.channel.send(f"{member} has been banned.") 
    
#Command:4 To Kick the Member in our group
@cli.command()
# @commands.has_permissions(kick_memebers=True)
async def Kick(ctx,member:discord.User=None,*,reason=None):
    if reason == None:
        reason="no reasons given"
    await member.kick(reason=reason)
    await ctx.channel.send(f"{member} has been kicked")

#Command:6 To Show the Cat Facts (Using API)Show Random Sentence for  Cat Facts
@cli.command()
async def Catfact(ctx):
    data=requests.get('https://catfact.ninja/fact').json()
    embed = discord.Embed(colour=0x2bc7ff,title=f'Cat Fact',description=f'{data["fact"]}')
    await ctx.send(embed=embed)
 
 #Command:7 To Show the Dog Facts (Using API)Show Random Sentence for  Dog Facts   
@cli.command()
async def Dogfact(ctx):
    data=requests.get('https://dog-api.kinduff.com/api/facts?number=1').json()
    embed = discord.Embed(colour=0x2bc7ff,title=f'Dog Fact',description=f'{data["facts"][0]}')
    await ctx.send(embed=embed)

#To run the TokenId and Check the TokenId in the Discord
cli.run(tokenid.tokenid)
   