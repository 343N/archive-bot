import json
import discord

from .MessageSerializer import MessageSerializer

class MessageHistoryHandler():

    def __init__(self, client: discord.Bot, channel: discord.channel.TextChannel) -> None:
        self.client = client
        self.channel = channel
        pass

    async def getMessages(self):
        h = self.channel.history(limit=None, oldest_first = True)
        
        with open('messages.json', 'w') as f:
            JSONstr = ""
            JSONstr += '{"messages":['
            m = 0
            async for message in h:
                if (m != 0): JSONstr+= ','
                data = MessageSerializer.serializeToJSON(message)
                JSONstr += data
                m +=1
                
            JSONstr += ']}'
            f.write(
                json.dumps(
                    json.loads(JSONstr), indent=4
                    )
                )

            
        

        
