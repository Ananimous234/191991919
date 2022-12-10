import random
class Human:
    def __init__(self, name = 'Human', job = None, car = None, home = None):
        self.name = name
        self.gladness = 50
        self.job = job
        self.home = home
        self.money = 200
        self.satiety = 50
        self.car = car
    def get_home(self):
        self.home = Home()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
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
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel....')
            self.money -= 50
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food....')
            self.money -= 20
            self.home.food += 20
        elif manage == 'delicacies':
            print('Happy!')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def clean_home(self):
        self.home.mess = 0
        self.gladness -= 5
    def to_repair(self):
        self.money -= 50
        self.car.strenght += 100
    def days_indexes(self, day):
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
        print(f'Strenght - {self.car.strenght}')
        print(f'Fuel - {self.car.fuel}')
    def is_alive(self):
        if self.gladness <= 0:
            print('Depression')
            return False
        if self.money <= 100:
            print('Bancrot')
            return False
        if self.satiety <= 0:
            print('Dead')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
            print('Settled in the Home')
        if self.car is None:
            self.get_car()
            print(f'I bought a car {self.car.brand}')
        if self.work is None:
            self.get_job()
            print(f'I am going to get a job {self.job.job} with salary {self.job.salary}')
        self.days_indexes(day)
        dice =  random.randint(1,4)
        if self.satiety < 20:
            print("Time to eat")
            self.eat()
        elif self.gladness:
            if self.home.mess > 15:
                print("I want to chill, but there so messy")
                self.clean.home()
            else:
               print("Let's Chill!")
               self.chill()
        elif self.money < 10:
            print("Start the work")
            self.work()
        elif self.car.strenght < 10:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Time to work")
            self.work()
        elif dice == 3:
            print("Time to clean home")
            self.clean_home()
        elif dice == 4:
            print("Time shopping")
            self.shopping(manage = "delicacies")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strenght']
        self.consumption = brand_list[self.brand]['consumption']
    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.strenght -= 1
            self.fuel -= self.consumption
            return True
        else:
            print('The car cannot move!')
            return False
class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self):
      self.job = random.choice(list(job_list))

job_list = {"C++":{'salary': 70, 'job_gladness': 5,},
           "Java": {'salary': 65, 'job_gladness': 4,},
           "Python": {'salary': 60, 'job_gladness': 7,},
           "PHP": {'salary': 50, 'job_gladness': 3,}}
brands_of_car = {"BMW":{'fuel': 70, 'strenght': 6, 'consumption': 5,},
                "LADA": {'fuel': 60, 'strenght': 4, 'consumption': 4,},
                "VOLVO": {'fuel': 80, 'strenght': 7, 'consumption': 6,},
                "SUBARU": {'fuel': 90, 'strenght': 4, 'consumption': 7,}}

sasha = Human(name = "Sasha")
for day in range(1,8):
    if sasha.live(day) == False:
        break