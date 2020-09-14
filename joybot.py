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



@bot.command(name="역할확인")
async def role_check(ctx, *, role : discord.role) :
    roles = await ctx.id
    print(roles)

@bot.command(name="추가")
async def cmd_add(ctx, arg) :
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

            guild_cmd = await bot.wait_for('arg', check=cmd_check)
            str_guild_cmd = str("{arg}".format(guild_cmd))
            
            await ctx.send("컨텐츠를 입력해 주세요")
            
            def content_check(m):
                return m.content and m.author == ctx.author
            
            guild_content = await  bot.wait_for('arg', check=content_check)
            str_guild_content =  str("{arg}".format(guild_content))

            conn = pymysql.connect(happyhost, user='TT', password=dbpsw,db='Happy' ,charset = 'utf8')
            curs = conn.cursor()
            sql = "INSERT into "+db_table_name+"(cmd, emoji) value (%s, %s)"
            curs.execute(sql, (str_guild_cmd, str_guild_content))
            conn.commit()
            conn.close()


    except AttributeError :
        pass 



bot.run(token)