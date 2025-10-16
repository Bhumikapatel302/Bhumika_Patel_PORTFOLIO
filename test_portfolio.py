#!/usr/bin/env python3
"""
Test script to validate Bhumika's portfolio functionality
"""

import os
import sys
from pathlib import Path

def test_file_structure():
    """Test that all required files are present"""
    required_files = [
        "src/streamlit_app.py",
        "src/assets/Bhumika_Photo.jfif",
        "src/assets/Presentation_Leadership_hackSRIT.jfif",
        "requirements.txt",
        "WARP.md"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files are present")
        return True

def test_image_files():
    """Test that image files are valid"""
    image_files = [
        "src/assets/Bhumika_Photo.jfif",
        "src/assets/Presentation_Leadership_hackSRIT.jfif"
    ]
    
    for img_path in image_files:
        if os.path.exists(img_path) and os.path.getsize(img_path) > 0:
            print(f"✅ {img_path} - Valid image file")
        else:
            print(f"❌ {img_path} - Invalid or empty file")
            return False
    
    return True

def test_streamlit_syntax():
    """Basic syntax check for streamlit app"""
    try:
        with open("src/streamlit_app.py", 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for deprecated parameters
        if 'use_column_width' in content:
            print("❌ Found deprecated 'use_column_width' parameter")
            return False
        
        if 'use_container_width' in content:
            print("❌ Found deprecated 'use_container_width' parameter")
            return False
        
        # Check for basic streamlit imports
        if 'import streamlit as st' not in content:
            print("❌ Missing streamlit import")
            return False
            
        print("✅ Streamlit app syntax check passed")
        return True
        
    except Exception as e:
        print(f"❌ Error reading streamlit app: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Bhumika's Portfolio...")
    print("=" * 40)
    
    tests = [
        test_file_structure,
        test_image_files,
        test_streamlit_syntax
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
        print()
    
    if all_passed:
        print("🎉 All tests passed! Portfolio is ready to run.")
        print("\nTo start the portfolio, run:")
        print("  pip install -r requirements.txt")
        print("  streamlit run src/streamlit_app.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()