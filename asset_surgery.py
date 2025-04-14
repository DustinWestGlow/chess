from PIL import Image

def split_image(image_path, rows, cols, output_prefix):
    """
    Splits an image into a grid of smaller images.

    Args:
        image_path (str): Path to the input image.
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        output_prefix (str, optional): Prefix for the output file names. Defaults to "part".
    """
    try:
        img = Image.open(image_path)
        width, height = img.size
        tile_width = width // cols
        tile_height = height // rows
        
        for i in range(rows):
            for j in range(cols):
                left = j * tile_width
                upper = i * tile_height
                right = (j + 1) * tile_width
                lower = (i + 1) * tile_height
                
                # Ensure that the last tile includes any remaining pixels
                if j == cols - 1:
                    right = width
                if i == rows - 1:
                    lower = height
                
                tile = img.crop((left, upper, right, lower))
                output_path = f"{output_prefix}/img_{i}_{j}.png"
                tile.save(output_path)
                print(f"Saved: {output_path}")

    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
    except Exception as e:
         print(f"An error occurred: {e}")

# Example usage:
split_image("chess.png", 12, 6, "assets")