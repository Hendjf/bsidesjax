I BROKEN IT GO AWAY

# BSidesJax Image Gallery Generator

A lightweight toolset for the BSides Jacksonville (BSidesJax) repository to automatically generate an HTML image gallery from PNG assets.

## Description

This repository hosts PNG assets related to BSides Jax events. The included Python script (`generate_gallery.py`) scans for all `.png` files in the root directory and produces a `gallery.html` page for easy offline or web-based viewing of event graphics.

## Prerequisites

* Python 3.x installed on your system

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Hendjf/bsidesjax.git
   cd bsidesjax
   ```
2. **Verify contents**: Ensure your PNG images and `generate_gallery.py` are present in the root folder.

## Usage

1. **Make the script executable** (if necessary):

   ```bash
   chmod +x generate_gallery.py
   ```
2. **Run the gallery generator**:

   ```bash
   ./generate_gallery.py
   ```
3. **View the gallery**:

   * Open `gallery.html` in your web browser to preview all images with captions and timestamps.

## File Structure

```
bsidesjax/
├── generate_gallery.py   # Script to generate the HTML gallery
├── gallery.html          # Generated output (after running script)
└── *.png                 # Your PNG assets
```

## Customization

* **Styling**: Edit the `<style>` block in the generated `gallery.html` to adjust fonts, borders, or layouts.
* **Image Types**: To support other formats (e.g., JPG), modify `generate_gallery.py` to include additional file extensions.

## Contributing

Contributions are welcome! Feel free to:

* Improve script functionality (e.g., recursive directory support)
* Enhance gallery styling
* Add README enhancements or documentation
