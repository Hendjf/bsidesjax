#!/usr/bin/env python3
import os
from datetime import datetime

# Directory to scan (change if needed)
IMG_DIR = "."

def main():
    # find all .png files
    images = sorted(f for f in os.listdir(IMG_DIR) if f.lower().endswith('.png'))
    if not images:
        print("No PNGs found in", IMG_DIR)
        return

    # build HTML
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>BSidesJax Image Gallery</title>
  <style>
    body {{ font-family: sans-serif; padding: 1rem; }}
    .img-wrap {{ margin-bottom: 2rem; }}
    img {{ max-width: 100%; height: auto; border: 1px solid #ccc; }}
    figcaption {{ font-size: 0.9rem; color: #666; }}
  </style>
</head>
<body>
  <h1>BSidesJax Image Gallery</h1>
  <p>Generated on {now}</p>
  {''.join(f'''
  <figure class="img-wrap">
    <img src="{img}" alt="{img}">
    <figcaption>{img}</figcaption>
  </figure>''' for img in images)}
</body>
</html>
"""
    # write out
    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ gallery.html generated with {len(images)} images.")

if __name__ == "__main__":
    main()
