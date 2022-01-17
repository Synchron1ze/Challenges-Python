keypad = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " "
}


def numbers_to_message(pressed_sequence):
    message = ""
    key_previous = None
    key_pressed_count = 0
    capitalize = False
    for key_pressed in pressed_sequence:
        if key_pressed in range(2, 10):
            if key_pressed == key_previous:
                key_pressed_count += 1
                message = message[:-1]
            else:
                key_pressed_count = 1
                if key_previous != 1:
                    capitalize = False
            letter_to_print = keypad[key_pressed][(key_pressed_count - 1) % len(keypad[key_pressed])]
            if capitalize:
                letter_to_print = letter_to_print.capitalize()
            message += letter_to_print
        elif key_pressed == 1:
            capitalize = True
        elif key_pressed == 0:
            message += keypad[key_pressed]
        elif key_pressed == -1:
            key_pressed_count = 0
        else:
            return "Error: Invalid input"
        key_previous = key_pressed
        # print(f"{key_pressed:2d} -> {message}")
    return message


print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))

letters = {
    "a": [2],
    "b": [2, 2],
    "c": [2, 2, 2],
    "d": [3],
    "e": [3, 3],
    "f": [3, 3, 3],
    "g": [4],
    "h": [4, 4],
    "i": [4, 4, 4],
    "j": [5],
    "k": [5, 5],
    "l": [5, 5, 5],
    "m": [6],
    "n": [6, 6],
    "o": [6, 6, 6],
    "p": [7],
    "q": [7, 7],
    "r": [7, 7, 7],
    "s": [7, 7, 7, 7],
    "t": [8],
    "u": [8, 8],
    "v": [8, 8, 8],
    "w": [9],
    "x": [9, 9],
    "y": [9, 9, 9],
    "z": [9, 9, 9, 9],
    " ": [0],
}


def message_to_numbers(message):
    numbers_list = []
    letter_previous = ""
    for letter in message:
        if letter.lower() in letters:
            if letter.isupper():
                numbers_list.append(1)
            elif (letter_previous != "") and (letters[letter][0] == letters[letter_previous][0]):
                numbers_list.append(-1)
            numbers_list.extend(letters[letter.lower()])
        else:
            return "Error: Invalid input"
        letter_previous = letter.lower()
    return numbers_list


print(message_to_numbers("abc"))
print(message_to_numbers("a"))
print(message_to_numbers("Ivo e Panda"))
print(message_to_numbers("aabbcc"))
