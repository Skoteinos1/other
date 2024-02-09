# Prints out exif/meta data for list of images in current folder
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from PIL.ExifTags import TAGS, GPSTAGS, IFD
import json
from string import printable


def exif_from_jpg(pth):
    # reads data from .jpg .jpeg .webp images
    image = Image.open(pth)
    exif = image.getexif()
    info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
    }

    # register_heif_opener()   # HEIF support
 
    for k, v in exif.items():
        tag = TAGS.get(k, k)
        info_dict[tag] = v

    for ifd_id in IFD:
        try:
            ifd = exif.get_ifd(ifd_id)

            if ifd_id == IFD.GPSInfo:
                resolve = GPSTAGS
            else:
                resolve = TAGS

            for k, v in ifd.items():
                tag = resolve.get(k, k)
                if ifd_id.name == 'Exif':
                    json_string = v.decode('utf-8')
                    json_string = ''.join(char for char in json_string if char in printable)
                    json_string = json_string[len('UNICODE'):]
                    # json_string = json_string.replace('null', '0')
                    user_comment_data = json.loads(json_string)
                    # print(json.dumps(user_comment_data, indent=2))
                    for key in user_comment_data:
                        info_dict[key] = user_comment_data[key]
                        # print(key, user_comment_data[key])
                else:
                    print(tag, v)
        except KeyError:
            pass

    # for label,value in info_dict.items():
    #     print(f"{label:26}: {value}")

    return info_dict


def metadata_from_png(pth):
    # reads .png files
    im = Image.open(pth)
    im.load()  # Needed only for .png EXIF data (see citation above)
    #print(im.info['meta_to_read'])
    # print(im.info)
    im.close()
    return im.info 
    

def metadata_to_png(pth):
    # This data will be pushed into image. It will replace it, not update it.
    targetImage = Image.open(pth)
    metadata = PngInfo()
    metadata.add_text("MyNewString", 'A string')
    # metadata.add_text("MyNewInt", str(1234))
    metadata.add_text('Author', 'John Doe')
    metadata.add_text('Description', 'A beautiful sunset')
    metadata.add_text('Location', 'San Franciscooooo')
    metadata.add_text('User Comment', '{"prompt": "a photograph of an astronaut riding a horse", "negative_prompt": "", "seed": 1904377878, "use_stable_diffusion_mode…')
    metadata.add_text('Exif Other', '{"prompt": "a photograph of an astronaut riding a horse", "negative_prompt": "", "seed": 1904377878, "use_stable_diffusion_mode…')
    # targetImage.save('output.jpg',exif=exif)
    pth = pth.replace('.png', '2.png')
    targetImage.save(pth, pnginfo=metadata)
    

def data_from_image(pth):
    # get exif/meta data as dictionary
    if '.png' in pth:
        img = Image.open(pth)
        # img = img.resize((100,100),Image.BILINEAR) # edit the image
        # exif = img.info['exif']
        exif = img.info
        # exif = img.text
    elif any(x in pth for x in ['.jpg', '.jpeg', '.webp']):
        exif = exif_from_jpg(pth)
    return exif


images_to_read = ['8k.png', 'NewPath.png', '0H33RSV_0.jpg']

for i in range(len(images_to_read)):
    print(images_to_read[i], '\n', data_from_image(images_to_read[i]), '\n\n')
   
