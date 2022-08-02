import random
from category_builder import notes, opttas, texts


def inject_body_parts(characters, parts, count=None):
    """ADD OPTIONAL PARTS IN CHARACTERS

    Without argument count all characters get part.
    """
    if count is None:
        count = len(characters)

    if count > len(characters):
        count = len(characters) // 2

    if parts is notes:
        n = 0
        while n != count:
            random_characters = (random.sample(characters, 1))[0]
            random_parts = random.sample(parts, 1)
            if random_parts[0] in random_characters:
                break
            if 'note_36' in random_parts and 'lid_6_up' in random_characters:
                pass
            elif 'note_36' in random_parts and 'lid_3_hat60x' in random_characters:
                pass
            elif 'note_36' in random_parts and 'lid_4_hat60x_cut' in random_characters:
                pass
            elif 'note_pface' in random_parts and 'lid_3_hat60x' in random_characters:
                pass
            elif 'note_pface' in random_parts and 'lid_4_hat60x_cut' in random_characters:
                pass
            random_characters.append(random_parts[0])
            n += 1
    elif parts is texts:
        n = 0
        while n != count:
            random_characters = (random.sample(characters, 1))[0]
            random_parts = random.sample(parts, 1)
            if random_parts[0] in random_characters:
                break
            elif 'glasses' in random_characters:
                break
            elif 'eyes_6_hypno_glasses' in random_characters:
                break
            elif 'eyes_7_sq_g_glasses' in random_characters:
                break
            random_characters.append(random_parts[0])
            n += 1
    elif parts is opttas:
        n = 0
        while n != count:
            random_characters = (random.sample(characters, 1))[0]
            random_parts = random.sample(parts, 1)
            if random_parts[0] == 'opttas_question':
                pointer = 0
                while True:
                    part = random_characters[pointer]
                    if part == 'opttas_question':
                        break
                    if 'cream_' in part or 'top_' in part:
                        random_characters.remove(part)
                    else:
                        pointer += 1
                    if pointer == len(random_characters):
                        break
                random_characters.append(random_parts[0])
                n += 1
            elif random_parts[0] == 'opttas_tubule':
                pointer = 0
                match = 0
                while True:
                    part = random_characters[pointer]
                    if part == 'lid_6_up':
                        match += 1
                        pointer += 1
                    elif part == 'cream_5_marshmallow':
                        match += 1
                        pointer += 1
                    elif part == 'top_bubs':
                        match += 1
                        pointer += 1
                    elif part == 'opttas_question':
                        break
                    else:
                        pointer += 1
                    if match == 3:
                        n += 1
                        random_characters.append(random_parts[0])
                        break
                    elif pointer == len(random_characters):
                        break
    else:
        random_characters = random.sample(characters, count)
        for character in random_characters:
            random_parts = random.sample(parts, 1)
            character.append(random_parts[0])
    return characters
