from PIL import Image, ImageDraw, ImageFont

def annotate_swings(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = img.size
    
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except:
        font = ImageFont.load_default()
        
    # Helper to map price to y-coordinate
    def price_to_y(p):
        return int(height * ((4376.17 - p) / 77.5))
        
    # We will draw lines representing the macro directional moves (Swings)
    # Swing 1: Massive Bullish (15:05 to 15:30)
    # Starts at 4312.00, ends at 4369.50. Distance: $57.50 (5 zones)
    x1, y1 = int(width * 0.45), price_to_y(4312.00)
    x2, y2 = int(width * 0.49), price_to_y(4369.50)
    draw.line([(x1, y1), (x2, y2)], fill=(0, 255, 0, 150), width=6)
    draw.text((x1 + 10, y1 - 40), "+$57.50 (5 Zones / 575 pips)", fill=(0, 255, 0, 255), font=font)
    
    # Swing 2: Bearish Drop to FVG 1 (16:25 to 17:05)
    # Starts at 4369.50 (double top), ends at 4340.75. Distance: $28.75 (2.5 zones)
    x3, y3 = int(width * 0.51), price_to_y(4369.50)
    x4, y4 = int(width * 0.58), price_to_y(4340.75)
    draw.line([(x3, y3), (x4, y4)], fill=(255, 50, 50, 150), width=6)
    draw.text((x4 + 10, y4 - 20), "-$28.75 (2.5 Zones / 287 pips)", fill=(255, 100, 100, 255), font=font)
    
    # Swing 3: Bullish FVG 1 Fill (17:05 to 18:25)
    # Starts at 4340.75, ends at 4363.75 (approx peak). Distance: $23.00 (2 zones)
    x5, y5 = int(width * 0.64), price_to_y(4363.75)
    draw.line([(x4, y4), (x5, y5)], fill=(0, 255, 0, 150), width=6)
    draw.text((x4 + 40, y4 - 60), "+$23.00 (2 Zones / 230 pips)", fill=(0, 255, 0, 255), font=font)
    
    # Swing 4: Bearish Drop to FVG 2 (18:25 to 19:45)
    # Starts at 4363.75, ends at 4329.25. Distance: $34.50 (3 zones)
    x6, y6 = int(width * 0.73), price_to_y(4329.25)
    draw.line([(x5, y5), (x6, y6)], fill=(255, 50, 50, 150), width=6)
    draw.text((x6 + 10, y6 - 20), "-$34.50 (3 Zones / 345 pips)", fill=(255, 100, 100, 255), font=font)
    
    # Draw a trendline connecting the bottoms (4352.25 -> 4340.75 -> 4329.25)
    # This shows the mathematical step-down nature of the moves
    # Actually, 4312 is down there too. Let's just draw the trendline through the Mid-POI rejections.
    bx1, by1 = int(width * 0.51), price_to_y(4352.25) # 15:45 rejection
    bx2, by2 = int(width * 0.58), price_to_y(4340.75) # 17:05 rejection
    bx3, by3 = int(width * 0.73), price_to_y(4329.25) # 19:45 rejection
    
    draw.line([(bx1, by1), (bx3, by3)], fill=(255, 255, 255, 200), width=3)
    
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(output_path)
    print(f"Annotated image saved to {output_path}")

if __name__ == "__main__":
    annotate_swings("/home/ubuntu/personal/trading/tests/test.png", "/home/ubuntu/personal/trading/tests/test-swings.png")
