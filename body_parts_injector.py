""" This tool adds special parts in time of characters creation
 You could choose amount of characters with specials"""


import random
from category_builder import notes, opttas, texts


def inject_body_parts(characters, parts, count=None):
    """ Add optional parts in character.

        Without argument "count" all characters get a part.

        Returns updated characters.
    """
    if count is None:
        count = len(characters)

    if count > len(characters):
        count = len(characters) // 2

    if parts == notes:
        n = 0
        while n < 2000:
            b = 0
            character = (random.sample(characters, 1))[0]
            random_parts = (random.sample(parts, 1))[0]
            if random_parts == 'note_36':
                if 'note_pface' in character:
                    b += 1
                if 'note_36' in character:
                    b += 1
                if 'lid_6_up' in character:
                    b += 1
                if 'lid_3_hat60x' in character:
                    b += 1
                if 'lid_4_hat60x_cut' in character:
                    b += 1
                if b == 0:
                    character.append(random_parts)
                    n += 1
                if n == count:
                    break
            elif random_parts == 'note_pface':
                if 'note_pface' in character:
                    b += 1
                if 'note_36' in character:
                    b += 1
                if 'lid_3_hat60x' in character:
                    b += 1
                if 'lid_4_hat60x_cut' in character:
                    b += 1
                if b == 0:
                    character.append(random_parts)
                    n += 1
                if n == count:
                    break
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
                    if 'opttas_question' in random_characters:
                        break
                    part = random_characters[pointer]
                    if 'cream_' in part:
                        random_characters.remove(part)
                    elif 'top_' in part:
                        random_characters.remove(part)
                    else:
                        pointer += 1
                    if pointer == len(random_characters):
                        random_characters.append(random_parts)
                        n += 1
                        break
            elif random_parts == 'opttas_tubule':
                match = 0
                while True:
                    if 'opttas_tubule' in random_characters:
                        break
                    elif 'opttas_question' in random_characters:
                        break
                    if 'lid_6_up' in random_characters:
                        match += 1
                    if 'cream_5_marshmallow' in random_characters:
                        match += 1
                    if match == 2:
                        if 'top_bubs' in random_characters:
                            random_characters.remove('top_bubs')
                        if 'top_pills_happy' in random_characters:
                            random_characters.remove('top_pills_happy')
                        random_characters.append(random_parts)
                        n += 1
                        break
                    else:
                        break
    else:
        random_characters = random.sample(characters, count)
        for character in random_characters:
            random_parts = (random.sample(parts, 1))[0]
            character.append(random_parts)
    return characters
