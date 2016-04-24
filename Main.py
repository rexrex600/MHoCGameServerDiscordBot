import discord
import asyncio

test = discord.Client()

commands = ['join', 'shutdown', 'leave', 'smashcapitalism']
chats = ['rocketleague', 'menofwar', 'minecraft', 'paradox','politicalmachine','ksp', 'gta']

@test.event
async def on_ready():
    print('Logged in as')
    print(test.user.name)
    print(test.user.id)
    print('------')


@test.event
async def on_message(message):
    contents = message.content
    if contents[0] == '!':
        contents = contents[1::]
        contents = contents.split(' ')
        if contents[0] in commands:
            if contents[0] == 'join' and contents[1] in chats:
                role = message.server.roles
                for i in role:
                    if i.name == contents[1].lower():
                        await test.add_roles(message.author, i)
            elif contents[0] == 'leave' and contents[1] in chats:
                role = message.server.roles
                for i in role:
                    if i.name == contents[1].lower():
                        await test.remove_roles(message.author, i)
            elif contents[0] == 'shutdown' and message.author.name == 'rexrex600':
                await test.close()
            elif contents[0] == 'shutdown' and message.author.name != 'rexrex600':
                await test.send_message(destination=message.channel, content='Fuck off', tts=True)
            elif contents[0] == 'smashcapitalism':
                await test.send_message(message.channel, ':bomb: SMASH CAPITALISM :bomb:')
        else:
            await test.send_message(destination=message.channel, content='Invalid Command')


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(test.login(str(input('Enter token: \n'))))
    loop.run_until_complete(test.connect())
except Exception:
    loop.run_until_complete(test.close())
finally:
    loop.close()
