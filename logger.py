import discord

class Logger:
    def __init__(self, name):
        self.name = name

    def log(self, message):
        """

        :type message: discord.message
        """
        file = open(self.name, 'a')
        file.write(str(message.timestamp) + ' : ' + message.content + ' : ' + message.author.name + ' : ' + 
                   message.author.id + '\n')
        file.close()
