import discord
from discord.ext import commands


class CogRemoveDupes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = "removedupes",
                    usage="",
                    description = "Remove all duplicates songs from the queue.")
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx):

        if ctx.author.voice is None:
            return await ctx.channel.send(f"<:False:798596718563950653> {ctx.author.mention} You are not connected in a voice channel!")
        if ctx.guild.voice_client and self.bot.user.id not in [
            i.id for i in ctx.author.voice.channel.members
        ]:
            return await ctx.channel.send(f"<:False:798596718563950653> {ctx.author.mention} You are not connected in the same voice channel that the bot!")
        if len(self.bot.music[ctx.guild.id]["musics"]) <= 0:
            return await ctx.channel.send(f"<:False:798596718563950653> {ctx.author.mention} The queue is empty!")

        # Remove duplicates
        newQueue = []
        for i in self.bot.music[ctx.guild.id]["musics"]:
            if i["music"].url not in [ i["music"].url for i in newQueue]:
                newQueue.append(i)

        self.bot.music[ctx.guild.id]["musics"] = newQueue

        embed=discord.Embed(title="Duplicate songs removed", description=f"All duplicate songs in the queue was removed!", color=discord.Colour.random())
        embed.set_footer(text=f"Requested by {ctx.author} | Open source", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

    @commands.command(name = "leavecleanup",
                    aliases=["lc"],
                    usage="",
                    description = "Remove absent user's songs from the queue.")
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def leavecleanup(self, ctx):
        
        if ctx.author.voice is None:
            return await ctx.channel.send(f"<:False:798596718563950653> {ctx.author.mention} You are not connected in a voice channel!")
        if ctx.guild.voice_client and self.bot.user.id not in [
            i.id for i in ctx.author.voice.channel.members
        ]: 
            return await ctx.channel.send(f"<:False:798596718563950653> {ctx.author.mention} You are not connected in the same voice channel that the bot!")
        if len(self.bot.music[ctx.guild.id]["musics"]) <= 0:
            return await ctx.channel.send(f"<:False:798596718563950653> {ctx.author.mention} The queue is empty!")

        newQueue = [
            i
            for i in self.bot.music[ctx.guild.id]["musics"]
            if i["requestedBy"].id
            in [i.id for i in ctx.author.voice.channel.members]
        ]
        self.bot.music[ctx.guild.id]["musics"] = newQueue

        embed=discord.Embed(title="Absent user's songs removed", description=f"All absent user's songs in the queue was removed!", color=discord.Colour.random())
        embed.set_footer(text=f"Requested by {ctx.author} | Open source", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(CogRemoveDupes(bot))