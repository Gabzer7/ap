import json

# --- DONNÉES ET SAUVEGARDE ---

server = {
    'users': [
        {'id': 41, 'name': 'Alice'},
        {'id': 23, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 12, 'name': 'Town square', 'member_ids': [41, 23]}
    ],
    'messages': [
        {
            'id': 18,
            'reception_date': '2025-12-09 15:00',
            'sender_id': 41,
            'channel': 12,
            'content': 'Hi 👋'
        }
    ]
}


fichier = open('server.json', 'r')
server = json.load(fichier)
fichier.close()
print("Données chargées !")

def sauvegarder():
    fichier = open('server.json', 'w')
    json.dump(server, fichier, indent=4)
    fichier.close()
    print("Sauvegarde effectuée")

def afficher_utilisateurs():
    print('\nLISTE DES UTILISATEURS')
    for user in server['users']:
        print(user['id'], ': ', user['name'])
    input('\nAppuyez sur Entrée pour retourner au menu principal')

def afficher_groupes():
    print('\nLISTE DES GROUPES')
    for group in server['channels']:
        print('Id:', group['id'], 'Nom:', group['name'])
    input('\nAppuyez sur Entrée pour retourner au menu principal')

def ajouter_utilisateur():
    print('\nAJOUT UTILISATEUR')
    nom = input('Nom du nouvel utilisateur : ')
    if len(server['users']) > 0:
        dernier_id = server['users'][-1]['id']
        nouvel_id = dernier_id + 1
    else:
        nouvel_id = 1   
    nouveau = {'id': nouvel_id, 'name': nom}
    server['users'].append(nouveau)
    
    sauvegarder()
    print(f"Succès : L'utilisateur {nom} a été ajouté.")
    
    input('\nAppuyez sur Entrée pour retourner au menu principal')

def ajouter_groupe():
    print('\nAJOUT GROUPE')
    nom = input('Nom du nouveau groupe : ')
    
    if len(server['channels']) > 0:
        dernier_id = server['channels'][-1]['id']
        nouvel_id = dernier_id + 1
    else:
        nouvel_id = 1
    
    nouveau = {'id': nouvel_id, 'name': nom, 'member_ids': []}
    server['channels'].append(nouveau)
    
    sauvegarder()
    print(f"Le groupe {nom} a été créé.")
    
    input('\nAppuyez sur Entrée pour retourner au menu principal')

def afficher_messages():
    print('\nMESSAGES')
    id_groupe = input('Entrez l\'ID du groupe à lire : ')
    id_groupe = int(id_groupe)
    compteur = 0
    print(f"Messages du groupe {id_groupe} :")
    for message in server['messages']:
        if message['channel'] == id_groupe:
            print(f"[{message['reception_date']}] : {message['content']}")
            compteur = compteur + 1
        
    if compteur == 0:
        print("Aucun message ou groupe vide.")
            
    print("Erreur : L'ID doit être un nombre.")
    input('\nAppuyez sur Entrée pour retourner au menu principal...')

def menu_principal():
    choix = ''
    while choix != '0':
        print('=== MESSENGER ===')
        print('1. Afficher les utilisateurs')
        print('2. Afficher les groupes')
        print('3. Ajouter un utilisateur')
        print('4. Ajouter un groupe')
        print('5. Voir les messages d\'un groupe')
        print('0. Quitter')
        
        choix = input('\nVotre choix : ')

        if choix == '0':
            print('Au revoir !')
        elif choix == '1':
            afficher_utilisateurs()
        elif choix == '2':
            afficher_groupes()
        elif choix == '3':
            ajouter_utilisateur()
        elif choix == '4':
            ajouter_groupe()
        elif choix == '5':
            afficher_messages()
        else:
            print('Choix incorrect.')
            input('Entrée pour réessayer')

menu_principal()