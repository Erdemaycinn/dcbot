import discord
import os
import io
import time 
import random
from discord.ext import commands
import asyncio


intents = discord.Intents.all()
Bot = commands.Bot(command_prefix= "!", intents=intents)

# Son harfi yazdıran fonksiyon

def lastchars(word,id):
    
        
        f = open(f"servers\\server_{id}\\lastchar.txt","w",encoding="utf-8")
        f.write(word[-1])
        f.close()
    
# Kullanıcıya puan ekleyen fonksiyon    
        
def pointadd(userid,symbol): 
    try:
        user = open(f"users\\user_{userid}\\userpoints.txt","a",encoding="utf-8")
        user.write(symbol)
        user.close()
    except: 
        try:
            user = open(f"users\\user_{userid}\\userpoints.txt","w",encoding="utf-8")
            user.write("")
            user.close()
            user = open(f"users\\user_{userid}\\userpoints.txt","a",encoding="utf-8")
            user.write(symbol)
            user.close()
        except:
            os.mkdir(f"users\\user_{userid}")
            user = open(f"users\\user_{userid}\\userpoints.txt","w",encoding="utf-8")
            user.write("")
            user.close()
            user = open(f"users\\user_{userid}\\userpoints.txt","a",encoding="utf-8")
            user.write(symbol)
            user.close()    
            
# Puanları hesaplayan fonksiyon            
               
def getpoints(userid):
    try:
        user = open(f"users\\user_{userid}\\userpoints.txt","r",encoding="utf-8")
        
    except: 
        try:
            user = open(f"users\\user_{userid}\\userpoints.txt","w",encoding="utf-8")
            user.write("")
            user.close()
            user = open(f"users\\user_{userid}\\userpoints.txt","r",encoding="utf-8")
            
        except:
            os.mkdir(f"users\\user_{userid}")
            user = open(f"users\\user_{userid}\\userpoints.txt","w",encoding="utf-8")
            user.write("")
            user.close()
            user = open(f"users\\user_{userid}\\userpoints.txt","r")
    data = user.read()       
    short   = data.count("1")       
    normal  = data.count("2") 
    long_   = data.count("3") 
    gamef   = data.count("-") 
    star    = data.count("s") 
    topword = star + short + normal + long_ + gamef  
    points  = (short*10) + (normal*15) + (long_*20) + (gamef * 20) + (star*100)   
         
    #short          =   1
    #normal         =   2
    #long           =   3
    #solong         =   4
    #gamefinisher   =   -
    #star           =   s
    user.close()  
    return short, normal, long_, topword, gamef, star, points    

# Kullanıcının seçtiği tepkiyi getiren fonksiyon
            
def getreact(userid):
    try:
        userfile = open(f"users\\user_{userid}\\reaction.txt","r",encoding="utf-8")
        tepki = userfile.read()  
        userfile.close()
        
    except:
        try:
            
            userfile = open(f"users\\user_{userid}\\reaction.txt","w",encoding="utf-8")
            userfile.write("✅") 
            tepki= "✅" 
            userfile.close()    
            
            
            
        except:    
            os.mkdir(f"users\\user_{userid}")
            userfile = open(f"users\\user_{userid}\\reaction.txt","w",encoding="utf-8")
            userfile.write("✅")  
            tepki = "✅"
            userfile.close()    
    return tepki        

# Kullanıcının seçtiği tepkiyi değiştiren fonksiyon

def changereact(userid,react):
    try:
        userfile = open(f"users\\user_{userid}\\reaction.txt","w",encoding="utf-8")
        userfile.write(react)  
        userfile.close()
    except:
        os.mkdir(f"users\\user_{userid}")
        userfile = open(f"users\\user_{userid}\\reaction.txt","w",encoding="utf-8")
        userfile.write(react)  
        userfile.close()
                              
# Yıldızlı kelimeleri çeken fonksiyon                              
                              
def getstarlist():
    f = open("starlist.txt", "r",encoding="utf-8")
    starlisttxt = f.readlines()
    return starlisttxt
    
# Yıldızlı kelimeleri yazdıran fonksiyon 
            
def writestarlist(txt):
    f = open("starlist.txt", "w",encoding="utf-8")
    for x in txt:
        f.write(x)
                
# Harfleri hafızaya kaydeden fonksiyon    
            
def memory(word,id):
    f = open(f"servers\\server_{id}\\memory.txt","a",encoding="utf-8")
    f.write(word+"\n")
    f.close()
    f = open(f"servers\\server_{id}\\memory.txt","r",encoding="utf-8")
    if len(f.readlines()) > 200:
        f.close()
        f = open(f"servers\\server_{id}\\memory.txt","w",encoding="utf-8")
        f.write("filler\n")
        f.close()
        return True
    else: 
        return False

# Harf bulunamadığında yeni bir harf oluşturacak fonksiyon

def newletter(id):
    alp = ["a", "b", "c", "ç", "d", "e", "f", "g", "h", "i", "ı", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
    f = open(f"servers\\server_{id}\\lastchar.txt","w",encoding="utf-8")
    randomletter = random.choice(alp)
    f.write(randomletter)
    return randomletter
    
# Kullanıcı idlerini not eden foksiyon
    
def usermem(serverid,id = ""):
        
        f = open(f"servers\\server_{serverid}\\usermem.txt","w",encoding="utf-8")
        f.write(f"{id}")
        f.close()
        
                    
# Bot aktif olunca bunları yapar
  
@Bot.event
async def on_ready():
        
    print("Bot aktif")
    f = open("category.txt","r",encoding="utf-8")
    text =f.read()
    f.close()
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Haftanın kategorisi :{text}"))
   

# Haftalık kategori girdisi için command

@Bot.command()
async def haftalıkkategori(ctx,category,*,txt):
    permid = [ 417661630969544734,278545515178622976]
    if ctx.author.id in permid:
        await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Haftanın kategorisi :{category}"))
        f = open("category.txt","w",encoding="utf-8")
        f.write(category)
        f.close()
        txtafterprocess = []
        txtlist = txt.split()
        f = open("starlist.txt","w",encoding="utf-8")
        f.write("")
        f.close() 
        for x in txtlist:
            x = x+"\n"
            txtafterprocess.append(x)
        f = open("starlist.txt","a",encoding="utf-8")
        writestarlist(txtafterprocess)
        f.close()  
        await ctx.channel.send("Kategori başarıyla değiştirilir")  
    
    
# Botun yeni sunuculardaki kurulumu için command

@Bot.command()
@commands.has_guild_permissions(ban_members = True)
async def kurulum(ctx):
    try:
        f = open(f"servers\\server_{ctx.guild.id}\\lastchar.txt","r",encoding="utf-8") # Son harf verisi içeren dosya açılır
        lastchar = f.read() # Son harf veriye atanır
        f.close() # Dosya kapatılır
    except:
        try:
            f=open(f"servers\\server_{ctx.guild.id}\\lastchar.txt","w",encoding="utf-8")
            lastchar = newletter(ctx.guild.id)
            f.close()
            
        except:
            os.mkdir(f"servers\\server_{ctx.guild.id}") 
            f=open(f"servers\\server_{ctx.guild.id}\\lastchar.txt","w",encoding="utf-8")
            lastchar = newletter(ctx.guild.id)
            f.close()
                    
    
    try: 
        f = open(f"servers\\server_{ctx.guild.id}\\channel.txt","w",encoding="utf-8")
        f.write(f"{ctx.channel.id}")
        f.close()
        await ctx.send(f"Kanal ayarlandı! harfimiz ``{lastchar}``")        
    except:
        os.mkdir(f"servers\\server_{ctx.guild.id}") 
        f = open(f"servers\\server_{ctx.guild.id}\\channel.txt","w",encoding="utf-8")
        f.write(f"{ctx.channel.id}") 
        f.close()
        await ctx.send(f"Kanal ayarlandı! harfimiz ``{lastchars}``")

# Komutların ne işe yaradığını gösteren bir komut
          
@Bot.command()
async def yardım(ctx):
    await ctx.channel.send("Kurulum komutu : ``!kurulum``\nProfil komutu : ``!profil``\nTepki ayarları ``!tepki``\n Puan sistemi : ``!puansistemi``")

# Puan sistemini yazdıran bir komut

@Bot.command() 
async def puansistemi(ctx):
    await ctx.channel.send("***Puan sistemi sizin yazdığınız kelimelerin özelliklerne göre puan verir, bunlar arasında;***\n\n**-Kelime uzunluğu (kısa = 10, orta = 15, uzun = 25)**\n**-Son harfin 'ğ' olması (ek 20 puan)**\n**-Yıldızlı kelime (ek 100 puan)**\n\n*Yıldızlı kelime listesi her hafta belirlenir ve botun durumunda temanın ne olduğu bellidir, yıldızlı bir kelimeyi tekrar yazmak ek puan kazandırmaz*")   

# Ana oyun döngüsü

@Bot.listen()
async def on_message(ctx):
 botid = 1096413201199018004   
 f = open(f"servers\\server_{ctx.guild.id}\\channel.txt","r",encoding="utf-8")
 channel1 = f.read()
 f.close
 if f"{ctx.channel.id}" == channel1 and not ctx.author.id ==botid:
    
    word = f"{ctx.content}" # Kelime değişkene çevirilir
    memberid = ctx.author.id
    word_afterprocess = word.replace("I","ı").lower().replace("i̇","i")
    
    wordf = word_afterprocess[0] # Kelimenin ilk harfi alınır
    try:
        f = open(f"servers\\server_{ctx.guild.id}\\usermem.txt","r",encoding="utf-8")
        userx = f.read()
        f.close()
    except:
        f = open(f"servers\\server_{ctx.guild.id}\\usermem.txt","w",encoding="utf-8")
        userx = "any"
        f.close()     
    
    if wordf == "ı":
        wordfirst = "I"
    elif wordf == "i":
        wordfirst = "İ"    
        
    else:   
        wordfirst = wordf.upper()    
    
    
    try:
        f = open(f"servers\\server_{ctx.guild.id}\\lastchar.txt","r",encoding="utf-8") # Son harf verisi içeren dosya açılır
        lastchar = f.read() # Son harf veriye atanır
        f.close() # Dosya kapatılır
    except:
        f=open(f"servers\\server_{ctx.guild.id}\\lastchar.txt","w",encoding="utf-8")
        lastchar = newletter(ctx.guild.id)
        f.close()
    try:
        f = open(f"servers\\server_{ctx.guild.id}\\memory.txt","r",encoding="utf-8")
        words = f.readlines()
        f.close()
    except:
        f = open(f"servers\\server_{ctx.guild.id}\\memory.txt","w",encoding="utf-8")
        f.write("Filler\n")
        f.close()
        f = open(f"servers\\server_{ctx.guild.id}\\memory.txt","r",encoding="utf-8")
        words = f.readlines()
        f.close()
        
    outloop = False
    delmsg = True    
    
    if word_afterprocess[0] == ".":
        delmsg = False
        
    else:    
    
     if f"{ctx.author.id}" == userx:
        await ctx.channel.send(f"Aynı kişi üst üste mesaj atamaz, harf: {lastchar}", delete_after = 3.5)
     else:
        if wordf == lastchar:
        
        
        
            sayı = 0
            for y in words:
                
                
                sayı += 1
                 
                
                y = y[0:-1]
                
            
                if word_afterprocess == y:
                    await ctx.channel.send(f"``{word_afterprocess}`` kelimesi bu oyuda zaten kullanılmış, harf: {lastchar}", delete_after = 3.5)
                    outloop = True
                    break
                
                elif sayı == len(words) or len(words) == 0:
                    
                    asyı = 0
                    f = open(f"{wordfirst}.txt","r",encoding="utf-8") # Kelimenin ilk harfi alınarak Harf dosyası açılır
                    wordlist = f.readlines() # Harf dosyası içindeki veriler harf listesine çevirilir
                    f.close() # Dosya kapatılır
                    
                    for x in wordlist: # Dosya verileri x e atanır
                        asyı +=1
                        
                        x = x[0:-1]
                        

                        if x == word_afterprocess and outloop == False:
                           
                            await ctx.add_reaction(getreact(ctx.author.id)) # Onay geri bildirimi
                            
                            if len(word_afterprocess)  < 4:      # short
                                pointadd(ctx.author.id,"1")
                            elif len(word_afterprocess) < 7:    # normal
                                pointadd(ctx.author.id,"2")
                            elif len(word_afterprocess) < 10:   # long_
                                pointadd(ctx.author.id,"3") 
                            else:   # solong
                                pointadd(ctx.author.id,"4")    
                                        
                            
                            starlistwoutn = getstarlist()
                            
                            for starword in starlistwoutn:
                                
                                starword = starword[0:-1]
                                if word == starword:
                                    await ctx.add_reaction("🌟")
                                    pointadd(ctx.author.id,"-")
                                    starlistwoutn.remove(starword + "\n")
                                    
                                    writestarlist(starlistwoutn)
                            
                            
                            
                            if word_afterprocess[-1] == "ğ":
                                await ctx.channel.send(f"'Ğ' harfiyle cümle kurulduğundan emin değilim, yeni harfimiz: ``{newletter(ctx.guild.id)}``  ")
                                pointadd(ctx.author.id,"s")
                            
                            else:
                                lastchars(word_afterprocess,ctx.guild.id)
                            delmsg = False
                            
                            usermem(ctx.guild.id,memberid)
                            if memory(word_afterprocess,ctx.guild.id) == True:
                                await ctx.channel.send(f"Oyun yeniden kuruluyor, yeni harfimiz: ``{ newletter(ctx.guild.id) }`` ", )
                            break
                        elif asyı == len(wordlist):
                            await ctx.channel.send(f"``{word_afterprocess}`` kelimesi veritabanımda bulunmuyor, harf: {lastchar}", delete_after = 3.5)
                        
                              
                    # For var
                        
                 
            # For var         
        else:
            await ctx.channel.send(f"Ciddenmi? Son harfle yazacaksın! harf: {lastchar}", delete_after = 3.5)
        
    if delmsg == True:
        await ctx.delete()

# Kullanıcı profilini yazdıran bir komut

@Bot.command()
async def profil(ctx, member: discord.Member = ""):
    if member == "":
        member = ctx.message.author
    
    
    pointlist = tuple(getpoints(member.id))
    
    
    embed = discord.Embed(title=f"Profil bilgileri\nSeçili tepki: '{getreact(member.id)}'",colour=0x2ecc71)
    embed.add_field(name="Kısa\nkelime:",value=pointlist[0],inline=True)
    embed.add_field(name="Orta\nkelime:",value=pointlist[1],inline=True)
    embed.add_field(name="Uzun\nkelime:",value=pointlist[2],inline=True)
    
    embed.add_field(name="Oyun bitiren kelime:",value=pointlist[3],inline=False)
    embed.add_field(name="Yıldızlı kelime:",value=pointlist[4],inline=False)
    embed.add_field(name="Toplam puan:",value=pointlist[6],inline=True)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text="Lügat Bot")
    embed.set_author(name= f"{member.display_name}")    
    await ctx.channel.send(embed= embed)


# Tepki ayarlamaları için kullanılan komut        
            
@Bot.command()
async def tepki(ctx, tepki = ""):
    pointlist = getpoints(ctx.message.author.id)
    if pointlist[5] <50:
            await ctx.channel.send("**Mesaj tepkisini değiştirmek için 50 kelime kullanmış olmanız gereklidir ⛔**",delete_after = 3.5 )
    elif tepki == "":
        
        embedfun = discord.Embed(title=f'***Sayfa 1/2***\n***Eğlence Tepkileri***',description='\n***``12``  -  "Ğ" Ustası (:disguised_face:) ***\n``100. "ğ" ile biten kelimeni yazıldığında açılır``\n\n***``13`` - Yıldız (:star2:) *** \n``20. Yıldızlı kelimeyi yazıldığında açılır``\n\n***``14`` - Orta şeker (:coffee: ) *** \n``123. Orta uzunlukta kelimeyi kullanıldığında açılır``\n ',colour=0x2ecc71)
        embedrank = discord.Embed(title=f"***Sayfa 2/2***\n***Seviye Tepkileri***",description='***``21`` - Amatör (:third_place:)  ***\n``1000 puanda açılır``\n\n***``22`` - Tecrübeli (:second_place:) ***  \n``10000 puanda açılır``\n\n***``23`` - Profesyonel (:first_place: ) ***  \n``25000 puanda açılır``\n\n***``24`` - Kelime dehası (:beginner: ) ***  \n``50000 puanda açılır``\n\n***``25`` - Zırdeli (:trident: ) ***  \n``100000 puanda açılır``\n',colour=0x2ecc71)
        
        contents = [embedfun, embedrank]
        pages = 2
        cur_page = 1
        message = await ctx.send(embed = contents[cur_page-1])
    

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
            # This makes sure nobody except the command sender can interact with the "menu"

        while True:
            try:
                reaction, user = await Bot.wait_for("reaction_add", timeout=60, check=check)
                # waiting for a reaction to be added - times out after x seconds, 60 in this
                # example

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed = contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)
                    # removes reactions if the user tries to go forward on the last page or
                    # backwards on the first page
            except asyncio.TimeoutError:
                await message.delete()
                break
                # ending the loop if user doesn't react after x seconds     
    elif   tepki == "21":
        if pointlist[6]>1999:
            await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
            changereact(ctx.message.author.id, "🥉")
        else:    
            await ctx.channel.send("Yeterli puana sahip değilsiniz")  
    elif  tepki == "22":
        if pointlist[6]>9999:
            await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
            changereact(ctx.message.author.id, "🥈")  
        else:    
            await ctx.channel.send("Yeterli puana sahip değilsiniz")    
    elif  tepki == "23":
        if pointlist[6]>24999:
            await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
            changereact(ctx.message.author.id, "🥇") 
        else:
            await ctx.channel.send("Yeterli puana sahip değilsiniz")   
    elif  tepki == "24":
        if pointlist[6]>49999:
            await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
            changereact(ctx.message.author.id, "🔰") 
        else:
            await ctx.channel.send("Yeterli puana sahip değilsiniz")   
    elif tepki == "25":
        if pointlist[6]>99999:
            await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
            changereact(ctx.message.author.id, "🔱") 
        else:     
            await ctx.channel.send("Yeterli puana sahip değilsiniz")  
     
    elif  tepki == "12":
        if pointlist[4]>99 :
            await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
            changereact(ctx.message.author.id, "🥸") 
        else:
            await ctx.channel.send("Yeterli puana sahip değilsiniz")   
    elif  tepki == "13":
        if pointlist[5]>19:
            await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
            changereact(ctx.message.author.id, "🌟") 
        else:
            await ctx.channel.send("Yeterli puana sahip değilsiniz")    
    elif  tepki == "14":
        if pointlist[1]>122:
            await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
            changereact(ctx.message.author.id, "☕")
        else:
            await ctx.channel.send("Yeterli puana sahip değilsiniz")
    elif tepki == "00":
        await ctx.channel.send("Tepkiniz başarıyla değiştirildi")
        changereact(ctx.message.author.id, "✅")           

Bot.run("MTA5NjQxMzIwMTE5OTAxODAwNA.GSXMoJ.p_O-Fhqfoao9mFmHBG-NttJacbENV_xnwychao")