import discord
from discord.ext import commands
from PIL import Image
import io

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if bot is mentioned and a PNG is attached
    if bot.user in message.mentions and message.attachments:
        for attachment in message.attachments:
            if attachment.filename.lower().endswith('.png'):
                image_bytes = await attachment.read()
                
                # Convert PNG to GIF using PIL
                img = Image.open(io.BytesIO(image_bytes))
                gif_bytes = io.BytesIO()
                img.save(gif_bytes, format='GIF')
                gif_bytes.seek(0)

                # Send the GIF back
                await message.channel.send(file=discord.File(fp=gif_bytes, filename='converted.gif'))

bot.run('MTM3NTE5MDQwMTY2OTEzNjQwNA.Gu-jVY.DMJ-sMx3axFP0DAPlEN5h5F8HDfuu5TIXF_jVI')
