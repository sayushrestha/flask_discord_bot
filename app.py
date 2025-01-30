import asyncio
import discord
from discord.ext import commands
from fastapi import FastAPI

app = FastAPI()
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@app.get("/")
async def hello_world():
    return {"hello": "world"}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} running together with FastAPI!")

@bot.command()
async def welcome(ctx: commands.Context, member: discord.Member):
    await ctx.send(f"Welcome to {ctx.guild.name}, {member.mention}!")

async def run():
    try:
        await bot.start("API_KEY_HERE")
    except KeyboardInterrupt:
        await bot.logout()

asyncio.create_task(run())
