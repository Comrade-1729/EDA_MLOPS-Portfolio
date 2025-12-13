# bootstrap.py at top of notebook
from pathlib import Path
import sys
import os

PROJECT_ROOT = Path(__file__).parent.parent
os.chdir(PROJECT_ROOT)

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
