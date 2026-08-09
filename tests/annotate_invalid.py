from PIL import Image, ImageDraw, ImageFont

def annotate_invalid(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = img.size
    
    try:
        font = ImageFont.truetype("arial.ttf", 25)
    except:
        font = ImageFont.load_default()
        
    # Estimated bounding box for the choppy price action
    x_start = int(width * 0.58) # Shifted right to ~17:25
    x_end = int(width * 0.88)
    y_start = int(height * 0.35)
    y_end = int(height * 0.60)
    
    # Draw the rectangle
    draw.rectangle([x_start, y_start, x_end, y_end], 
                   outline=(255, 50, 50, 255), width=4)
                   
    # Draw text label
    text = "Invalid / Choppy Price Action (No Clean FVG)"
    
    # Try to calculate text width for centering
    try:
        # For newer Pillow versions
        bbox = draw.textbbox((0,0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
    except:
        # Fallback
        text_w = font.getlength(text) if hasattr(font, 'getlength') else 200
        text_h = 20
        
    text_x = x_start + (x_end - x_start - text_w) / 2
    text_y = y_start - text_h - 10
    
    draw.text((text_x, text_y), text, fill=(255, 50, 50, 255), font=font)
    
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(output_path)
    print(f"Annotated image saved to {output_path}")

if __name__ == "__main__":
    annotate_invalid("/home/ubuntu/personal/trading/tests/vision_ground_truth/invalid_fvg/test.png", "/home/ubuntu/personal/trading/tests/vision_ground_truth/invalid_fvg/test_annotated_invalid.png")
