import requests 
import json
from model import User, Channel, Message


class RemoteStorage:
    def __init__(self):
        self.base_url = "https://groupe5-python-mines.fr"

    def get_users(self) -> list[User]:
        response = requests.get(f'{self.base_url}/users')
        response.raise_for_status()
        donnees = response.json()
        liste_utilisateurs = []
        for u in donnees:
            nouvel_utilisateur = User(u['id'], u['name'])
            liste_utilisateurs.append(nouvel_utilisateur)
            
        return liste_utilisateurs

    def get_channels(self) -> list[Channel]:
        response = requests.get(f'{self.base_url}/channels')
        response.raise_for_status()
        donnees = response.json()
        liste_channels = []
        for c in donnees:
            nouveau_channel = Channel(c['id'], c['name'], c.get('member_ids', []))
            liste_channels.append(nouveau_channel)           
        return liste_channels
    
    def get_messages(self):
            response = requests.get(f'{self.base_url}/messages')
            response.raise_for_status()
            donnees = response.json()
            liste_messages = []
            for m in donnees:

                channel_val = m.get('channel', m.get('channel_id', 0))
                
                nouveau_message = Message(
                    m.get('id', 0), 
                    m.get('reception_date', 'Date inconnue'), 
                    m.get('sender_id', 0), 
                    channel_val, 
                    m.get('content', '(Message vide)')
                )
                liste_messages.append(nouveau_message)
                
            return liste_messages

    def create_user(self, username: str):
        ajout = {"name": username}
        response = requests.post(f'{self.base_url}/users/create', json = ajout)
        response.raise_for_status()

    def create_channel(self, nom):
        ajout = {"name" : nom}
        response = requests.post(f'{self.base_url}/channels/create', json = ajout)
        response.raise_for_status()

    # Le paramètre date n'est pas utilisé dans cette fonction
    def create_message(self, sender_id: int, channel_id: int, content: str, date: str):
            ajout = {
                "sender_id": sender_id,
                "content": content
            }
            
            url = f'{self.base_url}/channels/{channel_id}/messages/post'
            
            response = requests.post(url, json=ajout)
                
            response.raise_for_status()