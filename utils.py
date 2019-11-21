import calendar
import os
import json
import discord
import random
from datetime import datetime
from config import getLogger, getMongoClient
from dateutil.relativedelta import relativedelta
from discord.ext.commands import errors
from bson.json_util import dumps


def loadAllCogs(bot):
    # loads cogs
    for cog in os.listdir("cogs"):
        if cog.endswith("py"):
            filename = cog.split(".")[0]
            try:
                bot.load_extension(f"cogs.{filename}")
                getLogger().info(f"[Cog Management] Cog Loaded: {filename}")
            except (errors.ExtensionNotFound, errors.ExtensionAlreadyLoaded, errors.NoEntryPointError,
                    errors.ExtensionFailed) as e:
                getLogger().error(f"[Cog Management] Error loading cog: {filename} - {e}")


def loadAllExtensions(bot):
    for extension in os.listdir("extensions"):
        if extension.endswith("py"):
            file = extension.split(".")[0]
            try:
                bot.load_extension(f"extensions.{file}")
                getLogger().info(f"[Extension Management] Extension Loaded: {file}")
            except (errors.ExtensionNotFound, errors.ExtensionAlreadyLoaded, errors.NoEntryPointError,
                    errors.ExtensionFailed) as e:
                getLogger().error(f"[Extension Management] Error loading extension: {file} - {e}")


def utc_to_epoch(utc: datetime):
    return calendar.timegm(utc.utctimetuple())


class EpochUtils(float):
    def __init__(self, unix):
        self.rdelta = relativedelta(datetime.now(), datetime.fromtimestamp(unix))

    def seconds(self):
        return self.rdelta.seconds

    def minutes(self):
        return self.rdelta.minutes

    def hours(self):
        return self.rdelta.hours

    def days(self):
        return self.rdelta.days

    def months(self):
        return self.rdelta.months

    def years(self):
        return self.rdelta.years


class UserProfiles(discord.Member):
    def __init__(self, member):
        mongoclient = getMongoClient()
        self.db = mongoclient["PyBot"]
        self.user_collection = self.db["users"]
        self.member = member

        user = self.user_collection.find_one({"id": member.id})
        if not user:
            user_payload = {
                "id": member.id,
                "RPGData": {
                    "CreatedCharacter": False,
                    "Name": {
                        "FirstName": "none",
                        "MiddleName": "none",
                        "LastName": "none",
                    },
                    "Race": "none",
                    "Stats": {
                        "Level": 1,
                        "CurrentExp": 0,
                        "MaxExp": 100,
                        "Sheckels": 10,
                    },
                    "Inventory": [],
                },
                "MiscData": {
                    "strikes": []
                }
            }
            idd = self.user_collection.insert_one(user_payload).inserted_id
            getLogger().debug(f"[MongoDB] Created user document for '{member.name}' ({member.id}), Document ID: {idd}")

    def getUserProfile(self):
        profile = self.user_collection.find_one({"id": self.member.id})
        return json.loads(dumps(profile))

    def update(self, key, value):
        self.user_collection.update_one({"id": self.member.id}, {"$set": {key: value}})

    def reset(self):
        result = self.user_collection.delete_one({"id": self.member.id})
        return result


class ServerSettings(discord.Guild):
    def __init__(self, guild):
        self.guild = guild
        mongoclient = getMongoClient()
        self.db = mongoclient["PyBot"]
        self.server_collection = self.db["servers"]

        server = self.server_collection.find_one({"id": guild.id})
        if not server:
            guild_payload = {
                "id": guild.id,
                "settings": {
                    "log_channel": None,
                    "message_responses_enabled": False,
                    "counting_channel_enabled": False,
                    "events": {
                        "member_join": True,
                        "member_leave": True,
                        "member_update": True,
                        "member_ban": True,
                        "member_unban": True,
                        "message_delete": True,
                        "build_message_delete": True,
                        "message_edit": True,
                        "guild_channel_delete": True,
                        "guild_channel_create": True,
                        "guild_channel_update": True,
                        "user_update": True,
                        "guild_update": True,
                        "guild_role_created": True,
                        "guild_role_delete": True,
                        "guild_role_update": True,
                        "guild_emojis_update": True
                    }
                }
            }
            idd = self.server_collection.insert_one(guild_payload).inserted_id
            getLogger().debug(f"[MongoDB] Created server document for '{guild.name}' ({guild.id}), Document ID: {idd}")

    def getServerDocument(self):
        document = self.server_collection.find_one({"id": self.guild.id})
        return json.loads(dumps(document))

    def update(self, key, value):
        self.server_collection.update_one({"id": self.guild.id}, {"$set": {key: value}})

    def reset(self):
        result = self.server_collection.delete_one({"id": self.guild.id})
        return result


def getRandomFact():
    file = open("didyouknow.json", 'r')
    file_content = file.read()
    json_data = json.loads(file_content)
    return random.choice(json_data)
