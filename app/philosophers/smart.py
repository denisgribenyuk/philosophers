import logging
import random
import time

from .abstract import AbstractPhilosopher
from ..enums import Side

logger = logging.getLogger(__name__)


class SmartPhilosopher(AbstractPhilosopher):
    """Represents thinker man."""

    def process(self) -> None:
        """Start dine."""
        logger.info("%r join the table", self)

        while self.is_hungry:
            self._get_both_forks()
            self._eat()
            self._return_fork()

        logger.info("%r left the table", self)

    def _get_both_forks(self) -> None:
        """Get fork from side."""
        got_left = got_right = False
        while not got_left or not got_right:
            got_left = self.forks[Side.LEFT].acquire(blocking=False)
            got_right = self.forks[Side.RIGHT].acquire(blocking=False)

            if not (got_left and got_right):
                if got_left:
                    self.forks[Side.LEFT].release()
                if got_right:
                    self.forks[Side.RIGHT].release()

        time.sleep(random.random())
        logger.info("%r get both forks from the table", self)

    def _return_fork(self) -> None:
        """Return fork back."""
        self.forks[Side.LEFT].release()
        self.forks[Side.RIGHT].release()
        logger.info("%r return both forks from the table", self)
        time.sleep(random.random())
