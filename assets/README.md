# Game assets

Add your images, sounds, fonts, and other game assets here. The starter movement
demo does not require any assets.

Resolve paths from your source file rather than the current working directory:

```python
from pathlib import Path
ASSETS = Path(__file__).resolve().parents[1] / "assets"
```

Include this directory in your game's py2ports manifest when packaging. Check
the license and attribution requirements of any assets you add.
