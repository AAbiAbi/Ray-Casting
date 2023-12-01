def hex_to_rgb(hex_color):
    """Convert hex color string to an RGB tuple."""
    hex_color = hex_color.lstrip('#')  # Remove '#' if present
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
