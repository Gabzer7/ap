import json
from model import User,Channel,Message

class Server:
    # - N'oubliez pas le typage
    # - Pourquoi utiliser None en valeur par défaut ? Vous pouvez directement mettre une liste vide
    def __init__(self, users: list[Channel]=[], channels: list[Channel]=[], messages: list[Message]=[]):
        self.users = users
        self.channels = channels
        self.messages = messages

    def next_user_id(self) -> int:
        return (max(u.id for u in self.users) + 1) if self.users else 1

    def next_channel_id(self) -> int:
        return (max(c.id for c in self.channels) + 1) if self.channels else 1
    
    def next_message_id(self) -> int:
        return (max(m.id for m in self.messages) + 1) if self.messages else 1


class LocalStorage:

    def __init__(self, chemin="server.json"):
        self.chemin = chemin
        # Vous auriez pu stocker les attributs users, channels, et messages
        # directement dans LocalStorage et vous affranchir
        # de la définition d'une classe Server
        self.server = Server()  

    def load(self):
        with open(self.chemin, "r") as f:
            data = json.load(f)
        users = [User(u["id"], u["name"]) for u in data.get("users", [])]
        channels = [Channel(c["id"], c["name"], c.get("member_ids", [])) for c in data.get("channels", [])]
        messages = [Message(m["id"], m["reception_date"], m["sender_id"], m["channel"], m["content"])for m in data.get("messages", [])]
        self.server = Server(users, channels, messages)
        return self.server

    def save(self):
        data = {
            "users": [{"id": u.id, "name": u.name} for u in self.server.users],
            "channels": [{"id": c.id, "name": c.name, "member_ids": c.member_ids} for c in self.server.channels],
            "messages": [{
                "id": m.id,
                "reception_date": m.reception_date,
                "sender_id": m.sender_id,
                "channel": m.channel,
                "content": m.content
            } for m in self.server.messages],
        }
        with open(self.chemin, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_users(self) -> list[User]:
        return self.server.users

    def get_channels(self):
        return self.server.channels

    def get_messages(self):
        return self.server.messages

    def create_user(self, username: str):
        new_id = self.server.next_user_id()
        u = User(new_id, username)
        self.server.users.append(u)
        self.save()
        return u

    def create_channel(self, nom: str):
        new_id = self.server.next_channel_id()
        c = Channel(new_id, nom, [])
        self.server.channels.append(c)
        self.save()
        return c
    
    def create_message(self, sender_id: int, channel_id: int, content: str, date: str):
        new_id = self.server.next_message_id()
        m = Message(new_id, date, sender_id, channel_id, content)
        self.server.messages.append(m)
        self.save()
        return m

