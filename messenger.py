import json

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


class Server:
    def __init__(self, users: list[User], channels: list[Channel], messages: list[Message]):
        self.users = users
        self.channels = channels
        self.messages = messages

    def next_user_id(self):
        return (max(u.id for u in self.users) + 1) if self.users else 1

    def next_channel_id(self):
        return (max(c.id for c in self.channels) + 1) if self.channels else 1


fichier = open('server.json', 'r')
server = json.load(fichier)
users = [User(u["id"], u["name"]) for u in server["users"]]
channels = [Channel(c["id"], c["name"], c.get("member_ids", [])) for c in server["channels"]]
messages = [
    Message(m["id"], m["reception_date"], m["sender_id"], m["channel"], m["content"])
    for m in server["messages"]
]

server = Server(users, channels, messages)
fichier.close()
print("Données chargées !")

def sauvegarder():
    server2 = {
        "users": [{"id": u.id, "name": u.name} for u in server.users],
        "channels": [{"id": c.id, "name": c.name, "member_ids": c.member_ids} for c in server.channels],
        "messages": [{
            "id": m.id,
            "reception_date": m.reception_date,
            "sender_id": m.sender_id,
            "channel": m.channel,
            "content": m.content
        } for m in server.messages]
    }
    with open("server.json", "w", encoding="utf-8") as fichier:
        json.dump(server2, fichier, indent=4, ensure_ascii=False)
    print("Sauvegarde effectuée")


def afficher_utilisateurs():
    print("\nLISTE DES UTILISATEURS")
    for user in server.users:
        print(user.id, ":", user.name)
    input("\nAppuyez sur Entrée pour retourner au menu principal")


def afficher_groupes():
    print("\nLISTE DES GROUPES")
    for group in server.channels:
        print("Id:", group.id, "Nom:", group.name)
    input("\nAppuyez sur Entrée pour retourner au menu principal")


def ajouter_utilisateur():
    print("\nAJOUT UTILISATEUR")
    nom = input("Nom du nouvel utilisateur : ").strip()
    nouvel_id = server.next_user_id()

    server.users.append(User(nouvel_id, nom))
    sauvegarder()
    print(f"Succès : L'utilisateur {nom} a été ajouté.")
    input("\nAppuyez sur Entrée pour retourner au menu principal")


def ajouter_groupe():
    print("\nAJOUT GROUPE")
    nom = input("Nom du nouveau groupe : ").strip()
    nouvel_id = server.next_channel_id()

    server.channels.append(Channel(nouvel_id, nom, []))
    sauvegarder()
    print(f"Le groupe {nom} a été créé.")
    input("\nAppuyez sur Entrée pour retourner au menu principal")


def afficher_messages():
    print("\nMESSAGES")
    raw = input("Entrez l'ID du groupe à lire : ").strip()

    try:
        id_groupe = int(raw)
    except ValueError:
        print("Erreur : L'ID doit être un nombre.")
        input("\nAppuyez sur Entrée pour retourner au menu principal...")
        return

    compteur = 0
    print(f"Messages du groupe {id_groupe} :")
    for message in server.messages:
        if message.channel == id_groupe:
            print(f"[{message.reception_date}] : {message.content}")
            compteur += 1

    if compteur == 0:
        print("Aucun message ou groupe vide.")

    input("\nAppuyez sur Entrée pour retourner au menu principal...")


def menu_principal():
    choix = ""
    while choix != "0":
        print("=== MESSENGER ===")
        print("1. Afficher les utilisateurs")
        print("2. Afficher les groupes")
        print("3. Ajouter un utilisateur")
        print("4. Ajouter un groupe")
        print("5. Voir les messages d'un groupe")
        print("0. Quitter")

        choix = input("\nVotre choix : ").strip()

        if choix == "0":
            print("Au revoir !")
        elif choix == "1":
            afficher_utilisateurs()
        elif choix == "2":
            afficher_groupes()
        elif choix == "3":
            ajouter_utilisateur()
        elif choix == "4":
            ajouter_groupe()
        elif choix == "5":
            afficher_messages()
        else:
            print("Choix incorrect.")
            input("Entrée pour réessayer")

menu_principal()