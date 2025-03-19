import os
import sys
from pathlib import Path
from streamlit.web import cli


def app():
    # Get the directory containing this script
    current_dir = Path(__file__).parent
    main_path = current_dir / "main.py"
    
    sys.argv = [
        "streamlit",
        "run",
        str(main_path),
    ]
    cli.main()
