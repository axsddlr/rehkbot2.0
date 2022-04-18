from re import search

from discord.ext import commands


class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.links_allowed = (
        )
        self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(" \
                         r"\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".," \
                         r"<>?«»“”‘’])) "

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if message.channel.id not in self.links_allowed:
                if search(self.url_regex, message.content):
                    await message.delete()
                    await message.channel.send(
                        "No links allowed in this channel!", delete_after=10
                    )
                else:
                    return


async def setup(bot):
    await bot.add_cog(Links(bot))
