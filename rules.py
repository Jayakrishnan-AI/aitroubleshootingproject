rules = [

    # Computer Power Problems
    {
        "conditions": ["computer_not_turning_on", "battery_dead"],
        "solution": "Charge the battery."
    },
    {
        "conditions": ["computer_not_turning_on", "charger_not_connected"],
        "solution": "Connect the charger properly."
    },
    {
        "conditions": ["computer_not_turning_on", "power_button_fault"],
        "solution": "Check the power button or motherboard."
    },

    # WiFi Problems
    {
        "conditions": ["wifi_not_working", "router_off"],
        "solution": "Turn on the router."
    },
    {
        "conditions": ["wifi_not_working", "router_no_internet"],
        "solution": "Restart the router."
    },
    {
        "conditions": ["wifi_not_working", "wrong_wifi_password"],
        "solution": "Enter the correct WiFi password."
    },

    # Printer Problems
    {
        "conditions": ["printer_not_printing", "ink_empty"],
        "solution": "Refill the printer ink."
    },
    {
        "conditions": ["printer_not_printing", "paper_jam"],
        "solution": "Remove the jammed paper."
    },

    # Overheating
    {
        "conditions": ["computer_overheating", "fan_not_working"],
        "solution": "Clean or replace the cooling fan."
    },

    # Slow Computer
    {
        "conditions": ["computer_slow", "many_background_apps"],
        "solution": "Close unnecessary background applications."
    },

]