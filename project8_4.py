class Warehouse:
    def __init__(self, division, quantity):
        self.division = division
        self.quantity = quantity
        self.items = []

    def admission_to_the_warehouse(self, OfficeEquipment):

        try:
            self.items.append({'Модель': OfficeEquipment.name, 'Количество': int(self.quantity)})
            print(f'Принято {OfficeEquipment.name} в количестве {self.quantity} в подразделение {self.division}')
        except:
            print('Количество должно быть числовым значением')


class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class printer(OfficeEquipment):
    def __init__(self, printing_technology, speed_print, name):
        super().__init__(name)
        self.printing_technology = printing_technology
        self.speed_print = speed_print


class Scaner(OfficeEquipment):
    def __init__(self, scanning_technology, dpi, name):
        super().__init__(name)
        self.scanning_technology = scanning_technology
        self.dpi = dpi


class Xerox(OfficeEquipment):
    def __init__(self, num_copy, scaling, name):
        super().__init__(name)
        self.num_copy = num_copy
        self.scaling = scaling


office_equipment = OfficeEquipment('HP')
ware = Warehouse('Бухгалтерия', '1')
ware.admission_to_the_warehouse(office_equipment)
