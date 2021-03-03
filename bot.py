import discord
from discord.ext import commands, tasks
import os

from dlottery import Lottery


# set token (a bit ugly...)
TOKEN = ""
ftoken = 'token'
import os.path
if os.path.isfile(ftoken):
    with open(ftoken, 'r') as file:
        TOKEN = file.read()
else:
    import os
    TOKEN = os.environ["TOKEN"]

client = commands.Bot(command_prefix = '!')

# globals ):
lottery = Lottery()
hasStarted = False

@client.event
async def on_ready():
    await client.wait_until_ready()
    print ('Bot is ready.')
    print ('Setting presence...')
    await client.change_presence(status=discord.Status.idle)
    print ('Done. Waiting for commands.')

@client.command(name='add')
async def add_participant(ctx, name, amount = 1, n = 0, fee = -1):
    global hasStarted
    if not hasStarted:
        return
    lottery.addParticipant(name, int(amount), int(n), int(fee))
    tickets = str(lottery.countTickets())
    pot = str(lottery.getPot())
    await client.change_presence(activity=discord.Game('with ' + tickets + ' for ' + pot + "💰"))
    
@client.command(name='end')
async def get_winner(ctx):
    global hasStarted
    if not hasStarted:
        return
    winner, value = lottery.getWinner()
    hasStarted = False
    await ctx.send("The lottery has ended.\n**" + winner + "** won " + str(value) + "💰")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=winner + ' who won ' + str(value) + "💰"))

    
@client.command(name='start')
async def start(ctx, fee=0):
    global hasStarted
    if hasStarted:
        return
    hasStarted = True
    lottery.setEntryFee(int(fee))
    lottery.clearParticipants()
    await ctx.send("The lottery has started.")
    tickets = str(lottery.countTickets())
    pot = str(lottery.getPot())
    await client.change_presence(activity=discord.Game('with ' + tickets + ' for ' + pot + "💰"))

@client.command(name='pot')
async def getpot(ctx):
    pot = str(lottery.getPot())
    await ctx.send("The current pot is: " + pot + "💰")

# @client.command(name='setfee')
# async def setfee(ctx, fee):
    # if not hasStarted:
        # return
    # lottery.setEntryFee(int(fee))
    # fee = str(lottery.getEntryFee())
    # await ctx.send("The entry fee is now " + fee + "💰 for every ticket")
    
@client.command(name='gethelp')
async def help(ctx):
    await ctx.send("""```Help
!start <fee>
- Starts the lottery and sets the entry fee

!add <name> <amount> [<n%>] [<fee>]
- Adds a participant by name with a certain amount of tickets.
- n% will go back to the pot if the participant wins (in percent from 0 to 100)
- fee can be set to 0 to play for free

!end
- This shows the winner and the price he won. The lottery ends.

!pot
- Shows the amount that currently is in the pot

!gethelp
- Shows this message.
```""")

print ("Starting bot...")
client.run(TOKEN)
