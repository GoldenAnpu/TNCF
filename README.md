# Randomly generated 3D collection

<img src="https://ipfs.io/ipfs/bafybeifdc7e5c6religh24yfhgy5ullhbqhka6vmjjtf3ev7hqixhuanly" width="810" alt="">

### [You could see results on Rarible](https://rarible.com/tinycafe)

<img src="https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWZ3c3RtdzI3NnM0Z2huazZwbWFzanY1dTVjeWFma3p0aTZxYWM2dnRweGdhbnRkYW9zNXUvaW1hZ2Uud2VicA==" height="200" alt="">
<img src="https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWJpNXh6eGs2aGV2ZDRwaHdxNnRwcWFnNGNqbDJlN3FwaGh4YnFiNG1qYmF6eW1sc3U0dWUvaW1hZ2Uud2VicA==" height="200" alt="">
<img src="https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWg1amZnZG5xN3NhYnU3bzdpZ2F4aWEzNXhzemZzZ3RzdnUyc2hoY2liYjNheDVyb2Zza3EvaW1hZ2Uud2VicA==" height="200" alt="">
<img src="https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWNreGl4a2tyZmduaWp0aG9xd3RuenVzYmR4Z2Z5NTZzNDNtdG02MmE0bHdlYnZyajN2dXkvaW1hZ2Uud2VicA==" height="200" alt="">

### Description
This toolset helps to create randomly generated 3D collection of characters that could be used as NFTs.
You need to prepare characters in Blender and separate them by parts as objects which could replace each other in their categories.
For example, you need to create 2 or more hats which will be good fit with all heads.

### Toolset
1. predefined_categories.py - contains predefined categories of objects of 3D model that were gathered via Blender API
2. additional_func.py - contains additional functional
3. category_builder.py - builds categories of parts for easier product generation
4. product_generator.py - generates characters DB which are not prepared for the following render
5. body_parts_injector.py - adds parts in characters body in time of character creation
6. character_creator.py - creates DB with characters which are ready to be rendered
7. material_changer.py - changes material in slots of parts, uses by render_machine 
8. render_machine.py - uses by Blender to automatically render the right amount of specific characters from DB 
9. metadata_creator.py - creates character metadata for the following upload via auto_uploader 
10. media_converter.py - converts rendered animation sequences into media files 
11. auto_uploader.py - automatically mints on marketplace

### Process
- Gather all needed objects and material form .blend and prepare lists and dicts.
- Build categories of objects with predefined logic for the following processing.
- Create DB with products.
- Create characters DB from products using parts injector to add special parts.
- Run render machine which will use material changer to randomly paint character which will be chosen randomly or by a given tag.
- Create metadata files for rendered characters.
- Create media file that will represent your character on marketplace.
- Run collection uploading process that will be automatically minted.


---
#### Will be supplemented