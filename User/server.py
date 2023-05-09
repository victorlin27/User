class User:

    def __init__(self,first_name,last_name,email,age) :
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name,self.last_name,self.email,self.age,self.is_rewards_member,self.gold_card_points)
        return self
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self,amount):
        self.gold_card_points -= amount
        return self

victor = User('Victor','Lin','victorflin@gmail.com',19,)
tan = User('Tan', 'Doan', 'tdoan@gmail.com', 19)
tommy = User('Tommy', 'Chen', 'tchen@gmail.com', 19)

victor.enroll()
victor.spend_points(50)
victor.display_info()
tan.enroll()
tan.spend_points(80)
tan.display_info()
tommy.display_info()