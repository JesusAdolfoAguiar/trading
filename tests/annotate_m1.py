from PIL import Image, ImageDraw, ImageFont

def draw_up_arrow(draw, tip_x, tip_y, size=30, color=(0, 255, 0, 255)):
    # Draw an upward pointing arrow
    # Line
    draw.line([(tip_x, tip_y + size), (tip_x, tip_y)], fill=color, width=4)
    # Arrowhead
    draw.polygon([(tip_x, tip_y), (tip_x - 8, tip_y + 16), (tip_x + 8, tip_y + 16)], fill=color)

def annotate_m1(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = img.size
    
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
        
    # The y-coordinates for the Mid-POIs
    # Based on the right y-axis, 4375.25 is top, 4294.75 is bottom. Range = 80.5
    y_4352 = int(height * ((4375.25 - 4352.25) / 80.5))
    y_4340 = int(height * ((4375.25 - 4340.75) / 80.5))
    
    # 1. First perfect entry at 4352.25 Mid-POI (FVG 0)
    # It occurs at the first sharp V-bottom after the main peak, around x=20.5%
    x1 = int(width * 0.205)
    draw_up_arrow(draw, x1, y_4352 + 5, size=40)
    draw.text((x1 - 10, y_4352 + 55), "Entry 1", fill=(0, 255, 0, 255), font=font)
    
    # 2. Second perfect entry at 4352.25 Mid-POI (FVG 0.5)
    # It occurs at the second sharp V-bottom, around x=27.5%
    x2 = int(width * 0.275)
    draw_up_arrow(draw, x2, y_4352 + 5, size=40)
    draw.text((x2 - 10, y_4352 + 55), "Entry 2", fill=(0, 255, 0, 255), font=font)
    
    # 3. Third perfect entry at 4340.75 Mid-POI (FVG 1)
    # It occurs at the deep V-bottom after the double top, around x=52%
    x3 = int(width * 0.522)
    draw_up_arrow(draw, x3, y_4340 + 5, size=40)
    draw.text((x3 - 10, y_4340 + 55), "Entry 3", fill=(0, 255, 0, 255), font=font)
    
    # Note: There's a slight double bottom around x=54% as well. We'll mark the first one as the initial sniper entry.
    
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(output_path)
    print(f"Annotated image saved to {output_path}")

if __name__ == "__main__":
    annotate_m1("/home/ubuntu/personal/trading/tests/test-m1.png", "/home/ubuntu/personal/trading/tests/test-m1-annotated.png")
