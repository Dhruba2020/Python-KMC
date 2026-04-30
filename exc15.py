class Account:
    def __init__(self, acc_no, balance):
        self.account_number = acc_no
        self.balance = balance
        self.history = []   

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account: {self.account_number}, Balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, acc_no, balance, rate):
        super().__init__(acc_no, balance)
        self.interest_rate = rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.history.append(f"Interest added: {interest}")


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, acc_no, balance, rate, points):
        super().__init__(acc_no, balance, rate)
        self.reward_points = points

    def redeem_points(self):
        print("Redeemed points:", self.reward_points)
        self.reward_points = 0

   
    def withdraw(self, amount):
        if self.balance - amount < 100:   # minimum balance
            print("Minimum balance must be 100")
        else:
            super().withdraw(amount)



obj = PremiumSavingsAccount("A101", 1000, 10, 50)

obj.deposit(500)
obj.withdraw(300)
obj.add_interest()
obj.redeem_points()

print(obj)
print("History:", obj.history)



#..............................................
class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        print("Device ON")

    def turn_off(self):
        self.status = "OFF"
        print("Device OFF")

    def __str__(self):
        return f"Device: {self.device_id}, Status: {self.status}"


class SmartDevice(Device):
    def __init__(self, device_id, connectivity):
        super().__init__(device_id)
        self.connectivity = connectivity

    def connect(self):
        print("Connected via", self.connectivity)


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, connectivity, temp):
        super().__init__(device_id, connectivity)
        self.temperature = temp
        self.mode = "Normal"

    def set_temperature(self, temp):
        try:
            if temp < 0 or temp > 50:
                raise ValueError("Invalid temperature")
            self.temperature = temp
            print("Temperature set to", temp)
        except:
            print("Error: Invalid temperature")

   
    def turn_on(self):
        super().turn_on()
        print("Thermostat starting...")


obj = SmartThermostat("D101", "WiFi", 25)

obj.turn_on()
obj.connect()
obj.set_temperature(30)
obj.set_temperature(100)

print(obj)



#..........................................
class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def attack(self):
        print(self.name, "does basic attack")

    def level_up(self):
        self.level += 1
        print(self.name, "leveled up!")

    def __str__(self):
        return f"{self.name}, Health: {self.health}, Level: {self.level}"


class Warrior(Character):
    def __init__(self, name, health, level, strength):
        super().__init__(name, health, level)
        self.strength = strength

    def heavy_attack(self):
        damage = self.strength * 2
        print("Heavy attack damage:", damage)


class EliteWarrior(Warrior):
    def __init__(self, name, health, level, strength, armor):
        super().__init__(name, health, level, strength)
        self.armor = armor
        self.rage_meter = 0

    def ultimate_attack(self):
        if self.rage_meter >= 50:
            print("Ultimate attack!")
            self.rage_meter = 0
        else:
            print("Not enough rage")

  
    def attack(self):
        damage = self.strength + 5
        self.rage_meter += 10
        print("Elite attack damage:", damage)
        print("Rage:", self.rage_meter)



obj = EliteWarrior("Hero", 100, 1, 20, 10)

obj.attack()
obj.attack()
obj.heavy_attack()
obj.ultimate_attack()

print(obj)


