import logging
import random
import time
from threading import Semaphore

from .basic import Philosopher
from ..enums import Side
from ..forks import Fork

logger = logging.getLogger(__name__)


class PhilosopherWithWaiter(Philosopher):
    """Represents thinker man."""
    def __init__(
        self,
        name: str,
        left_fork: Fork,
        right_fork: Fork,
            waiter: Semaphore
    ):
        super().__init__(name=name, left_fork=left_fork, right_fork=right_fork)
        self.waiter = waiter

    def _get_fork(self, side: Side) -> None:
        """Get fork from side."""
        with self.waiter:
            super()._get_fork(side)
