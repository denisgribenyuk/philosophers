import logging
import random
import time
from threading import Semaphore

from .basic import Philosopher
from ..enums import Side
from ..forks import Fork

logger = logging.getLogger(__name__)


class PhilosopherWithNummeredForks(Philosopher):
    """Represents thinker man."""
    def process(self) -> None:
        side_ordered = [side for side, fork in sorted(self.forks.items(), key=lambda item: item[1].id)]
        logger.info("%r join the table", self)

        while self.is_hungry:
            for side in side_ordered:
                self._get_fork(side)
            self._eat()

            for side in side_ordered:
                self._return_fork(side)

        logger.info("%r left the table", self)
