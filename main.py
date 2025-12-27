test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}

def add_setting(dic_settings, key_value_pair):
    key, value = key_value_pair
    key = key.lower()
    value = value.lower()

    if key in dic_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dic_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dic_settings, key_value_pair):
    key, value = key_value_pair
    key = key.lower()
    value = value.lower()

    if key in dic_settings:
        dic_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dic_settings, key):
    key = key.lower()

    if key in dic_settings:
        del dic_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(dic_settings):
    if not dic_settings:
        return "No settings available."

    output = "Current User Settings:\n"
    for key, value in dic_settings.items():
        output += f"{key.capitalize()}: {value}\n"

    return output
