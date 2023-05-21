#base_components

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: 
    from engine import Engine
    from entity import Entity
    from game_map import GameMap

class BaseComponent: 
    eparent: Entity #owning entity instance

    @property
    def gamemap(self) -> GameMap: 
        return self.parent.gamemap

    @property
    def engine(self) -> Engine: 
        return self.gamemap.engine
    