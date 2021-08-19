#Importing the Libraries which are used

import discord
from discord.embeds import Embed
import tok as tokenid
from discord import colour
from discord.ext import commands
import random
from aiohttp import request
import json
import requests

#Setting A Prefix to Run the Bot 
cli=commands.Bot(command_prefix=".")

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

#Commands:5 To Unban the Memeber in our group (Using Member Id)
@cli.command()
async def Unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if ( user.discriminator) == ( member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} have been unbanned sucessfully")
    return

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
    
#Command:8 To Get the Random Meme on reddit
@ cli.command(pass_context=True)
async def Meme(ctx):
    data=requests.get('https://reddit-meme-api.herokuapp.com/').json()
    await ctx.send(f'{data["url"]}')
    
#Command:9 To Get the information related Bot and User
@ cli.command()
async def Userinfo(ctx,member:discord.Member=None):
    member = ctx.author if not member else member
    embed=discord.Embed(colour=member.color)
    
    embed.set_author(name=f"User info-{member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
    
    embed.add_field(name="Username:",value=member.display_name)
    embed.add_field(name="Created at:",value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="joined at:",value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    
    embed.add_field(name="ID",value=member.id)
    embed.add_field(name="BOT",value=member.bot)
    
    await ctx.send(embed=embed)
    
    
#Command:10 To Get the Command And his Information
cli.remove_command('help')#To disable the Help default function 
@cli.command()
async def Help(ctx):

    embed = discord.Embed()
    embed.set_author(name=f"**Here is the list of commands you can use**")
    embed.set_footer(text=f"For Feedback contact {ctx.author}")
    
    embed.add_field(name="Welcome",value="> Shows Welcome Message")
    embed.add_field(name=" Ask",value="> Gives Random Answers")
    embed.add_field(name="Ban",value="> Can Ban the Members (Admin Rights Required)")
    
    embed.add_field(name=" Kick ",value="> Can Kick the Members (Admin Rights Required)")
    embed.add_field(name=" Unban  ",value="> Can Unban the Members(Using Member-ID) (Admin Rights Required)")
    embed.add_field(name="Catfact",value="> Can Show the Cat Facts (Admin Rights Required)")
    
    embed.add_field(name="Dogfact",value="> Can Show the Dog Facts (Admin Rights Required)")
    embed.add_field(name=" Meme ",value="> Can Show The random meme Which are Fetch on the Reddit App")
    embed.add_field(name="Userinfo",value="> To find the User information like join the Discord,Name with ID,bot or not, Etc.")
     
    await ctx.send(embed=embed)
#To run the TokenId and Check the TokenId in the Discord
cli.run(tokenid.tokenid)
   
   