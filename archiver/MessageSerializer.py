import discord 
import json

class MessageSerializer():

    @classmethod
    def serializeToJSON(cls, obj):
        if (isinstance(obj, discord.Message)):
            return cls.serializeMessage(obj)


    @classmethod
    def serializeMessage(cls, message):
        d = dict()
        for k in message.__slots__:
            if (k == '_state' or k.startswith("_")):
                continue
            d[k] = str(getattr(message, k))
        
        return json.dumps(d)

        