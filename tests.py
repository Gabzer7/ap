import unittest
import os
from localstorage import LocalStorage

class TestMessenger(unittest.TestCase):
    
    def setUp(self):
        # S'exécute avant chaque test. On crée un fichier temporaire.
        self.test_file = "test_data.json"
        with open(self.test_file, "w") as f:
            f.write('{"users": [], "channels": [], "messages": []}')
        
        self.storage = LocalStorage(self.test_file)
        self.storage.load()

    def tearDown(self):
        # S'exécute après chaque test. On nettoie le fichier temporaire.
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_ajout_utilisateur(self):
        self.storage.create_user("TestUser")
        utilisateurs = self.storage.get_users()
        self.assertEqual(len(utilisateurs), 1)
        self.assertEqual(utilisateurs[0].name, "TestUser")

    def test_ajout_groupe(self):
        self.storage.create_channel("TestGroup")
        groupes = self.storage.get_channels()
        self.assertEqual(len(groupes), 1)
        self.assertEqual(groupes[0].name, "TestGroup")

    def test_ajout_message(self):
        self.storage.create_message(1, 1, "Bonjour tout le monde", "2024-03-01 10:00:00")
        messages = self.storage.get_messages()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].content, "Bonjour tout le monde")
        self.assertEqual(messages[0].sender_id, 1)

if __name__ == '__main__':
    unittest.main()