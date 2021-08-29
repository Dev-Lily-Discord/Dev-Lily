import discord
from discord.ext import commands

@commands.command()
async def ping(ctx):
	await ctx.send('Pong! {0}ms'.format(client.latency))


def setup(client):
	client.add_command(ping)