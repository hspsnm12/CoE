def update_menu(menu, add_item, remove_item):
    if add_item not in menu:
        menu.append(add_item)
    if remove_item in menu:
        menu.remove(remove_item)
    return menu

def check_availability(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

updated_menu = update_menu(initial_menu, add_item, remove_item)
availability = check_availability(updated_menu, check_item)

print(f"Updated menu: {updated_menu}")
print(f"Availability: {availability}")
