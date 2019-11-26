import discord
import random
import re
import requests
from datetime import datetime
from discord.ext import commands
from config import getRedditClient
from utils import getLogger

gfycat_regex = re.compile(r'(https://gfycat.com/(.*))(\?.*)?')
imgur_regex = re.compile(r'(https://i.imgur.com/(.*))(\?.*)?')
reddit_regex = re.compile(r'(https://i.redd.it/(.*))(\?.*)?')


class NSFWCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="boobs", hidden=True, enabled=False)
    @commands.has_role("NSFW Tester")
    @commands.is_nsfw()
    @commands.guild_only()
    async def boobs(self, ctx):
        boob_subreddits = ["boobs", "Boobies", "Bigtitssmalltits", "naturaltitties", "BustyPetite"]
        subreddit = random.choice(boob_subreddits)
        posts = getRedditClient().subreddit(subreddit).new(limit=100)
        post = random.choice([x for x in posts])
        print(post.url)

        if gfycat_regex.match(post.url):
            direct_link = getGfycatDirect(post.url)
            if direct_link:
                embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                      timestamp=datetime.utcnow())
                embed.set_image(url=direct_link)
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                return await ctx.send(content=None, embed=embed)
        elif imgur_regex.match(post.url) or reddit_regex.match(post.url):
            embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                  timestamp=datetime.utcnow())
            embed.set_image(url=post.url)
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            getLogger().debug(post.url)
            return await ctx.send(content=None, embed=embed)
        else:
            return await ctx.send(f"Nothing found :(")

    @commands.command(name="boobdrop", hidden=True, enabled=False)
    @commands.has_role("NSFW Tester")
    @commands.is_nsfw()
    @commands.guild_only()
    async def boobdrop(self, ctx):
        posts = getRedditClient().subreddit("TittyDrop").new(limit=1000)
        post = random.choice([x for x in posts])
        print(post.url)

        if gfycat_regex.match(post.url):
            direct_link = getGfycatDirect(post.url)
            if direct_link:
                embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                      timestamp=datetime.utcnow())
                embed.set_image(url=direct_link)
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                return await ctx.send(content=None, embed=embed)
        elif imgur_regex.match(post.url) or reddit_regex.match(post.url):
            embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                  timestamp=datetime.utcnow())
            embed.set_image(url=post.url)
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            getLogger().debug(post.url)
            return await ctx.send(content=None, embed=embed)
        else:
            return await ctx.send(f"Nothing found :(")

    @commands.command(name="pussy", hidden=True, enabled=False)
    @commands.has_role("NSFW Tester")
    @commands.is_nsfw()
    @commands.guild_only()
    async def pussy(self, ctx):
        pussy_subreddits = ["pussy", "LipsThatGrip"]
        posts = getRedditClient().subreddit(random.choice(pussy_subreddits)).new(limit=100)
        post = random.choice([x for x in posts])
        print(post.url)

        if gfycat_regex.match(post.url):
            direct_link = getGfycatDirect(post.url)
            if direct_link:
                embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                      timestamp=datetime.utcnow())
                embed.set_image(url=direct_link)
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                return await ctx.send(content=None, embed=embed)
        elif imgur_regex.match(post.url) or reddit_regex.match(post.url):
            embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                  timestamp=datetime.utcnow())
            embed.set_image(url=post.url)
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            getLogger().debug(post.url)
            return await ctx.send(content=None, embed=embed)
        else:
            return await ctx.send(f"Nothing found :(")

    @commands.command(name="ass", hidden=True, enabled=False)
    @commands.has_role("NSFW Tester")
    @commands.is_nsfw()
    @commands.guild_only()
    async def ass(self, ctx):
        pussy_subreddits = ["asshole", "AssOnTheGlass", "SpreadEm", "booty_gifs"]
        posts = getRedditClient().subreddit(random.choice(pussy_subreddits)).new(limit=100)
        post = random.choice([x for x in posts])
        print(post.url)

        if gfycat_regex.match(post.url):
            direct_link = getGfycatDirect(post.url)
            if direct_link:
                embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                      timestamp=datetime.utcnow())
                embed.set_image(url=direct_link)
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                return await ctx.send(content=None, embed=embed)
        elif imgur_regex.match(post.url) or reddit_regex.match(post.url):
            embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                  timestamp=datetime.utcnow())
            embed.set_image(url=post.url)
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            getLogger().debug(post.url)
            return await ctx.send(content=None, embed=embed)
        else:
            return await ctx.send(f"Nothing found :(")

    @commands.command(name="nsfw", hidden=True, enabled=False)
    @commands.has_role("NSFW Tester")
    @commands.is_nsfw()
    @commands.guild_only()
    async def nsfw(self, ctx):
        nsfw_subreddits = ["nsfw", "NSFW_GIFS", "squirting", "pussy", "whenitgoesin", "scissoring", "boobs", "gonewild", "RealGirls", "OnOff", "bdsm", "Bondage", "pawg", "PetiteGoneWild", "GirlsWithToys", "NSFW_4K", "NsfwAss", "60fpsporn", "NSFW_HTML5", "iWantToFuckHer", "HighResNSFW", "nsfwhardcore", "celebnsfw", "Amateur", "Nsfw_Amateurs", "ass", "bigasses", "anal", "asshole", "AssOnTheGlass", "SpreadEm", "booty_gifs", "SheLikesItRough", "facesitting", "curvy", "petite", "xsmallgirls", "collegesluts", "CollegeAmateurs", "collegensfw", "Gonewild18", "gonewildcouples", "gwcumsluts", "workgonewild", "LegalTeens", "Just18", "barelylegalteens", "Barelylegal", "LipsThatGrip", "rearpussy", "Boobies", "TittyDrop", "Bigtitssmalltits", "BustyPetite", "naturaltitties"]
        posts = getRedditClient().subreddit(random.choice(nsfw_subreddits)).new(limit=100)
        post = random.choice([x for x in posts])
        print(post.url)

        if gfycat_regex.match(post.url):
            direct_link = getGfycatDirect(post.url)
            if direct_link:
                embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                      timestamp=datetime.utcnow())
                embed.set_image(url=direct_link)
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                return await ctx.send(content=None, embed=embed)
        elif imgur_regex.match(post.url) or reddit_regex.match(post.url):
            embed = discord.Embed(title=f"{post.title}", description=None, color=discord.Color.green(),
                                  timestamp=datetime.utcnow())
            embed.set_image(url=post.url)
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            getLogger().debug(post.url)
            return await ctx.send(content=None, embed=embed)
        else:
            return await ctx.send(f"Nothing found :(")


def getGfycatDirect(link):
    try:
        gfycat_id = link.split("/")[-1].split("-")[0].split("?")[0]
        response = requests.get(f"https://api.gfycat.com/v1/gfycats/{gfycat_id}").json()
        return response["gfyItem"]["gifUrl"]
    except Exception as e:
        getLogger().error(f"[NSFWCommands] boobdrop; Error: {e}")
        return None


def setup(bot):
    bot.add_cog(NSFWCommands(bot))
