import asyncio
import discord
from discord.ext import commands
import random

TOKEN = 'token'  # the account token of AVNDB

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}!')  # prints a message that shows the bot is online.
#  above code logs the bot online


@bot.command(name='random')  # random number command
async def name(ctx: commands.Context):
    response = f'this is your random number: {random.randrange(9999)}'  # random number gen 1-9999
    await ctx.reply(response)


@bot.command(name='echo')  # echo command wip
async def name(ctx, *, repeat: str):

    if ctx.author.id == 654818715183087626:
        await ctx.send(f"{repeat}")
        await ctx.message.delete()
        return

    else:
        await ctx.message.delete()
        return


@bot.command()
async def gaytest(ctx: commands.Context):  # gay test command yes/no test
    while True:  # puts the command in a while true loop, so it won't break if you enter an invalid answer.
        await ctx.reply('Are you Gay? (yes/no only)')

        try:
            message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel, timeout=30.0)  # message timeout variable

        except asyncio.TimeoutError:
            await ctx.reply('You ignored me? :(')  # if no response in 30s, break the loop and end the command
            break

        else:
            if message.content.lower() == 'yes':
                await ctx.send('BASED!!!!!!!')  # we are a little silly
                break

            elif message.content.lower() == 'no':
                await ctx.send('oh.')  # you cissie.
                break

            else:
                await ctx.send('english, motherfucker, do you speak it ? (Invalid answer, Yes/No only)')  # if invalid answer, rerun the command + add a reply


@bot.listen()
async def on_message(message):  # this code checks for messages, and if there is a message, it runs this code
    longtext1 = """Not funny. I didn't laugh. Your joke is so bad I would have preferred the joke went over my head and you gave up re-telling me the joke.
To be honest this is a horrible attempt at trying to get a laugh out of me.
Not a chuckle, not a hehe, not even a subtle burst of air out of my esophagus.
Science says before you laugh your brain preps your face muscles but I didn't even feel the slightest twitch.
0/10 this joke is so bad I can't believe anyone legally allowed you to be creative at all.
The amount of brain power you must have put into that joke has the potential to power every house on Earth.
Get a personality and learn how to make jokes, read a book.
I'm not saying this to be funny i genuinely mean it on how this is just bottom barrel embarrassment at comedy.
You've single handedly killed humor and every comedic act on the planet.
I'm so disappointed that society has failed as a whole in being able to teach you how to be funny.
Honestly if I put in all my power and time to try and make your joke funny,
and even then all that joke would get from people is a subtle scuff.
You're lucky i still have the slightest of empathy for you after telling that joke,
otherwise I would have committed every war crime in the book just to prevent you from attempting any humor ever again.
We should put that joke in text books so future generations can be wary of becoming such an absolute comedic failure.
Im disappointed, hurt, and outright offended that my precious time has been wasted in my pathetic brain understanding that joke.
In the time that took i was planning on helping kids who have been orphaned,
but because of that you've wasted my time explaining the obscene integrity of your terrible attempt at comedy.
Now those kids are suffering with out meals and there's nobody to blame but you.
I hope you're happy with what you have done."""  # I am honestly quite funny
    channels = {1015067084893458503, 979044034070843393}  # channels the bot will use specific commands
    blocked_channels = {966409881324253234, 930547097369976863}  # channels the bot will ignore
    USER_IDS = {996196570397687838, 298980849892851714}  # IDs for people you want the bot to respond to with 'shut up' messages
    NERD_EMOJI_HIM_USER_IDS = {839883479759585330, 298980849892851714}  # ids of people you want the bot to :nerd: react
    username = str(message.author)  # username variable
    user_message = str(message.content)  # user message variable
    channel = str(message.channel.name)  # channel variable
    guild = str(message.guild.name)  # server variable (guild = server)
    user_ids_print = str(message.author.id)
    print(f'{username} ({user_ids_print}): {user_message}  (posted in "#{channel}" in "{guild}")')  # when a message is sent, it enters this in the terminal.
    #  i.e "pellko!#6849: Hello. (posted in #fortnite in Fortnite Official)

    if message.author == bot.user:
        return  # ignores below code if message author is the bot

    if message.channel.id in channels:  # if channel name of a message is in the channels variable, run below code:
        if message.content.lower() == 'hello' or message.content.lower() == 'hi':   # if message = hi, hello
            await message.channel.send(f'hello, {username}!')
            return
        elif message.content.lower() == 'bye':
            await message.channel.send(f'see ya, {username}!')
            return

    if message.channel.id not in blocked_channels:
        if message.author.id in USER_IDS:
            response = [f'shut up, {username}', 'be quiet.', 'shush.', f'{longtext1}']
            await message.channel.send(random.choice(response))
        if random.randint(1, 100) <= 3:  # this is a 30% chance that the nerd emoji can be sent, this line can be deleted, or modified like 'if random.randint(1, 100) <= 5:'
            if message.author.id in NERD_EMOJI_HIM_USER_IDS:
                response = ['https://tenor.com/view/avengers-endgame-thanos-nerd-alert-opinion-nerd-gif-26272469']
                await message.channel.send(random.choice(response))
                await message.add_reaction('🤓')  # 🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓

bot.run(TOKEN)
