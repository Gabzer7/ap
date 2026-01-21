import requests 
import json
from model import User,Channel,Message


class RemoteStorage:
    def __init__(self):
        self.base_url = "https://groupe5-python-mines.fr"

    def get_users(self):
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

    def create_user(self, username: str):
        ajout = {"name": username}
        response = requests.post(f'{self.base_url}/users/create', json = ajout)
        response.raise_for_status()

    def create_channel(self, nom):
        ajout = {"name" : nom}
        response = requests.post(f'{self.base_url}/channels/create', json = ajout)
        response.raise_for_status()
