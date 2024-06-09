class Building:
    def __init__(self,numberOfFloors,buildingType):
        if  not isinstance(numberOfFloors,int):
            raise TypeError("Значение должно быть числом")
        if  not isinstance(buildingType,str):
            raise TypeError("Значение должно быть строкой")
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)
    def __str__(self):
        return self.buildingType
    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors

haus_1 = Building(5,'Башня')
haus_2 = Building(6, 'Институт')
print(haus_1 == haus_2)
if haus_1 != haus_2:
    print('Это разные здания')
else:
    print("они равны")

    