# create user, search friends, add/delete friends

class User:
    # user attributes
    def __init__(self, user_name, user_id, user_password):
        self.name = user_name
        self.id = user_id
        self.user_password = user_password
        self.connections = []

    def change_user_name(self, user_name):
        self.name = user_name

    def change_user_id(self, user_id):
        self.id = user_id

    def add_connections(self, user_connections):
        self.connections.append(user_connections)

    def remove_connections(self, user_connections):
        self.connections.remove(user_connections)

    def change_user_password(self, user_password):
        self.user_password = user_password

class Network:
    # network attributes
    # add, remove, check, form friendships
    def __init__(self):
        self.user_list = []

    def check_existing_user(self, check_user):
        for i in self.user_list:
            if check_user == self.user_list[i]:
                return True
        return False

    def accept_connections(self, user_accepting, user_requesting):
        user_accepting.add_connections(user_requesting)
        user_accepting.connections.append(user_requesting)

    def add_user(self, new_user):
        self.user_list.append(new_user)

    def delete_user(self, remove_user):
        self.user_list.remove(remove_user)


def main():
    my_network = Network()

    user_1 = User("Friend_1", "Person 1", "password")
    my_network.add_user(user_1)

    user_2 = User("Friend_2", "Person 2", "password")
    my_network.add_user(user_2)

    user_3 = User("Friend_3", "Person 3", "password")
    my_network.add_user(user_3)

    creating = True
    num_loops = 0

    print("Welcome, user!  Please create an account first.")
    main_username = input("username: ")
    main_password = input("password: ")
    main_user_id = input("screen name: ")

    main_user = User(main_username, main_user_id, main_password)

    print("\nWelcome to the network, " + main_user.id + "!")

    while creating:
        if num_loops == 0:
            print("Type in 'c' to create a new user and add them to the network.")
            print("Type in 'f' to add a friend.")
            print("Type in 'exit' to exit.")
            print("Type in 'friend's list' to display your friend's list.")
            print("Type in 'user list' to display the list of users that currently exist on this network.")
            print("Type in 'i' for this set of instructions again.")

        action = input("What would you like to do?\n")
        action = action.lower()

        if action == "c":
            username = input("username: ")
            password = input("password: ")
            user_id = input("screen name: ")
            print()

            new_user = User(username, user_id, password)
            my_network.add_user(new_user)

        elif action == "i":
            print("Type in 'c' to create a new user and add them to the network.")
            print("Type in 'f' to add a friend.")
            print("Type in 'del' to exit.")
            print("Type in 'friend's list' to display your friend's list.")
            print("Type in 'user list' to display the list of users on this network.")
            print("Type in 'i' for this set of instructions again.")
            print()

        elif action == "f":
            add_friend = input("What is your friend's screen name?")
            add_friend = add_friend.lower()
            if my_network.check_existing_user(add_friend):
                print(add_friend + " has been successfully added!")

            else:
                print("This user is not on this network.")

        elif action == "exit":
            break

        elif action == "user list":
            # print list of users
            print()
            print("List of users:")
            for i in my_network.user_list:
                print(i.name)
            print()

        else:
            print("Please select a valid action to do, or type in 'i' to see the directions again.")
            print()

        num_loops += 1

main()
