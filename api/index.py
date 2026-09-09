import os
import sys

# Add project root directory to sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Import the main FastAPI application instance
from app import app

# Export both 'app' (for Vercel native ASGI) and 'handler' (for Lambda/Mangum)
try:
    from mangum import Mangum
    handler = Mangum(app)
except Exception:
    handler = app
