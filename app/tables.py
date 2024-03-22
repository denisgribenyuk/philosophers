__all__ = [
    "Table",
    # "TableWithNumberedForks",
    # "TableWithSmartPhilosophers",
    "TableWithWaiter",
    "Philosopher",
    "PhilosopherWithNummeredForks",
    "SmartPhilosopher",
    "PhilosopherWithWaiter",
]

from threading import Semaphore
from typing import List, Type

from app.forks import Fork
from app.philosophers import (
    AbstractPhilosopher,
    Philosopher,
    SmartPhilosopher,
    PhilosopherWithWaiter,
PhilosopherWithNummeredForks
)

DEFAULT_SEATS = 5


class Table:
    """Represents Table with Philosophers.

    This is example of blocking state.
    Every philosopher took the left fork and then will forever await
    for the right fork.
    """

    philosopher_class: Type[AbstractPhilosopher] = Philosopher

    def __init__(
        self,
        seats: int = DEFAULT_SEATS,
    ):
        self.seats = seats
        self.forks = [Fork(i) for i in range(seats)]
        self.philosophers: List[AbstractPhilosopher] = []

    def seat_philosophers(self) -> None:
        """Seat philosophers to their seats."""
        self.philosophers = [
            self.philosopher_class(
                name=str(i),
                left_fork=self.forks[i],
                right_fork=self.forks[(i + 1) % self.seats],
            )
            for i in range(self.seats)
        ]

class TableWithSmartPhilosophers(Table):
    philosopher_class: Type[AbstractPhilosopher] = SmartPhilosopher

class TableWithWaiter(Table):
    philosopher_class: Type[AbstractPhilosopher] = PhilosopherWithWaiter
    def seat_philosophers(self) -> None:
        """Seat philosophers to their seats."""
        waiter = Semaphore(len(self.forks) - 1)
        self.philosophers = [
            self.philosopher_class(
                name=str(i),
                left_fork=self.forks[i],
                right_fork=self.forks[(i + 1) % self.seats],
                waiter=waiter
            )
            for i in range(self.seats)
        ]

class TableWithNummeredForks(Table):
    philosopher_class: Type[AbstractPhilosopher] = PhilosopherWithNummeredForks