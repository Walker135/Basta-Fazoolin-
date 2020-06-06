class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


class Franchises:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return 'This franchises is located at: ' + self.address
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return 'The ' + self.name + ' menu is available between ' + str(self.start_time) + ' and ' + str(self.end_time) +'.'

  def calculate_bill(self, purchased_items):
    total = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        total += self.items[purchased_item]
    return total

# Menu items - Basta Fazoolin
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00,          'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

# Menu items - Take a' Arepa
arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}


# Menus - Basta Fazoolin
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

early_bird_menu = Menu('Early bird', early_bird_items, 1500, 1800)

dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

kids_menu = Menu('Kids', kids_items, 1100, 2100)

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# Menus - Take a' Arepa
arepas_menu = Menu("Take a' Arepa", arepa_items, 1000, 2000)


# Franchises - Basta Fazoolin
flagship_store = Franchises('1232 West End Road', menus)

new_installment = Franchises('12 East Mulberry Street', menus)

# Franchises - Take a' Arepa
arepas_place = Franchises('189 Fitzgerald Avenue', [arepas_menu])


# Business
Basta_Fazoolin_with_my_Heart = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

take_a_arepa = Business("Take a' Arepa", [arepas_place])


