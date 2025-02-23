def calculate_leds(number_to_calculate):
    weight = 0
    for char in number_to_calculate:
        if char in leds_by_number:
            weight += leds_by_number[char]
    return weight


leds_by_number = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "0": 6}

test_cases = int(input())

for _ in range(test_cases):
    number = input()
    leds_needed = calculate_leds(number)
    print(f"{leds_needed} leds")
