from aiohttp import ClientSession
from Python_ARQ import ARQ

from Tianabot import *
from Tianabot.events import register

#value
ARQ_API_KEY = "QCRJIN-MJOBNZ-SPYKTN-NFZKZZ-ARQ"
ARQ_API_URL = "https://thearq.tech/"

aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

@register(pattern="^/lyrics (.*)")
async def lyrics_func(_, message):
    if len(message.command) < 2:
        await message.reply_text("**Sike That's The Wrong Command Usage!** \nUse `/lyrics` (song name)")
        return
    m = await message.reply_text("**Searching For Song Lyrics**")
    query = message.text.strip().split(None, 1)[1]
    song = await arq.lyrics(query)
    lyrics = song.result
    if len(lyrics) < 4095:
        await m.edit(f"__{lyrics}__")
        return
    lyrics = await paste(lyrics)
    await m.edit(f"**Oops! Lyrics Too Long To Send!** \n**Your Song Lyrics: [Click Here]({lyrics})**")
