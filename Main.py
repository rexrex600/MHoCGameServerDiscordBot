import discord
import asyncio
import pickle

test = discord.Client()
file = open('MuteList.txt', 'r')

mute_list = []
mute_list = file.read().split(',')

commands = ['join', 'shutdown', 'leave', 'smashcapitalism', 'mute', 'unmute']
chats = ['rocketleague', 'menofwar', 'minecraft', 'paradox','politicalmachine','ksp', 'gta']

@test.event
async def on_ready():
    print('Logged in as')
    print(test.user.name)
    print(test.user.id)
    print('------')


@test.event
async def on_message(message):
    global mute_list
    global file
    contents = message.content
    if contents[0] == '!':
        print("command: ",  contents, "author: ", message.author)
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
            elif contents[0] == 'smashcapitalism':
                await test.send_message(message.channel, ':bomb: SMASH CAPITALISM :bomb:')
            elif contents[0] == 'shutdown' and message.author.name == 'rexrex600':
                file.close()
                await test.delete_message(message)
                await test.close()
            elif contents[0] == 'shutdown' and message.author.name != 'rexrex600':
                await test.send_message(destination=message.channel, content='Fuck off', tts=True)
            elif contents[0] == 'mute' and message.author.permissions_in(message.channel).kick_members is True:
                file = open('MuteList.txt', 'r')
                mute_list = file.read().split(',')
                mute_list = [i for i in mute_list if i != '']
                if contents[1] not in mute_list:
                    file.close
                    mute_list.append(contents[1])
                    file = open('MuteList.txt', 'w')
                    dump_str = ''
                    for i in mute_list:
                        dump_str += i + ','
                    file.write(dump_str)
                else:
                    await test.send_message(message.author, 'user is already muted')
                file.close()

            elif contents[0] == 'unmute' and message.author.permissions_in(message.channel).kick_members is True:
                file = open('MuteList.txt', 'r')
                mute_list = file.read().split(',')
                mute_list = [i for i in mute_list if i != '']
                if contents[1] in mute_list:
                    file.close()
                    mute_list.remove(contents[1])
                    file = open('MuteList.txt', 'w')
                    dump_str = ''
                    for i in mute_list:
                        dump_str += i + ','
                    file.write(dump_str)
                else:
                    await test.send_message(message.author, 'user is not muted')
                file.close()
        else:
            await test.send_message(destination=message.channel, content='Invalid Command')
        await test.delete_message(message)
    if ('#' + str(message.author).split('#')[1]) in mute_list:
        await test.delete_message(message)


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(test.login(str(input('Enter token: \n'))))
    loop.run_until_complete(test.connect())
except Exception:
    loop.run_until_complete(test.close())
finally:
    loop.close()
