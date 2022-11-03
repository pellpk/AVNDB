import discord
from discord.ext import commands
import random

TOKEN = 'TOKEN HERE'

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
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
              it would require Einstein himself to build a device to strap me into so I can be connected to the energy of a billion stars to do it,
               and even then all that joke would get from people is a subtle scuff.
                You're lucky i still have the slightest of empathy for you after telling that joke,
                 otherwise I would have committed every war crime in the book just to prevent you from attempting any humor ever again.
                  We should put that joke in text books so future generations can be wary of becoming such an absolute comedic failure.
                   Im disappointed, hurt, and outright offended that my precious time has been wasted in my pathetic brain understanding that joke.
                    In the time that took i was planning on helping kids who have been orphaned,
                     but because of that you've wasted my time explaining the obscene integrity of your terrible attempt at comedy.
                      Now those kids are suffering with out meals and there's nobody to blame but you.
                       I hope you're happy with what you have done."""
    USER_IDS = {879004139361816596}  # IDs stored in a set
    NERD_EMOJI_HIM_USER_IDS = {839883479759585330, 266602020608278529, 736982476764741685, 520741459478052886}  # ids of people you wanna NERD EMOJI!!!!
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    guild = str(message.guild.name)
    print(f'{username}: {user_message} (posted in "#{channel}" in "{guild}")')

    if message.author == client.user:
        return

    if message.channel.name == 'alabama' or message.channel.name == 'ai':
        if message.content.lower() == 'hello' or message.content.lower() == 'hi':
            await message.channel.send(f'hello, {username}!')
            return
        elif message.content.lower() == 'bye':
            await message.channel.send(f'see ya, {username}!')
            return
        elif message.content.lower() == 'random':
            response = f'this is your random number: {random.randrange(100000000000)}'
            await message.channel.send(response)
            return

    if message.channel.name not in '#hydra-song-requests':
        if message.author.id in USER_IDS:
            response = [f'shut up, {username}', 'be quiet.', 'shush.', longtext1]
            await message.channel.send(random.choice(response))
        if random.randint(1, 100) <= 3:  # this is a 30% chance that the nerd emoji can be sent, this line can be deleted, or modified like 'if random.randint(1, 100) <= 5:'
            if message.author.id in NERD_EMOJI_HIM_USER_IDS:
                response = ['https://tenor.com/view/avengers-endgame-thanos-nerd-alert-opinion-nerd-gif-26272469']
                await message.channel.send(random.choice(response))
                await message.add_reaction('🤓')

client.run(TOKEN)
