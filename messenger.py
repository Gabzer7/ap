import argparse
import datetime

from localstorage import LocalStorage
from remotestorage import RemoteStorage


class UserInterface:
    def __init__(self, storage):
        self._storage = storage

    def run(self):
        choix = ""
        while choix != "0":
            print("\n=== MESSENGER ===")
            print("1. Afficher les utilisateurs")
            print("2. Afficher les groupes")
            print("3. Ajouter un utilisateur")
            print("4. Ajouter un groupe")
            print("5. Afficher les messages")
            print("6. Publier un message")
            print("0. Quitter")

            choix = input("\nVotre choix : ").strip()

            if choix == "1":
                self.show_users()
            elif choix == "2":
                self.show_channels()
            elif choix == "3":
                self.add_user()
            elif choix == "4":
                self.add_channel()
            elif choix == "5":
                self.show_messages()
            elif choix == "6":
                self.post_message()
            elif choix == "0":
                print("Au revoir !")
            else:
                print("Choix incorrect.")

    def show_users(self):
        print("\nLISTE DES UTILISATEURS")
        for u in self._storage.get_users():
            print(u.id, ":", u.name)
        input("\nEntrée pour revenir")

    def show_channels(self):
        print("\nLISTE DES GROUPES")
        for c in self._storage.get_channels():
            print("Id:", c.id, "Nom:", c.name)
        input("\nEntrée pour revenir")

    def add_user(self):
        nom = input("Nom du nouvel utilisateur : ").strip()
        if nom:
            self._storage.create_user(nom)
            print("Utilisateur ajouté.")
        input("Entrée pour revenir")

    def add_channel(self):
        nom = input("Nom du nouveau groupe : ").strip()
        if nom:
            self._storage.create_channel(nom)
            print("Groupe créé.")
        input("Entrée pour revenir")

    def show_messages(self):
        print("\nDERNIERS MESSAGES")
        messages = self._storage.get_messages()
        users_dict = {u.id: u.name for u in self._storage.get_users()}
        channels_dict = {c.id: c.name for c in self._storage.get_channels()}

        if not messages:
            print("Aucun message à afficher.")
        
        for m in messages:
            nom_auteur = users_dict.get(m.sender_id, f"Inconnu({m.sender_id})")
            nom_canal = channels_dict.get(m.channel, f"Inconnu({m.channel})")
            
            # Format d'affichage avec horodatage
            print(f"[{m.reception_date}] {nom_auteur} (sur {nom_canal}) : {m.content}")
        
        input("\nEntrée pour revenir")

    def post_message(self):
        try:
            sender_id = int(input("Votre ID utilisateur : "))
            channel_id = int(input("ID du groupe de destination : "))
        except ValueError:
            print("Erreur : Les IDs doivent être des nombres entiers.")
            return

        content = input("Votre message : ").strip()
        if content:
            date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._storage.create_message(sender_id, channel_id, content, date_str)
            print("Message publié !")
        
        input("Entrée pour revenir")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--storage-file", default="server.json")
    parser.add_argument("--url", default=None)
    args = parser.parse_args()

    if args.url:
        storage = RemoteStorage() 
    else:
        storage = LocalStorage(args.storage_file)
        storage.load()

    ui = UserInterface(storage)
    ui.run()


if __name__ == "__main__":
    main()