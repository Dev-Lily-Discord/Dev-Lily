import discord, discord.ext, glob, os
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	print(f"Logged in as {client.user}")


######################################################################
# Load commands (DONT TOUCH)
files = glob.glob("commands/*")
done = []
for file in files:
	if file not in done:
		if file.endswith(".py"):
			file_to_load = file.replace(".py", "").replace("\\", "/").replace("/", ".")
			print(f"Loading {file_to_load}")
			client.load_extension(file_to_load)
			done.append(file)
		elif not file.endswith(".pyc"):
			files2 = glob.glob(file+"/*")
			for file in files2:
				files.append(file)
		else:
			done.append(file)

######################################################################

# client.run(os.getenv("TOKEN"))