"""Unit API."""

from typing import Any, Protocol, Self, runtime_checkable

__version__ = "0.0.1.dev0"
__all__ = ["Unit"]

type Dimension = Any  # TODO: dimension-api
type Quantity = Any  # TODO: quantity-api

@runtime_checkable
class Unit(Protocol):
    @property
    def dimension(self) -> Dimension: ...

    def __eq__(self, other: Self, /) -> bool: ...
    def __mul__(self, other: Self, /) -> Self: ...
    def __div__(self, other: Self, /) -> Self: ...
    def __pow__(self, other: int | Self, /) -> Self: ...

    # debatable whether this should be standardised
    def __rlshift__[V](self, other: V) -> Quantity[V, Self]: ...
