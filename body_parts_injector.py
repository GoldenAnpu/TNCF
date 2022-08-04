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
            random_parts = (random.sample(parts, 1))[0]
            if random_parts == 'note_36':
                if 'lid_6_up' in random_characters:
                    break
                if 'lid_3_hat60x' in random_characters:
                    break
                if 'lid_4_hat60x_cut' in random_characters:
                    break
                random_characters.append(random_parts)
                n += 1
            elif random_parts == 'note_pface':
                if 'lid_3_hat60x' in random_characters:
                    break
                if 'lid_4_hat60x_cut' in random_characters:
                    break
                random_characters.append(random_parts)
                n += 1
    elif parts is texts:
        n = 0
        while n != count:
            random_characters = (random.sample(characters, 1))[0]
            random_parts = (random.sample(parts, 1))[0]
            give = 0
            if random_parts not in random_characters:
                if 'glasses' in random_characters:
                    give += 1
                if 'eyes_6_hypno_glasses' in random_characters:
                    give += 1
                if 'eyes_7_sq_g_glasses' in random_characters:
                    give += 1
                if give == 0:
                    random_characters.append(random_parts)
                    n += 1
            else:
                break
    elif parts is opttas:
        n = 0
        while n != count:
            random_characters = (random.sample(characters, 1))[0]
            random_parts = (random.sample(parts, 1))[0]
            if random_parts == 'opttas_question':
                pointer = 0
                while True:
                    if 'opttas_tubule' in random_characters:
                        break
                    elif 'opttas_question' in random_characters:
                        break
                    else:
                        part = random_characters[pointer]
                        if 'cream_' in part:
                            random_characters.remove(part)
                        elif 'top_' in part:
                            random_characters.remove(part)
                        else:
                            pointer += 1
                        if pointer == len(random_characters):
                            break
                    random_characters.append(random_parts)
                    n += 1
                    break
            elif random_parts == 'opttas_tubule':
                pointer = 0
                match = 0
                while True:
                    if 'opttas_tubule' in random_characters:
                        break
                    elif 'opttas_question' in random_characters:
                        break
                    else:
                        if pointer == len(random_characters):
                            break
                        part = random_characters[pointer]
                        if part == 'top_bubs':
                            break
                        elif part == 'lid_6_up':
                            match += 1
                        elif part == 'cream_5_marshmallow':
                            match += 1
                        if match == 2:
                            random_characters.append(random_parts)
                            n += 1
                            break
                        pointer += 1
    else:
        random_characters = random.sample(characters, count)
        for character in random_characters:
            random_parts = (random.sample(parts, 1))[0]
            character.append(random_parts)
    return characters
