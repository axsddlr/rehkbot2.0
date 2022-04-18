import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv("DISCORD_GUILD")


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="avatar", description="Display the avatar.")
    @app_commands.describe(user="The user to get the avatar from.")
    @app_commands.checks.bot_has_permissions(embed_links=True)
    @app_commands.guilds(discord.Object(id=GUILD))
    async def avatar(self, interaction: discord.Interaction, user: discord.Member = None):
        if not user:
            user = interaction.user
        await interaction.response.send_message(user.display_avatar.url)

    @app_commands.command(name="banner", description="Display the banner.")
    @app_commands.describe(user="The user to get the banner from.")
    @app_commands.checks.bot_has_permissions(embed_links=True)
    @app_commands.checks.has_permissions(use_slash_commands=True)
    @app_commands.guilds(discord.Object(id=GUILD))
    async def banner(self, interaction: discord.Interaction, user: discord.Member = None):
        if not user:
            user = interaction.user
        user = await self.bot.fetch_user(user.id)
        try:
            await interaction.response.send_message(user.banner.url)
        except:
            await interaction.response.send_message("This user doesn't have a banner.")


async def setup(bot):  # set async function
    await bot.add_cog(Info(bot))  # Use await
