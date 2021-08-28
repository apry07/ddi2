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
    
    if message.content.startswith("/패치노트"):
        await message.channel.send("dangdangi 1.1.5.v  추가된 기능, 버그 개선, 접두사 변경. ")

    if message.content.startswith("댕댕아"):
         await message.channel.send("뭐")
    
    if message.content.startswith("나랑 놀자"):
         await message.channel.send("싫은데")

    if message.content.startswith("이진"):
        await message.channel.send("국기에 대한 경례에 이어, 순국선열 및 호국영령에 대한 묵념이 있겠습니다. 일동 묵념. :flag_kr: ")

    if message.content.startswith("백현"):
        await message.channel.send("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%B1%ED%98%84")

    if message.content.startswith("하이"):
        await message.channel.send("ㅎㅇㅎㅇㅎㅇ")

    if message.content.startswith("멈춰"):
        await message.channel.send("아무도 날 막을수 없으셈!")
    
    if message.content.startswith("미친"):
        await message.channel.send("ㅇㅉ")
    
    if message.content.startswith("ㅋ"):
        await message.channel.send("뭐")

    if message.content.startswith("ㅇㅉ"):
        await message.channel.send("어쩌라고ㅗ 인간주제에")

    if message.content.startswith("ㅠ"):
        await message.channel.send("울지마 바보야")
    
    if message.content.startswith("다크손오공"):
        await message.channel.send("제-천-대-성!!!!!!")

    if message.content.startswith("사료줄까?"):
         await message.channel.send("우리 멋지고 예쁘신 주인님! 감사합니다!!❤")
    
    if message.content.startswith("엿먹어"):
         await message.channel.send("엿 너무달아~!")
    
    if message.content.startswith("응아니야"):
         await message.channel.send("네 다음 잼민이~")
    
    if message.content.startswith("어쩔"):
        await message.channel.send("에휴..할말이 그거밖에 없냐;;")

































                                   

    #욕감지 시스템

    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("욕하지마!")
    if message.content.startswith("ㅂㅅ"):
        await message.channel.send("자기소개하네")
    if message.content.startswith("개같네"):
        await message.channel.send("그건 니 인성인듯 ㅇㅇ..")
    if message.content.startswith("ㅗ"):
        await message.channel.send("욕하지마")
    if message.content.startswith("18"):
        await message.channel.send("은근슬쩍 욕하는건 아니겠지?^^")
    if message.content.startswith("ㄲㅈ"):
        await message.channel.send("시1바")

    #시스템 메시지

    if message.content.startswith("/디버그"):
        await message.channel.send("terminal.debug      877362254654353478 (dangdangi ver:1.9.5): ready apry_dangdangi_xms128m_xmx16G")
    
    if message.content.startswith("/update dangbt"):
        await message.channel.send("1.9.5v 최신버전입니다. : vsc를 참고해주세요")
    
    if message.content.startswith("안녕"):
        await message.channel.send("하이")



    

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
