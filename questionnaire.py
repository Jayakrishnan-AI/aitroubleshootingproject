def ask_questions():

    conditions = []

    power = input("Is the computer not turning on? (yes/no): ")
    if power.lower() == "yes":
        conditions.append("computer_not_turning_on")

        battery = input("Is the battery dead? (yes/no): ")
        if battery.lower() == "yes":
            conditions.append("battery_dead")

        charger = input("Is the charger connected? (yes/no): ")
        if charger.lower() == "no":
            conditions.append("charger_not_connected")

    wifi = input("Is WiFi not working? (yes/no): ")
    if wifi.lower() == "yes":
        conditions.append("wifi_not_working")

        router = input("Is the router turned off? (yes/no): ")
        if router.lower() == "yes":
            conditions.append("router_off")

    printer = input("Is the printer not printing? (yes/no): ")
    if printer.lower() == "yes":
        conditions.append("printer_not_printing")

        ink = input("Is the ink empty? (yes/no): ")
        if ink.lower() == "yes":
            conditions.append("ink_empty")

    return conditions