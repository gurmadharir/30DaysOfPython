# =====================================================
# Day 12: Modules
# =====================================================
import random
import secrets
import string

# --------------------- Level 1 -----------------------

#1. Write a function to generate a 6-character random ID.
def random_user_id():
    return secrets.token_hex(3)

print(random_user_id())

#2. Modify: Generate user IDs using user input.
def user_id_gen_by_user():
    try:
        num_chars = int(input("How many characters would you like to generate? "))
        num_ids = int(input("How many ids would you like? "))
    except ValueError:
        print("Please enter numbers only.")
        return

    chars = string.ascii_letters + string.digits

    for _ in range(num_ids):
        user_id = ''.join(secrets.choice(chars) for _ in range(num_chars))
        print(user_id)

user_id_gen_by_user()

#3. Generate an RGB color with 3 values (0–255).
def rgb_color_gen():
    r,g,b = [random.randint(0, 255) for _ in range(3)]
    print(f"rgb({r},{g},{b})")

rgb_color_gen()

# --------------------------  Level 2 -------------------------------

#1. Return a list of hex colors with 6 digits each.
def list_of_hexa_colors(n):
    hex_chars = '0123456789abcdef'
    colors = []

    for _ in range(n):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)

    return colors

# Example usage:
print(list_of_hexa_colors(5))  # Returns a list of 5 random hex colors

#2. Returns a list of RGB colors
def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        r,g,b = [random.randint(0, 255) for _ in range(3)]
        rgb_colors.append((r,g,b))

    return rgb_colors

print(list_of_rgb_colors(5))

#3. Generates a list of n colors in 'hexa' or 'rgb' format.
def generate_colors(type, n):
    colors = []

    if type == 'hexa':
        hex_chars = '0123456789abcdef'
        for _ in range(n):
            color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
            colors.append(color)
    elif type == 'rgb':
        for _ in range(n):
            color = f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"
            colors.append(color)
    else:
        raise ValueError("Color type must be 'hexa' or 'rgb'")

    return colors


# Examples
print(generate_colors('hexa', 3))  # ['#a3e12f', '#03ed55', '#eb3d2b']
print(generate_colors('rgb', 3))  # ['rgb(5,55,175)', 'rgb(50,105,100)', 'rgb(15,26,80)']


# ------------------------- Level 3 -----------------------------

#1. Returns a shuffled list
def shuffle_list(array):
    random.shuffle(array)
    return array

print(shuffle_list([1,2,3,4,5,6]))

#2. Returns a list of 7 unique random numbers from 0 to 9
def unique_numbers():
    return random.sample(range(10), 7)

print(unique_numbers())