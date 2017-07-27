
import discord
import random
import math
from datetime import *
from discord.ext.commands import Bot
import base64
from discord.ext import commands

def encrypt(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decrypt(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)




client = Bot(command_prefix=";")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await discord.Client.change_presence(client,game=discord.Game(name=";help | Made by Yohimbo"))


@client.event
async def on_message(message):
    if message.content.startswith("djinn"):
        f = open("words.txt",'r+')
        words = f.read()
        
        words2 = words[random.randint(0,len(int(len(words))))]
        return await client.send_message(message.channel,words)
    await client.process_commands(message)
    
@client.command()
async def tns(x : int):
    """ toggles nsfw [0/1] """
    global nsfw
    if x == 0:
        nsfw = False
        return await client.say(nsfw)
    elif x == 1:
        nsfw = True
        return await client.say(nsfw)
    toggle()
    await client.say("NSFW is: " + nsfw)
@client.command()
async def gns():
    """get whether or now NSFW is enabled"""
    return await client.say(nsfw)


@client.command()
async def ass():
    """shows asses"""
    
    asslist = ['http://i.imgur.com/VBQexlY.jpg','http://i.imgur.com/lBB6D0E.jpg','http://i.imgur.com/wVfvPzw.jpg','https://fat.gfycat.com/ForcefulVigorousKangaroo.gifv',]
    if nsfw == False:
        return await client.say("NSFW is not allowed in this server. use ;togglensfw to toggle NSFW on/off")
    elif nsfw == True:
        return await client.say(random.choice(asslist))

@client.command()
async def noods():
    """Sends noods"""
    noodlist = ['http://i.imgur.com/8fpiqyX.gifv','http://i.imgur.com/XB4S1cq.jpg','http://i.imgur.com/eH0kX2r.gifv']
    return await client.say(random.choice(noodlist))

@client.command()
@commands.has_permissions(manage_messages = True)
async def purgeamount(amount : int):
    amounta = amount
    global xin
    xin = int(amounta)
    return await client.say("amount to purge: %s" % amounta)
@client.command()
async def purge(*ChannelID : str):
    """Purges 500 or less messages from the target channel"""
    def is_me(m):
        return m.author != client.user
                                
    deleted = await client.purge_from(discord.Object(id='%s' % ChannelID), limit=xin, check=is_me)
    await client.send_message(discord.Object(id='%s' % ChannelID),'Deleted {} Message(s)'.format(len(deleted)))

@client.command()
async def enc(key:str,word:str):
    """Encrypts A Word"""
    return await client.say(encrypt(key,word))

@client.command()
async def massenc(key:str,word:str):
    """Sooper strong encryption"""
    enc1 = encrypt(key,word)
    enc2 = encrypt(key,enc1)
    enc3 = encrypt(key,enc2)
    return await client.say(encrypt(key,enc3))

@client.command()
async def massdec(key:str,encryptedword:str):
    """Sooper strong decryption"""
    dec1 = decrypt(key,encryptedword)
    dec2 = decrypt(key,dec1)
    dec3 = decrypt(key,dec2)
    return await client.say(decrypt(key,dec3))

@client.command()
async def dec(key:str,encryptedword:str):
    """Decrypts Encrypted Text"""
    return await client.say(decrypt(key,encryptedword))


@client.command(description='Choice System')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await client.say(random.choice(choices))


@client.command()
async def hello(*args):
    """says hello"""
    return await client.say("Hello! My name is Djinn. use the ';' prefix to command me!")

@client.command()
async def say(*left: str):
    """say something (I'm giving up on you)"""
    return await client.say("%s" % left)

@client.command()
async def harpoonish(*left: str):
    """HARPOONISHMENT"""
    async def aaa():
        ex = 0
        while ex <= 100:
            return await client.say("https://raw.githubusercontent.com/active9/harpoon/master/files/default.png %s" % left)
            await client.sleep[1]
            x + 1
            return aaa()

    await aaa()



@client.command()
@commands.has_permissions(manage_roles = True)
async def setroles(rooles : id):
    return await client.replace_roles(client.user,discord.Role.id(rooles))

@client.command()
async def pyx(*args):
        """Gives a Pretend You're Xzyzzy Link"""
        return await client.say('http://pyx-2.pretendyoure.xyz/zy/game.jsp#game=%s' % random.randint(0,50))

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(mem: discord.Member):
    """ kick a member """
    await client.kick(mem)
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(mem: discord.Member):
    """ ban a member """
    await client.ban(mem)



client.run("TOKEN HERE")

