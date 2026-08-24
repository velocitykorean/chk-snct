"""
Chakra Healing YouTube Thumbnail Generator
- Generates mystical, high-CTR spiritual thumbnails (1280x720)
- Automatically detects and removes AI/Gemini star watermarks via OpenCV inpainting
- Clean, majestic typography (Cinzel / Playfair) without distracting underlines
- Rich golden aura glow, deep ambient vignette, and Solfeggio frequency badges
"""

import os
import sys
import random
import cv2
import numpy as np
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

def remove_watermark(cv_img):
    """Removes corner AI watermarks (e.g. Gemini star) seamlessly using OpenCV inpainting."""
    h, w = cv_img.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)
    
    # Gemini watermark star zone in bottom-right corner
    sx1 = int(w * 0.89)
    sy1 = int(h * 0.83)
    sx2 = int(w * 0.96)
    sy2 = int(h * 0.94)
    mask[sy1:sy2, sx1:sx2] = 255
    
    inpainted = cv2.inpaint(cv_img, mask, inpaintRadius=4, flags=cv2.INPAINT_TELEA)
    return inpainted

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

def apply_spiritual_vignette(img, intensity=0.28):
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
    Creates a clean, high-converting Chakra Healing YouTube thumbnail (1280x720).
    Watermarks are automatically removed and typography is styled without lines.
    """
    if not main_text:
        preset = random.choice(CHAKRA_HOOKS)
        main_text = preset["main"]
        sub_text = preset["sub"]
        badge_text = preset.get("badge", "432Hz · 1 HOUR")
    elif not badge_text:
        badge_text = "432Hz · 1 HOUR"

    # 1. Load image & Inpaint watermark
    cv_img = cv2.imread(bg_path)
    if cv_img is not None:
        clean_cv = remove_watermark(cv_img)
        rgb_img = cv2.cvtColor(clean_cv, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb_img).convert("RGBA")
    else:
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
    img = ImageEnhance.Color(img).enhance(1.12)
    img = ImageEnhance.Contrast(img).enhance(1.05)
    
    # 2. Add mystical vignette
    img = apply_spiritual_vignette(img, intensity=0.28)
    
    # 3. Create text overlay
    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_main = get_font("Cinzel.ttf", size=64)
    font_sub = get_font("PlayfairDisplay.ttf", size=30)
    font_badge = get_font("Cinzel.ttf", size=24)
    
    # Bottom-left typography layout
    x_pos = 70
    y_base = target_h - 165
    
    # Subtitle (Clean glowing gold text with drop shadow, no harsh line)
    if sub_text:
        for dx, dy in [(-2,2), (2,2), (0,2), (2,0), (-1,-1)]:
            draw.text((x_pos + dx, y_base - 40 + dy), sub_text.upper(), font=font_badge, fill=(0, 0, 0, 230))
        draw.text((x_pos, y_base - 40), sub_text.upper(), font=font_badge, fill=(255, 225, 150, 255))
        
    # Main Headline (Crisp brilliant white with multi-directional dark drop shadow)
    for dx, dy in [(-3,3), (3,3), (0,4), (4,4), (-2,-2), (2,-2)]:
        draw.text((x_pos + dx, y_base + dy), main_text.upper(), font=font_main, fill=(0, 0, 0, 240))
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
        fill=(10, 15, 25, 190),
        outline=(255, 215, 0, 180),
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
    test_bg = os.path.join(SCRIPT_DIR, "input_images", "Golden_figure_sitting_in_lotus_202608231719.jpeg")
    test_out = os.path.join(SCRIPT_DIR, "output_thumbnails", "Chakra_Thumb_Clean.jpg")
    if os.path.exists(test_bg):
        create_chakra_thumbnail(test_bg, test_out, "ALL 7 CHAKRAS", "UNBLOCK & HEAL ENTIRE AURA", "432Hz · 1 HOUR")
    else:
        print("[!] Base background not found for testing.")
