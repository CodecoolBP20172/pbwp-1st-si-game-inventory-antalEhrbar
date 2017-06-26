import sys


def display_inventory(inventory):
    
    print('Inventory:')
    for k, v in inventory:
        print (k, '', v)
    print(('Total number of items:'), sum(inventory.values()))


def add_to_inventory(inventory, added_items):
    
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i: 1})
    return inventory


def print_table(inventory, order=None):
   
    list_sorted = []
    i_value = 0
    i_item = 0

    for key in inventory.keys():
        if len(key) > i_item:
            i_item = len(key)
        if len(str(inventory[key])) > i_value:
            i_value = len(str(inventory[key]))
        for k, v in inventory.items():
            sorted_list.append([k, v])
    i_item += 4  # To make a better layout on output
    i_value += 4

    if order == "count,asc":
        list_sorted.sort()
    elif order == "count,desc":
        list_sorted.sort(reverse=True)

    print("Inventory:")
    print("{}{}".format("count".rjust(i_value), "item name".rjust(i_item)))
    print("-" * (i_value + i_item))

    for i in list_sorted:
        print("{}{}".format(str(i[0]).rjust(i_value), i[1].rjust(i_item)))

    print("-" * (i_value + i_item))
    print("Total number of items: ", sum(inventory.values()))


def import_inventory(inventory, filename="import_inventory.csv"):
  
    i_inventory = ""
    try:
        with open(sys.path[0] + '/' + filename, "r") as f:  # Not a csv reader it will fail at item names with ','
            i_inventory = f.read().split(",")
    except FileNotFoundError:
        print("The file is missing.")

    inventory = add_to_inventory(inventory, i_inventory)
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    export_inv = []
    for key in inventory:
        for value in range(inventory.get(key)):
            export_inv.append(key)
    export_inv = ",".join(export_inv)
    try:
        with open(filename, "w") as f:
            f.write(export_inv)
    except FileNotFoundError:
        print("You're looking for the wrong file. Try again.")


    return inventory