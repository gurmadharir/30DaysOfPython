
# 💻 Day 12 – Modules Exercises (Python)

## 📘 Level 1

1. **Write a function which generates a six-digit/character random user ID.**  

   ```
   print(random_user_id()) 
   # Example output:
   # '1ee33d'
   ````

2. **Modify the previous task.** Declare a function named `user_id_gen_by_user`. It doesn’t take any parameters but takes two inputs using `input()`:
   * Number of characters per ID
   * Number of IDs to generate

   ```
   print(user_id_gen_by_user()) 
   # Example user input: 5 5
   # Example output:
   # kcsy2
   # SMFYb
   # bWmeq
   # ZXOYh
   # 2Rgxf
   ```

   ```
   print(user_id_gen_by_user()) 
   # Example user input: 16 5
   # Example output:
   # 1GCSgPLMaBAVQZ26
   # YD7eFwNQKNs7qXaT
   # ycArC5yrRupyG00S
   # UbGxOFI7UXSWAyKN
   # dIV0SSUTgAdKwStr
   ```

3. Write a function named `rgb_color_gen`. **It will generate RGB colors with 3 values ranging from 0 to 255 each.**
   ```
   print(rgb_color_gen())
   # Example output:
   # rgb(125,244,255)
   ```

## 📗 Level 2
1. Write a function `list_of_hexa_colors` which **returns any number of hexadecimal** in an array.
   * Each color is six hexadecimal digits written after `#`.
   * Hexadecimal numeral system: 0-9 and a-f.


2. Write a function `list_of_rgb_colors` which **returns any number of RGB colors** in an array.

3. Write a function `generate_colors` which can generate any number of **hexa** or **RGB** colors.
   ```
   generate_colors('hexa', 3)  # Example: ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1)  # Example: ['#b334ef']
   generate_colors('rgb', 3)   # Example: ['rgb(5,55,175)','rgb(50,105,100)','rgb(15,26,80)'] 
   generate_colors('rgb', 1)   # Example: ['rgb(33,79,176)']
   ```

## 📕 Level 3

1. Call your function `shuffle_list`. It takes a list as a parameter and **returns a shuffled list.**

2. Write a function which returns an array of seven random numbers in the range 0–9. All the numbers must be **unique**.


---
**Gurmad Harir**  
January 26, 2026.
