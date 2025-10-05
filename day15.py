# 17/09/25
# ------ # -------------$$$$$--------------- # -------
# -->>  why use parameter ? --> to pass the argument --> 

'''class New:
    print('hiii')'''
    

# Variable
# class variable // only belongs to class 
'''class Pubg:
    playername='cr7'
    print(playername)
#----> access outside the class --> create a object, then call the object --> object_name.class_var
obj=Pubg()
print(obj.playername)'''

# instance variable
'''class Realme:
    name='realme9se'
    def __init__(self): # without calling this fn execute first // by default it pass address of all instance method // self store an address of object // if not pass --> positional argument error
        # model='oneee' # Normal variable
        self.model='ONe' # instance variable
        self.name='abc' # overwrite the 'name'
        self.price=100000 # instance variable
        # print(self.model) # output: ONe
        # print(self.name)  # output: abc
        # print(model) # output : oneee
    # print(model) # output: abc // outside the instance method its not possible to access instance variable
    # print(name) # output: abc // outside the instance method its possible to access class variable


obj=Realme() # object creation
# outside the class we can access both class and instance variables
print(obj.name)
# print(obj.model)
# print(obj.price)
# obj1=Realme()'''


# object creation
'''
    1. __new__()  // method execute // creating the address of object
    2. __init__() // constructor --> without call it's execute --> init. the instance variable
    3. 
'''

'''class game:
    def __init__(self,g_name,g_size,g_duration,g_type):
        self.g_name=g_name
        self.g_size=g_size
        self.g_duration=g_duration
        # self.g_type=g_type
        g_type=g_type
        # print(self.g_duration)
        # print(self.g_name)
        # print(self.g_type)
    def details(self):
        print(self.g_duration)
        print(self.g_name)
        # print(self.g_type) // not possible to access why ? -->> (g_type not an attribute its just a normal variable)
pubg=game('pubg','8-gb','45 min','battle ground(survival)')
# print(pubg.g_name)
# print(pubg.g_duration)
# print(pubg.g_type)
# print(pubg.g_size)
pubg.details()'''


# -------------------------------------------------------------------------------------------------
# ---------------------> pillers of opps <-----------------------
'''
    1.Encapsulation
    2.Inheritance
    3.Polymorphism
    4.Abstraction
'''
# ------------->> Encapsulation <------------------  
'''
    - binding the data members(attributes) into a single unit with the help of (private, public, protected)
    - private can access by using getter and setter methods
    - 
'''

'''scenario: 
    1. create a user
        u_name(input form user)
        u_id(input form user)
        u_mobile(input form user)
        follower count(assign 0)
        following count(assign 0)
        
    2. Display the user details
    3. follow & unfollow
'''
class instagram:
    def __init__(self,u_name,u_id,u_mobile):
        self.u_name=u_name
        self.u_id=u_id
        self.u_mobile=u_mobile
        self.follower_count=0
        self.following_count=0
    def display(self):
        print(self.u_name)
        print(self.u_id)
        print(self.u_mobile)
        print(self.follower_count)
        print(self.following_count)

obj=instagram('suman','suman_z','9535925470')
obj1=instagram('sum','sum_z','00000000000')
print(f'user id: {obj.u_id}, user name: {obj.u_name}, user mobile: {obj.u_mobile}, follower: {obj.follower_count}, following: {obj.following_count}')
print(f'user1 id: {obj1.u_id}, user1 name: {obj1.u_name}, user1 mobile: {obj1.u_mobile}, user 1follower: {obj1.follower_count}, user1 following: {obj1.following_count}')


'''
    scenario 1(snap):
        1. create a user
            u_id
            u_name
            date_join
            u_points
            bff
            z_sign
        2. display
    scenario 2(wh):
        1. create a user
            u_ph
            u_name
            u_status
            n_bio
            status
            status_like
            unread_message
            channel
        2. display
    scenario 3(discord):
        1. create a user
            u_id
            u_mail
            u_name
            u_symbol
            date_join
            number_of_server_join
            own_server
            friends
        2. display
    scenario 4(faceb):
        1. create a user
            u_id
            u_name
            date_join
            u_status
            u_friends
            u_group
            u_following
        2. display
    scenario 5(youtube):
        1. create a user
            u_chanal_name
            u_name
            date_join
            subscribers
            views
            no_of_videos
            no_of_likes
            no_of_comments
        2. display
'''


# assignment all the basic concept -->> waht is python to function