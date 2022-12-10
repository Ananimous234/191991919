import random
class Human:
    def __init__(self, name = 'Human', job = None, car = None):
        self.name = name
        self.gladness = 50
        self.job = job
        self.home = Home
        self.money = 100
        self.satiety = 50
    def get_home(self):
        self.home = Home()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_retair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety +=5

    def work(self):
        if self.car.drive():
            pass
        else:
          self.to_repair()
          return
        self.money += self.job.salary
        self.gladness += self.job.gladness
        self.satiety -=5

    def chill(self):
        self.gladness += 15
        self.home.mess += 5
    def shopping(self):
        pass
    def clean_home(self):
        self.home.mess = 0
        self.gladness -= 5
    def to_repair(self):
        self.money -= 50
        self.car.strenght += 100
    def days_indexes(self):
        day = f"Today th {day} of {self.name}'s life: "
        print(f'{day:=^50}', "\n")
        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:=^50}', "\n")
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexes = 'Home indexes'
        print(f'{"Home indexes":=^50}', "\n")
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        car_indexes = f'{self.car.brand} car indexes'
        print(f'{"car_indexes":=^50}', "\n")
        print(f'Strength - {self.car.strenght}')
        print(f'Fuel - {self.car.fuel}')
    def is_alive(self):
        pass
    def life(self):
        pass




class Auto:
   def __init__(self, brand_list):
       self.brand = random.choice(list(brand_list))
   def drive(self):
       pass




class Home:
    pass
class Job:
    def __init__(self):
      self.job = random.choice(list(job_list))

job_list = {"C++":{'salary': 70, 'job_gladness': 5,},
           "Java": {'salary': 65, 'job_gladness': 4,},
           "Python": {'salary': 60, 'job_gladness': 7,},
           "PHP": {'salary': 50, 'job_gladness': 3,}}
brands_of_car = {"BMW":{'fuel': 70, 'strenght': 6, 'consumption': 5,},
                "LADA": {'fuel': 60, 'strength': 4, 'consumption': 4,},
                "VOLVO": {'fuel': 80, 'strenght': 7, 'consumption': 6,},
                "SUBARU": {'fuel': 90, 'strenght': 4, 'consumption': 7,}