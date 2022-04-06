user_info = []

class User:
    def __init__(self, first_name, last_name, user_name, birthday, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.birthday = birthday
        self.password = password
        self.login_attempts = 0
    
    def describe_user (self):
        print(f"{self.first_name} {self.last_name}'s user name is {self.user_name} and their birthday is {self.birthday}.")

    def greet_user(self):
        print(f"Welcome {self.user_name}! Have an amazing day!")

    def increment_login_attempts(self, inputted_password):
        if self.password == inputted_password:
            print("Congratulations, you've logged in!")
        elif self.login_attempts < 3 and self.password != inputted_password:
            self.login_attempts += 1
            print(f"You have attempted to log in {self.login_attempts} times")
        else:
            print("You have failed logging in too many times")

    
    def reset_login_attempts(self):
        if self.login_attempts == 3:
            print("You're password attempts have been reset")
            self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, user_name, birthday, password):
        super().__init__(first_name, last_name, user_name, birthday, password)
        self.rights = Privelages()

class Privelages:
    def __init__(self):
        self.privelages = ["can add post", "can delete post", "can ban user"]

    def show_privelages(self):
        print(f"As an admin you are able to: {', '.join(self.privelages)}")

user_info.append(input("What is your first name? "))
user_info.append(input("What is your last name? "))
user_info.append(input("What user name do you want? "))
user_info.append(input("When is your birthday? "))
user_info.append(input("What do you want your password to be? "))

profile = User(*user_info)
profile.describe_user()
profile.greet_user()
# profile.increment_login_attempts(input("What is your password? "))
# profile.increment_login_attempts(input("What is your password? "))
# profile.increment_login_attempts(input("What is your password? "))
# profile.increment_login_attempts(input("What is your password? "))
# profile.reset_login_attempts()
admin_privelage = Admin(*user_info)
admin_privelage.rights.show_privelages()