import discord
import os
import asyncio
import youtube_dl
import time


# Bot Initialization

token = 'YOUR TOKEN'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
queue = []

voice_clients = {}
songs = []

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': '-vn'}

#Moderation things
block_words = ["http://", "https://"]
allowed_links = ["https://youtube", "https://youtu.be"]


#BOT events 
@client.event
async def on_ready():
    print(f'Bot loggeid in as {client.user}')

async def play_queue:
    try: 
        voice_client = await msg.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except Exception as err:
            print(err)
@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.lower().startswith('?hi'):
            await msg.channel.send(f'Hi, {msg.author.display_name}')
    
    if msg.content.startswith(".play"):
        queue.append(msg.content.split()[1])
        

        try: 
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except Exception as err:
            print(err)

        try:
            url = msg.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C:\\Users\\lucas\\Downloads\\ffmpeg\\bin\\ffmpeg.exe")
            voice_clients[msg.guild.id].play(player)
            await msg.channel.send(f'Playing now: {ytdl.extract} \nRequested by: {msg.author.display_name}')

        except Exception as err:
            print(err)

        except Exception as err:
            print(err)

    if msg.content.startswith(".pause"):
        try:
            if voice_clients[msg.guild.id].is_playing:
                voice_clients[msg.guild.id].pause()
            else:
                await msg.channel.send(f"{msg.author.display_name}, there's no songs playing now!")

            
        except Exception as err:
            print(err)

    if msg.content.startswith(".resume"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)

    if msg.content.startswith(".stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)
    time.sleep

    



client.run(token)