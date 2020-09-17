import discord
import asyncio
import pymysql
import datetime
from datetime import timedelta
import random
from discord.ext import commands, tasks
from collections import Counter
import joybot_private

bot = commands.Bot(command_prefix='$')

token = joybot_private.token
happyhost = joybot_private.happyhost
dbpsw = joybot_private.dbpsw

client =  discord.Client()
@bot.event
async def on_ready():
    print("================")
    print(bot.user.name)
    print(bot.user.id)
    print("================")

@bot.command(name="가위바위보")
async def hey(ctx, arg):
    handlist = [1,2,3] #1 : 가위 2: 주먹 3:보
    
    bot_hand = random.choice(handlist)
    if arg == "찌" :
        
        if bot_hand == 1 :
            await ctx.send("찌!")
            await ctx.send(ctx.author.name + "님과 비겼습니다.")
        if bot_hand == 2 :
            await ctx.send("묵!")
            await ctx.send(ctx.author.name + "님에게 승리하였습니다.")
        if bot_hand ==  3 :
            await ctx.send("빠!") 
            await ctx.send(ctx.author.name + "님에게 패배하였습니다.")
    elif arg == "묵" :
        
        if bot_hand == 1 :
            await ctx.send("찌!")
            await ctx.send(ctx.author.name + "님에게 패배하였습니다.")
        if bot_hand == 2 :
            await ctx.send("묵!")
            await ctx.send(ctx.author.name + "님과 비겼습니다.")
        if bot_hand ==  3 :
            await ctx.send("빠!") 
            await ctx.send(ctx.author.name + "님에게 승리하였습니다.")
    
    elif arg == "빠" :
        
        if bot_hand == 1 :
            await ctx.send("찌!")
            await ctx.send(ctx.author.name + "님에게 승리하였습니다.")
        if bot_hand == 2 :
            await ctx.send("묵!")
            await ctx.send(ctx.author.name + "님에게 패배하였습니다.")
        if bot_hand ==  3 :
            await ctx.send("빠!") 
            await ctx.send(ctx.author.name + "님과 비겼습니다.")
    else :
        await ctx.send("묵 찌 빠 중에서 입력해 주세요")

@bot.command(name="삭제")
async def cmd_delete(ctx) :
    conn = pymysql.connect(happyhost, user='TT', password=dbpsw, db='Happy' ,charset = 'utf8')
    try:
        curs = conn.cursor()
        sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'Happy'"
        curs.execute(sql)
        guild_cmd_table_id = str(curs.fetchall())
        conn.commit() 
    finally:
        conn.close()

    await ctx.send("명령어를 입력해 주세요.")
    
    def delete_check(m) :
        return m.content and m.author == ctx.author

    del_cmd = await bot.wait_for('message', check=delete_check)
    db_del_cmd = str("{.message}".format(del_cmd))
    try:
        guild_table_id = str(ctx.guild.id)
        if guild_table_id in guild_cmd_table_id :
            db_table_name = str("a_"+guild_table_id)

        qwer = pymysql.connect(happyhost, user='TT', password=dbpsw,db='Happy' ,charset = 'utf8')
        try:
            cursor = qwer.cursor(pymysql.cursors.DictCursor)
            sql1 = "select * from "+db_table_name+""
            cursor.execute(sql1)
            result = cursor.fetchall()
        finally:
            qwer.close()
        
        for i in result :
            if ctx.content == i.get('cmd')  :
                
                conn = pymysql.connect(happyhost, user='TT', password=dbpsw,db='Happy' ,charset = 'utf8')
                curs = conn.cursor()
                sql = "delete from "+db_table_name+" where cmd = '"+db_del_cmd+"'"
                curs.execute(sql)
                conn.commit()
                conn.close()
                await ctx.send(db_del_cmd + "명령어가 삭제되었습니다.")
                break

    except AttributeError:
        pass

@bot.command(name="역할확인")
async def role_check(ctx, *, role : discord.role) :
    roles = await ctx.id
    print(roles)

@bot.command(name="추가")
async def cmd_add(ctx) :
    conn = pymysql.connect(happyhost, user='TT', password=dbpsw, db='Happy' ,charset = 'utf8')
    try:
        curs = conn.cursor()
        sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'Happy'"
        curs.execute(sql)
        guild_cmd_table_id = str(curs.fetchall())
        conn.commit() 
    finally:
        conn.close()
    
    try :
        guild_table_id = str(ctx.guild.id)
        if guild_table_id in guild_cmd_table_id :
            db_table_name = str("a_"+guild_table_id)
            await ctx.send("명령어를 입력해 주세요")
            
            def cmd_check(m):
                return m.content and  m.author == ctx.author

            guild_cmd = await bot.wait_for('message', check=cmd_check)
            str_guild_cmd = str("{.content}".format(guild_cmd))
            
            await ctx.send("컨텐츠를 입력해 주세요")
            
            def content_check(m):
                return m.content and m.author == ctx.author
            
            guild_content = await  bot.wait_for('message', check=content_check)
            str_guild_content =  str("{.content}".format(guild_content))

            conn = pymysql.connect(happyhost, user='TT', password=dbpsw,db='Happy' ,charset = 'utf8')
            curs = conn.cursor()
            sql = "INSERT into "+db_table_name+"(cmd, emoji) value (%s, %s)"
            curs.execute(sql, (str_guild_cmd, str_guild_content))
            conn.commit()
            conn.close()

            await ctx.send(str_guild_cmd+"가 추가되었습니다.")
    except AttributeError :
        pass 

@bot.command(name="명령어확인")
async def cmd_list(ctx) :
    print("qwer")
    conn = pymysql.connect(happyhost, user='TT', password=dbpsw, db='Happy' ,charset = 'utf8')
    try:
        curs = conn.cursor()
        sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'Happy'"
        curs.execute(sql)
        guild_cmd_table_id = str(curs.fetchall())
        conn.commit() 
    finally:
        conn.close()

    guild_table_id = str(ctx.guild.id)
    if guild_table_id in guild_cmd_table_id :
        db_table_name = str("a_"+guild_table_id)
        
        qwer = pymysql.connect(happyhost, user='TT', password=dbpsw,db='Happy' ,charset = 'utf8')
        try:
            cursor = qwer.cursor()
            sql1 = "select cmd from "+db_table_name+""
            cursor.execute(sql1)
            result = cursor.fetchall()
        finally:
            qwer.close()
        
        cmd_len = len(result)
        cmd_page =int(cmd_len // 10)
        page = []
        print(cmd_page)
        if cmd_page > 1 :
            i = 0
            while(i<cmd_page):
                page.append(result[i:i*10])
                i += 1
        else :
            page.append(result)

        cmd_list_embed = discord.Embed()
        cmd_list_embed.add_field(name="명령어 목록", value=page[0]) 
        qwer = await ctx.send(embed=  cmd_list_embed)

        def reaction_check(reaction) :
            return reaction.emoji
        
        check_reaction = await bot.wait_for('reaction', check=reaction_check)
        emoji = str("{emoji}".format(check_reaction))
        for i in page :
            if emoji == '👍' :
                cmd_list_embed_page = discord.Embed()
                cmd_list_embed_page.add_field(name="명령어 목록", value=i)
                await qwer.edit(embed = cmd_list_embed_page)
        
async def um_message(message) :
    if message.author.bot :
        return None

    conn = pymysql.connect(happyhost, user='TT', password=dbpsw, db='Happy' ,charset = 'utf8')
    try:
        curs = conn.cursor()
        sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'Happy'"
        curs.execute(sql)
        guild_cmd_table_id = str(curs.fetchall())
        conn.commit() 
    finally:
        conn.close()

    guild_table_id = str(message.guild.id)
    if guild_table_id in guild_cmd_table_id :
        db_table_name = str("a_"+guild_table_id)

        qwer = pymysql.connect(happyhost, user='TT', password=dbpsw,db='Happy' ,charset = 'utf8')
        try:
            cursor = qwer.cursor(pymysql.cursors.DictCursor)
            sql1 = "select * from "+db_table_name+""
            cursor.execute(sql1)
            result = cursor.fetchall()
        finally:
            qwer.close()
        
        for i in result :
            if message.content == i.get('cmd') :
                guild_emoji = i.get('emoji')
                if 'https' in guild_emoji :
                    embed = discord.Embed()
                    embed.set_image(url=guild_emoji)
                    await message.channel.send(embed)
                    break
                
                if 'http' in guild_emoji  :
                    embed = discord.Embed()
                    embed.set_image(url=guild_emoji)
                    await message.channel.send(embed)
                    break
                await message.channel.send(guild_emoji)

bot.add_listener(um_message,'on_message')
    

bot.run(token)