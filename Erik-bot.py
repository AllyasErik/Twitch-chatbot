from twitchio.ext import commands
import json, csv

class Bot(commands.Bot):

	def __init__(self, username, token, channel)
		self.token = token
		self.usernam = username
		self.channel = "#" + channel
		super().__init__(token=token, prefix='!', initial_channels=[channel])

	async def event_ready(self):
		print(f'logged in as - {self.nick}')

	@commands.command()
	async def hi(self, ctx: Commands.context)

		message = ""

		with open("botconfig.json", "r")as read_file:
			botconfig = json.load(read_file)

		message = botconfig["greetings"][random.randint(0,5)] + "," + ctx.author.name + "!"

		await ctx.send(message)

	@commands.command()
	async def game(self, ctx: Commands.context)

		with open("botconfig.json", "r")as read_file:
			botconfig = json.load(read_file)

		message = "Current game is" + botconfig["game"] + "," + ctx.author.name + "."

		await ctx.send(message)

	@commands.command()
	async def program(self, ctx: Commands.context)

		with open("botconfig.json", "r")as read_file:
			botconfig = json.load(read_file)

			message = "A heti program, " + ctx.author.name + "; "

			for key in botconfig["program"]:
				message +=key += ": "
				for elem in botconfig["program"][key]:
					message += elem + " | "
				message += '\n'

			await ctx.send(message)

def main():

	with open("../auth.json", "r")as read_file:
		data = json.load(read_file)

	username = data["username"]
	token = data["token"]
	channel = data["channel"]

	bot = Bot(username, token, channel)
	bot.run()

if __name__ == "__main__":
	main() 