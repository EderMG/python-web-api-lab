"""Configuración para pytest."""
import sys
from pathlib import Path

# Agregar la raíz del proyecto al path de Python
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
