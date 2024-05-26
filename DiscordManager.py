import asyncio
import discord


def Start():
    with open("token.txt", "r") as file:
        TOKEN = file.read()


    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = discord.Client(loop=loop)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

        for channel in client.private_channels:
            if isinstance(channel, discord.GroupChannel):
                print(f'Group Chat: {channel.name}')
                for member in channel.recipients:
                    print(f'Member: {member.name}')
            elif isinstance(channel, discord.DMChannel):
                print(f'Direct Message with: {channel.recipient.name}')
            await channel.send("Слава Украине! 💙💛🇺🇦")

        for guild in client.guilds:
            print(f'Guild Name: {guild.name}')
            print(f'Guild ID: {guild.id}')
            for channel in guild.text_channels:
                print(f'Text Channel: {channel.name}')
                try:
                    await channel.send("Слава Украине! 💙💛🇺🇦")
                except:
                    ...
            print('------')

    client.run(TOKEN, bot=False)
