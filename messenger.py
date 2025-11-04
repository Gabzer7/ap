from datetime import datetime

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
            'reception_date': datetime.now(),
            'sender_id': 41,
            'channel': 12,
            'content': 'Hi 👋'
        }
    ]
}

def menu_principal():

    print('=== Messenger ===')

    print('0. Leave')

    print('1. Afficher les utilisateurs')

    print('2. Afficher les groupes')

    choix = input('Select an option :')

    if choix == '0':
        print('Bye!')

    elif choix == '1':
        afficher_utilisateurs()

    elif choix == '2':
        afficher_groupes()

    else:
        print('Unknown option:')
        menu_principal

def afficher_utilisateurs():
       # server['users'] est une LISTE → on itère directement
    for user in server['users']:
        print(user['id'], ': ', user['name'])
    choix1 = input('0 : Retour au menu principal')
    if choix1 == '0':
        menu_principal()
    else:
        print('Unknown option:', choix1)


def afficher_groupes():
    for group in server['channels']:
        print('Id :', group['id'], ' Nom :', group['name'], ' Membres :', group['member_ids'])
    choix = input('0 : Retour au menu principal')
    if choix == '0':
        menu_principal()
    else:
        print('Unknown option:', choix)
    
menu_principal()


#elif choice == 'g':
#    print(server['channels'])
#    print("Voulez-vous afficher les messages d'un groupe ?")
#    choix = input('Select a group')
#    if choix in server['messages']['channel']:
#        print (server['messages']['content']  server['messages']


