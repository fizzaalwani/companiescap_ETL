import logging
from pathlib import Path
from datetime import datetime


# Project root
APP_DIR = Path(__file__).resolve().parent.parent

# Today's date
DATE = datetime.now().strftime("%Y-%m-%d")

# logs/YYYY-MM-DD
LOG_DIR = APP_DIR / "logs" / DATE

LOG_DIR.mkdir(parents=True, exist_ok=True)

# logs/YYYY-MM-DD/app.log
LOG_FILE = LOG_DIR / "app.log"


logging.basicConfig(
    level=logging.DEBUG,
    filename=LOG_FILE,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

