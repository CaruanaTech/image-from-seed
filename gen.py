from PIL import Image
import random
import math
import sys

def text_seed_to_integer(seed):
    """Turn a string into a unique integer value. Used for seeds as the random library does not support string seeds

    Args:
        seed (String): the seed

    Returns:
        Int: Byte-encoded seed
    """
    return int.from_bytes(seed.encode(), 'little')

def create_image(x, y):
    """initialise a new PIL image of dimensions X*Y

    Args:
        x (int): the image length
        y (int): the image height

    Returns:
        Image: blank PIL image object
    """
    image = Image.new('RGB', (x, y))
    return image

def shuffle_seed(seed):
    """create a new seed by shuffling the characters in the pre-existing seed

    Args:
        seed (int): the randomiser seed
    """
    # print(f"{seed} -> ", end="")
    # turn it into an array
    seed_to_shuffle = [int(a) for a in str(seed)]
    # shuffle it    
    random.shuffle(seed_to_shuffle)
    # turn it back into a number
    string_ints = [str(int) for int in seed_to_shuffle]
    seed = "".join(string_ints)
    # print(seed)

def generate_rgb_tuple():
    """create 3 unique integers between 0 and 255, shuffling the seed each time

    Returns:
        tuple: an RGB value to use in PIL
    """
    final_array = []
    for i in range(3):
        color_x = random.randint(0, 256)
        # print(color_x)
        final_array.append(color_x)
        shuffle_seed(seed)
    
    return (final_array[0], final_array[1], final_array[2])

def generate_image_from_seed(image):
    """method that places a pseudo-random color in every pixel based on the seed. The seed is shuffled again after every pixel placement.

    Args:
        image (PIL.Image): a PIL image
    """
    for pixel_x in range(image.width):
        for pixel_y in range(image.height):
            color = generate_rgb_tuple()
            # print(f"placing {color} @ {pixel_x},{pixel_y}")
            image.putpixel((pixel_x, pixel_y), color)
            shuffle_seed(seed)

if __name__ == "__main__":
    seed = input("Seed: ")
    if not isinstance(seed, int):
        seed = text_seed_to_integer(seed)
        print("seed is not an integer, converted to: {}".format(seed))

    random.seed(seed)
    # now that the first seed has been set,
    # make sure the seed is in a shuffle-able format
    print("generating image with seed {}".format(seed))
    image = create_image(16, 16)
    generate_image_from_seed(image)
    image.save(f"output/{seed}.jpg")