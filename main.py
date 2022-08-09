import os
import argparse
import asyncio

########## Credits ##############################               
#    github = "https://github.com/EinWortspiel" #
#    discord = "EinWortspiel 3#9998"            #
#    dev = "EinWortspiel"                       #
########## Credits ##############################

def createCog(name:str, cmdName:str, cmdDesc:str) -> str:
    exampleCog = """import discord
from discord.ext import commands

class {}(commands.Cog):
    def __init__(self, client:commands.Bot) -> None:
        self.client:commands.Bot = client
    
    @commands.command(name="{}", description="{}")
    async def {}(self, ctx:commands.Context) -> None:
        await ctx.send("Hello World!")
    
async def setup(client:commands.Bot) -> None:
    await client.add_cog({}(client))""".format(name, cmdName, cmdDesc, cmdName, name)
    return exampleCog

async def main() -> None:
    parser = argparse.ArgumentParser(description="Discord.py 2.0+ cog generator")
    parser.add_argument("--cogName", type=str, default="Test", required=False, help="Name of the new cog")
    parser.add_argument("--cmdName", type=str, default="test", required=False, help="Name of the example command")
    parser.add_argument("--cmdDesc", type=str, default="Example cmd", required=False, help="Description of the example command")
    args = parser.parse_args()
    try:
        with open(f"{os.getcwd()}/{args.cogName}.py", "x+", encoding="UTF-8") as f:
            f.write(createCog(args.cogName, args.cmdName, args.cmdDesc))
    except FileExistsError:
        print("File already there!")
    else:
        print("Finished!")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())