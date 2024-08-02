import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

BOT_TOKEN: str = os.getenv("TOKEN", "*****")

# Time wait in secs after each error
TIMED_OUT_PAUSE: int = 15
