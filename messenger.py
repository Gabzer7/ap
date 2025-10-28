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

print('=== Messenger ===')

print('x. Leave')

print('u. Afficher les utilisateurs')

#print('g. Afficher les groupes')

choice = input('Select an option: ')

if choice == 'x':
    print('Bye!')

elif choice == 'u':
    # server['users'] est une LISTE → on itère directement
    for user in server['users']:
        print(user['id'], ': ', user['name'])

#elif choice == 'g':
#    print(server['channels'])
#    print("Voulez-vous afficher les messages d'un groupe ?")
#    choix = input('Select a group')
#    if choix in server['messages']['channel']:
#        print (server['messages']['content']  server['messages']

else:
    print('Unknown option:', choice)
