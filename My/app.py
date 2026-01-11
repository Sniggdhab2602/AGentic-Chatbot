import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from langgraphagenticai.main import load_langgraph_agenticai_app

if __name__ == "__main__":
   load_langgraph_agenticai_app()