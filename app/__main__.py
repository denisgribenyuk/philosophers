import logging

from app import start_dinner
from app.tables import (
    Table,
TableWithSmartPhilosophers,
TableWithWaiter,
TableWithNummeredForks
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

start_dinner(TableWithNummeredForks)
