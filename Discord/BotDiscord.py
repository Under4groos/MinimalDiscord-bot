 
import Model.JsonObject
import discord

_json = Model.JsonObject.JsonModel("Data\data.json").Serialization()

discord_client = discord.Client()

@discord_client.event

async def on_message(ctx):
    print( ctx.content)

discord_client.run(_json["token"])
