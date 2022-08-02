def clean_it_pass(characters):
    part = 'it_pass'
    for character in characters:
        if part in character:
            character.remove(part)
