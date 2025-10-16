#!/usr/bin/env python3
"""
Hugging Face Spaces entry point for Bhumika's Portfolio
This file ensures proper deployment on Hugging Face Spaces
"""

import os
import sys
import streamlit as st
from pathlib import Path

# Set environment variables for Hugging Face Spaces
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_SERVER_ENABLE_CORS"] = "false"
os.environ["STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION"] = "false"
os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"

# Add the src directory to Python path
src_path = Path(__file__).parent / "src"
if src_path.exists():
    sys.path.insert(0, str(src_path))

# Copy images to root level for Hugging Face Spaces
def setup_assets():
    """Setup assets for Hugging Face Spaces deployment"""
    try:
        import shutil
        
        # Create assets directory in root
        assets_root = Path("assets")
        assets_root.mkdir(exist_ok=True)
        
        # Copy images from src/assets to root assets
        src_assets = Path("src/assets")
        if src_assets.exists():
            for img_file in src_assets.glob("*.jfif"):
                dest_file = assets_root / img_file.name
                if not dest_file.exists():
                    shutil.copy2(img_file, dest_file)
                    
    except Exception as e:
        # Silently handle setup errors in HF Spaces
        pass

# Setup assets
setup_assets()

# Import and run the main application
try:
    from streamlit_app import *
except ImportError:
    # Fallback import
    exec(open("src/streamlit_app.py").read())