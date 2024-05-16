# Система управления учетными записями
class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_access_level(self, access_level):
        self._access_level = access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._user_list = []

    def add_user(self, user):
        self._user_list.append(user)

    def remove_user(self, user):
        if user in self._user_list:
            self._user_list.remove(user)
        else:
            print(f"User {user.get_name()} not found in the list.")

# Пример использования:
user1 = User(1, "John Doe")
user2 = User(2, "Jane Smith")
admin = Admin(100, "Admin User")

admin.add_user(user1)
admin.add_user(user2)

print(f"Admin's user list: {[user.get_name() for user in admin._user_list]}")

admin.remove_user(user1)
print(f"Admin's user list after removing {user1.get_name()}: {[user.get_name() for user in admin._user_list]}")

