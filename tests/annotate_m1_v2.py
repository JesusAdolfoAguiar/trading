from PIL import Image, ImageDraw, ImageFont

def draw_up_arrow(draw, tip_x, tip_y, size=30, color=(255, 255, 0, 255)):
    # Draw an upward pointing arrow
    draw.line([(tip_x, tip_y + size), (tip_x, tip_y)], fill=color, width=4)
    draw.polygon([(tip_x, tip_y), (tip_x - 8, tip_y + 16), (tip_x + 8, tip_y + 16)], fill=color)

def annotate_m1_v2(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = img.size
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
        
    # The true "execution" entry isn't catching the falling knife at the Mid-POI.
    # It's waiting for the M1 Market Structure Shift (MSS) and pulling back into the M1 FVG.
    
    # 1. Entry 1 (FVG 0): 
    # M5 POI hit at 15:48. M1 rallies, creates M1 FVG. Pullback occurs at 15:50.
    x1 = int(width * 0.22) # Pullback candle
    y1 = int(height * 0.25) # Approx height of the pullback
    draw_up_arrow(draw, x1, y1, size=40)
    draw.text((x1 - 40, y1 + 50), "M1 FVG Entry 1", fill=(255, 255, 0, 255), font=font)
    
    # 2. Entry 2 (FVG 0.5): 
    # M5 POI hit at 16:01. M1 rallies, creates M1 FVG. Pullback occurs at 16:04.
    x2 = int(width * 0.29) 
    y2 = int(height * 0.25) 
    draw_up_arrow(draw, x2, y2, size=40)
    draw.text((x2 - 40, y2 + 50), "M1 FVG Entry 2", fill=(255, 255, 0, 255), font=font)
    
    # 3. Entry 3 (FVG 1): 
    # M5 POI hit at 17:08. M1 rallies, creates M1 FVG. Pullback occurs at 17:12.
    x3 = int(width * 0.54) 
    y3 = int(height * 0.40) # Approx height of the 17:12 pullback
    draw_up_arrow(draw, x3, y3, size=40)
    draw.text((x3 - 40, y3 + 50), "M1 FVG Entry 3\n(The Sniper)", fill=(255, 255, 0, 255), font=font)
    
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(output_path)
    print(f"Annotated image saved to {output_path}")

if __name__ == "__main__":
    annotate_m1_v2("/home/ubuntu/personal/trading/tests/test-m1.png", "/home/ubuntu/personal/trading/tests/test-m1-annotated2.png")
