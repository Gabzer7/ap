class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Channel:
    def __init__(self, id: int, name: str, member_ids: list[int] | None = None):
        self.id = id
        self.name = name
        self.member_ids = member_ids if member_ids is not None else []

class Message:
    def __init__(self, id: int, reception_date: str, sender_id: int, channel: int, content: str):
        self.id = id
        self.reception_date = reception_date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content