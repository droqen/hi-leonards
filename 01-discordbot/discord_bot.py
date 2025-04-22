import discord
from discord.ext import commands
import time
import asyncio
from secret import BOT_TOKEN

# Set up the bot with command prefix '!'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now online!')

@bot.command(name='leonard')
async def leonard(ctx, *args):
    """Makes Leonard speak with natural pauses"""
    # Default lines if no arguments are provided
    lines = [
        "LEONARD: Hello, World!",
        "LEONARD: Imagine, with the power of empathy, that I'm a living thing."
    ]
    
    # If arguments are provided, join them to create a custom message
    if args:
        lines = [f"LEONARD: {' '.join(args)}"]
    
    message = await ctx.send("_Leonard is typing..._")
    
    for line in lines:
        words = line.split(" ")
        full_text = ""
        
        for word in words:
            full_text += word
            await message.edit(content=full_text)
            
            # Add pauses based on punctuation
            if any(word.endswith(char) for char in [".", "!", "?"]):
                await asyncio.sleep(0.5)
            elif any(word.endswith(char) for char in [",", ":", ";"]):
                await asyncio.sleep(0.2)
            
            await asyncio.sleep(0.1)
            full_text += " "  # Add space after each word
            
        await asyncio.sleep(1)  # Pause between lines
        
        if len(lines) > 1:
            await message.edit(content=full_text)
            await ctx.send("_Leonard is typing..._")

bot.run(BOT_TOKEN)