#!/usr/bin/env python3
"""
Enhanced startup script for Bhumika's Portfolio with comprehensive error handling
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    """Setup environment variables to avoid permission issues"""
    # Set STREAMLIT_HOME to current directory to avoid permission issues
    os.environ['STREAMLIT_HOME'] = os.getcwd()
    
    # Disable telemetry to avoid permission issues
    os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
    
    # Set server configuration
    os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = 'false'
    os.environ['STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION'] = 'false'
    
    print("✅ Environment configured successfully")

def check_requirements():
    """Check if all requirements are installed"""
    try:
        import streamlit
        import pandas
        import numpy
        import requests
        print("✅ All Python packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Installing requirements...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Requirements installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install requirements")
            return False

def check_files():
    """Check if all required files exist"""
    required_files = [
        "src/streamlit_app.py",
        "src/assets/Bhumika_Photo.jfif",
        "src/assets/Presentation_Leadership_hackSRIT.jfif"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        print("Please ensure all required files are in place before running the portfolio.")
        return False
    
    print("✅ All required files are present")
    return True

def run_streamlit():
    """Run the Streamlit app with proper configuration"""
    try:
        # Create .streamlit directory if it doesn't exist
        streamlit_dir = Path(".streamlit")
        if not streamlit_dir.exists():
            streamlit_dir.mkdir(exist_ok=True)
            print("✅ Created .streamlit directory")
        
        print("🚀 Starting Bhumika's Portfolio...")
        print("📍 URL: http://localhost:8501")
        print("⏹️  Press Ctrl+C to stop the server")
        
        # Run streamlit with explicit configuration
        cmd = [
            sys.executable, "-m", "streamlit", "run", 
            "src/streamlit_app.py",
            "--server.port=8501",
            "--server.address=localhost",
            "--browser.gatherUsageStats=false",
            "--global.developmentMode=false"
        ]
        
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        print("\n✅ Portfolio stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Streamlit: {e}")
        print("Try running manually: streamlit run src/streamlit_app.py")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    """Main function to run the portfolio"""
    print("🎨 Bhumika's Portfolio Launcher")
    print("=" * 40)
    
    # Setup environment
    setup_environment()
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check files
    if not check_files():
        sys.exit(1)
    
    # Run the portfolio
    run_streamlit()

if __name__ == "__main__":
    main()