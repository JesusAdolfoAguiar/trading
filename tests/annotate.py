from PIL import Image, ImageDraw, ImageFont

def annotate_chart(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = img.size
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
        
    # The true missing one: 3 zones below the last arrow (4329.25 - 17.25 = 4312.00)
    # This is the drop right before the massive green candle.
    # Drop starts around 4323.50 (Main POI), creates Bearish FVG, wicks exactly on 4312.00 (Main POI).
    
    y_top_fvg = int(height * 0.68) # ~4323.50
    y_bottom_fvg = int(height * 0.81) # ~4314 (bottom of gap)
    x_start = int(width * 0.42)
    x_end = int(width * 0.46)
    
    # Draw the Bearish FVG
    draw.rectangle([x_start, y_top_fvg, x_end, y_bottom_fvg], 
                   fill=(255, 100, 100, 60), outline=(255, 50, 50, 255), width=2)
    draw.text((x_start, y_top_fvg - 25), "The 'Missing' FVG", fill=(255, 255, 255, 255), font=font)
    
    # Rejection perfectly on the 4312.00 Main POI
    # 4376.17 (top) - 4312.00 = 64.17. 64.17 / 77.5 (range) = 0.828
    y_rejection = int(height * 0.828)
    bounce_x = int(width * 0.45) # right at 15:05
    
    # Arrow for the massive bullish move that fills it
    draw.line([(bounce_x, y_rejection), (bounce_x, y_top_fvg)], fill=(255, 255, 0, 255), width=4)
    draw.polygon([(bounce_x, y_top_fvg), (bounce_x - 6, y_top_fvg + 12), (bounce_x + 6, y_top_fvg + 12)], fill=(255, 255, 0, 255))
    
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(output_path)
    print(f"Annotated image saved to {output_path}")

if __name__ == "__main__":
    annotate_chart("/home/ubuntu/personal/trading/tests/test.png", "/home/ubuntu/personal/trading/tests/test_annotated7.png")
