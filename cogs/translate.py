import discord
from discord import app_commands
from discord.ext import commands

from googletrans import Translator


class Translate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="translate", description="google translator .")
    @app_commands.describe(lang="destination language", text="the language you want to translate")
    @app_commands.guilds(discord.Object(id=235999739978448896))
    async def translate(self, ctx: discord.Interaction, lang: str, *, text: str):
        """Usage: `.translate {destination language} {the sentence you want to translate}`"""
        translator = Translator()
        translation = translator.translate(text, dest=lang)
        await ctx.response.defer()  # wait for followup message

        await ctx.followup.send(f"{lang} " + "translation: " + f"**`{translation.text}`**")


async def setup(bot):  # set async function
    await bot.add_cog(Translate(bot))  # Use await
