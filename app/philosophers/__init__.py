__all__ = [
    "AbstractPhilosopher",
    "Philosopher",
    "Philosopher",
    "SmartPhilosopher",
    "PhilosopherWithWaiter",
    "PhilosopherWithNummeredForks"
]

from .abstract import AbstractPhilosopher
from .basic import Philosopher
from .smart import SmartPhilosopher
from .waiter import PhilosopherWithWaiter
from .nummered import PhilosopherWithNummeredForks