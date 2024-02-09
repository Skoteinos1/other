import os

path = '/home/skoty/Stable Diffusion UI/1701102498415/'

strings_to_have = [
    '1895996768',
    'Generate an image of a 21-year-old blond woman with dark blue eyes. Capture her in a moment of quiet contentment, featuring a subtle and genuine suggestive smile. Emphasize a sense of calm and charm in her expression. In terms of makeup, she has strong pink blush shades under her eyes and dark bottom eyeliner, noticeable black lower lash lines. The setting should be neutral, and the lighting should be soft and natural to enhance the warmth of the scene. Please ensure the image is tasteful and avoids any explicit or inappropriate elements, focusing on highlighting her personality and charm.',
    'BadDream, (UnrealisticDream:1.3), glasses, cap, hat, hoodie',
    "absolutereality_v181",
    '"use_lora_model": null,',
]

for path, subdirs, files in os.walk(path):
    for fl in files:
        key = ''
        if '.txt' in fl or '.xml' in fl or '.json' in fl:
            file1 = open(path + '/' + fl, "r")
            read_content = file1.read()
            file1.close()
            if all(i in read_content for i in strings_to_have):
                print(fl)
            # print(read_content)
        # break
    # break


