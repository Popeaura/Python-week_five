# Parent Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand              # Instance variable
        self.model = model              # Instance variable
        self.battery_life = battery_life  # Instance variable

    def call(self):
        print(f"{self.brand} {self.model} is making a call.")

    def battery_status(self):
        print(f"{self.brand} {self.model} has {self.battery_life}% battery remaining.")

# Child Class: SmartphoneWithCamera (Inheritance)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life) 
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels} MP camera!")

# Creating Objects
phone1 = Smartphone("Samsung", "Galaxy S23", 85)
phone2 = SmartphoneWithCamera("iPhone", "14 Pro", 90, 48)

# Using Methods
phone1.call()               
phone1.battery_status()           

phone2.call()                         
phone2.take_photo()                   
phone2.battery_status()               
