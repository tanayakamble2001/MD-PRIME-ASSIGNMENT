from PIL import Image
import os

def is_valid_image(image_path):
    """Check if the provided file is a valid image."""
    try:
        with Image.open(image_path) as img:
            img.load()  # Ensure the image is fully loaded into memory
        return True
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return False

def resize_images_to_same_size(images):
    """Resize all images to the smallest width and height."""
    min_width = min(img.width for img in images)
    min_height = min(img.height for img in images)
    resized_images = [img.resize((min_width, min_height)) for img in images]
    return resized_images

def create_collage(images, output_path, output_format, grid_size=(2, 2)):
    """Arrange the images in a grid and save as the output file."""
    width, height = images[0].size
    collage_width = width * grid_size[0]
    collage_height = height * grid_size[1]

    collage = Image.new('RGB', (collage_width, collage_height))

    # Paste images in a grid
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            index = row * grid_size[0] + col
            if index < len(images):
                collage.paste(images[index], (col * width, row * height))

    collage.save(output_path, output_format)
    print(f"Collage saved as {output_path}")

def main():
    # Input: File paths for the images
    images = []
    num_images = 4  # Default to 4 images, but this can be changed
    for i in range(1, num_images + 1):
        while True:
            image_path = input(f"Please enter the path for Image {i}: ")
            if os.path.exists(image_path) and is_valid_image(image_path):
                with Image.open(image_path) as img:
                    img.load()  # Ensure the image is fully loaded into memory
                    images.append(img.copy())  # Copy the image to avoid closing the file context
                break
            else:
                print(f"Invalid image file: {image_path}. Please provide a valid image file.")

    # Resize all images to the same size
    images = resize_images_to_same_size(images)

    # Input: Desired output format
    output_format = input("Please specify the output file format (jpg, png, etc.): ").upper()
    output_path = f"collage.{output_format.lower()}"  # Ensure the extension is in lowercase

    # Create the collage and save it
    create_collage(images, output_path, output_format)

if __name__ == "__main__":
    main()
