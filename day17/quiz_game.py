class User: 
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.hands = 2
        self.followers = 0
        self.folling = 0
    def become_pirate(self):
        self.hands = 1

    def follow(self, user):
        user.followers +=1
        self.following +=1


user_1 = User("jack" , 1)
# using OOP


 