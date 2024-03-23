#봇 관련 프로그램

import discord
import datetime
from discord import message
from discord.flags import MessageFlags
import openpyxl
import os







client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("(dangdangi ver:1.9.5): ready")
    print("apry_dangdangi_xms128m_xmx16G")
    game = discord.Game("dangdangi 1.9.5v")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    #채팅 명령어
    if message.content.startswith("/명령어"):
        await message.channel.send("(명령어 앞에 접두사는 /입니다.) 명령어, vt(투표), 정보, 핑, 시스템관리자")

    if message.content == "/핑":
        la = client.latency
        await message.channel.send(f'`{str(round(la * 1000))}ms`입니다.')

    if message.content.startswith("안녕"):
        await message.channel.send("하이")
    
    if message.content.startswith("/vt"):
        vote = message.content[4:].split("/")
        await message.channel.send("@everyone" + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('✅')

    if message.content.startswith("/정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(colour=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("댕댕아"):
         await message.channel.send("뭐")
    
    if message.content.startswith("나랑 놀자"):
         await message.channel.send("싫은데")

    if message.content.startswith("안녕"):
        await message.channel.send("하이")



    

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
