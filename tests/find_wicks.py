from PIL import Image, ImageDraw

def analyze(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = img.size
    
    # 4376 to 4298 -> 78 range
    # Let's draw horizontal lines for all Mid-POIs
    # 4363.75 -> (4376.17 - 4363.75)/78 = 12.42/78 = 0.159 (15.9%)
    # 4352.25 -> (4376.17 - 4352.25)/78 = 23.92/78 = 0.306 (30.6%)
    # 4340.75 -> (4376.17 - 4340.75)/78 = 35.42/78 = 0.454 (45.4%)
    # 4329.25 -> (4376.17 - 4329.25)/78 = 46.92/78 = 0.601 (60.1%)
    
    y_mid = [
        int(height * 0.159),
        int(height * 0.306),
        int(height * 0.454),
        int(height * 0.601)
    ]
    
    colors = [(255,0,0), (0,255,0), (0,0,255), (255,0,255)]
    labels = ["4363.75", "4352.25", "4340.75", "4329.25"]
    
    for y, color, label in zip(y_mid, colors, labels):
        draw.line([(0, y), (width, y)], fill=color, width=2)
    
    # Highlight the region between x=48% and 58%
    draw.rectangle([int(width*0.48), 0, int(width*0.58), height], outline=(255,255,0), width=3)
    
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(output_path)

if __name__ == "__main__":
    analyze("/home/ubuntu/personal/trading/tests/test.png", "/home/ubuntu/personal/trading/tests/test_analysis.png")
