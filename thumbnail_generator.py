"""
Chakra Healing YouTube Thumbnail Generator
- Generates mystical, high-CTR spiritual thumbnails
- Features sacred geometry, 7 Chakra radiant glow, and elegant typography (Cinzel / Playfair)
- Uses high-converting power hooks & Solfeggio frequency badges (432Hz, 528Hz, 963Hz)
- Output: Standard YouTube 1280x720 (16:9)
"""

import os
import sys
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

CHAKRA_HOOKS = [
    {"main": "ALL 7 CHAKRAS", "sub": "UNBLOCK & HEAL ENTIRE AURA", "badge": "432Hz · 1 HOUR"},
    {"main": "CHAKRA HEALING", "sub": "INSTANT NEGATIVE ENERGY RELEASE", "badge": "528Hz · MIRACLE TONE"},
    {"main": "KUNDALINI AWAKENING", "sub": "DEEP CELLULAR REGENERATION", "badge": "963Hz · GOD FREQUENCY"},
    {"main": "SACRED RESONANCE", "sub": "FULL BODY PRANA ALIGNMENT", "badge": "432Hz · DEEP PEACE"},
    {"main": "THIRD EYE OPENING", "sub": "INTUITION & PINEAL ACTIVATION", "badge": "852Hz · SPIRITUAL AWAKENING"},
    {"main": "HEART HEALING", "sub": "ATTRACT LOVE & INNER HARMONY", "badge": "639Hz · CELLULAR REPAIR"},
    {"main": "AURA CLEANSE", "sub": "RELEASE BLOCKAGES & RESTORE PEACE", "badge": "SOLFEGGIO · 1 HOUR"}
]

def get_font(font_name="Cinzel.ttf", size=56):
    """Load font with project fallback hierarchy."""
    font_path = os.path.join(SCRIPT_DIR, "assets", "fonts", font_name)
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
            
    # Fallback to Playfair
    pf = os.path.join(SCRIPT_DIR, "assets", "fonts", "PlayfairDisplay.ttf")
    if os.path.exists(pf):
        try:
            return ImageFont.truetype(pf, size)
        except Exception:
            pass

    # Windows system fonts
    for f in [r"C:\Windows\Fonts\georgiab.ttf", r"C:\Windows\Fonts\georgia.ttf", r"C:\Windows\Fontsrialbd.ttf"]:
        if os.path.exists(f):
            try:
                return ImageFont.truetype(f, size)
            except Exception:
                pass

    return ImageFont.load_default()

def apply_spiritual_vignette(img, intensity=0.32):
    """Applies a rich mystical vignette to create depth and frame center energy."""
    W, H = img.size
    mask = Image.new("L", (W, H), 0)
    draw_m = ImageDraw.Draw(mask)
    draw_m.ellipse([-W * 0.15, -H * 0.15, W * 1.15, H * 1.15], fill=int(255 * (1.0 - intensity)))
    mask = mask.filter(ImageFilter.GaussianBlur(radius=int(W * 0.07)))
    dark = Image.new("RGBA", (W, H), (8, 12, 18, 255))
    return Image.composite(img, dark, mask)

def create_chakra_thumbnail(bg_path, output_path, main_text=None, sub_text=None, badge_text=None):
    """
    Creates an eye-catching, high-converting Chakra Healing YouTube thumbnail (1280x720).
    """
    if not main_text:
        preset = random.choice(CHAKRA_HOOKS)
        main_text = preset["main"]
        sub_text = preset["sub"]
        badge_text = preset.get("badge", "432Hz · 1 HOUR")
    elif not badge_text:
        badge_text = "432Hz · 1 HOUR"

    # 1. Open and resize/crop to 1280x720 (16:9)
    img = Image.open(bg_path).convert("RGBA")
    target_w, target_h = 1280, 720
    
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h
    
    if img_ratio > target_ratio:
        new_w = int(img.height * target_ratio)
        offset = (img.width - new_w) // 2
        img = img.crop((offset, 0, offset + new_w, img.height))
    else:
        new_h = int(img.width / target_ratio)
        offset = (img.height - new_h) // 2
        img = img.crop((0, offset, img.width, offset + new_h))
        
    img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Enhance vibrant golden and chakra colors
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.12)
    
    # Contrast bump
    enhancer_con = ImageEnhance.Contrast(img)
    img = enhancer_con.enhance(1.05)
    
    # 2. Add mystical vignette
    img = apply_spiritual_vignette(img, intensity=0.28)
    
    # 3. Create text overlay
    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_main = get_font("Cinzel.ttf", size=64)
    font_sub = get_font("PlayfairDisplay.ttf", size=30)
    font_badge = get_font("Cinzel.ttf", size=24)
    
    # Bottom-left typography layout with generous margins
    x_pos = 70
    y_base = target_h - 170
    
    # Subtitle / Category
    if sub_text:
        # Subtle glowing line or tag
        draw.text((x_pos + 1, y_base - 42 + 1), sub_text.upper(), font=font_badge, fill=(0, 0, 0, 200))
        draw.text((x_pos, y_base - 42), sub_text.upper(), font=font_badge, fill=(255, 225, 160, 255))
        # Golden accent line
        line_y = y_base - 16
        draw.line([(x_pos, line_y), (x_pos + 220, line_y)], fill=(255, 215, 0, 200), width=2)
        
    # Main Headline (White with multi-directional deep glow drop shadow)
    for dx, dy in [(-3,3), (3,3), (0,4), (4,4), (-2,-2), (2,-2)]:
        draw.text((x_pos + dx, y_base + dy), main_text.upper(), font=font_main, fill=(0, 0, 0, 220))
    # Crisp brilliant white & warm golden highlight
    draw.text((x_pos, y_base), main_text.upper(), font=font_main, fill=(255, 255, 255, 255))
    
    # Top-Right Solfeggio / Duration Badge
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw, bh = bbox[2] - bbox[0], bbox[3] - bbox[1]
    bx = target_w - bw - 70
    by = 45
    padding_x = 16
    padding_y = 10
    
    # Glowing pill background for badge
    draw.rounded_rectangle(
        [bx - padding_x, by - padding_y, bx + bw + padding_x, by + bh + padding_y],
        radius=10,
        fill=(10, 15, 25, 180),
        outline=(255, 215, 0, 160),
        width=2
    )
    draw.text((bx, by), badge_text, font=font_badge, fill=(255, 240, 200, 250))
    
    # Merge overlay
    final = Image.alpha_composite(img, overlay).convert("RGB")
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    final.save(output_path, quality=96)
    print(f"[+] Generated Chakra Thumbnail: {output_path}")
    return output_path

if __name__ == "__main__":
    test_bg = os.path.join(SCRIPT_DIR, "input_images", "base_frame.jpg")
    test_out = os.path.join(SCRIPT_DIR, "output_thumbnails", "Test_Chakra_Thumb.jpg")
    if os.path.exists(test_bg):
        create_chakra_thumbnail(test_bg, test_out, "ALL 7 CHAKRAS", "UNBLOCK & HEAL ENTIRE AURA", "432Hz · 1 HOUR")
    else:
        print("[!] Base frame not found for testing.")
