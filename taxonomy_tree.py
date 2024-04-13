from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

@dataclass 
class Clade:
    name: str 
    members: list[Clade]
    
    @staticmethod
    def build(taxonomies: list[list]) -> Clade:
        return Clade.clade_set(taxonomies)[0]

    @staticmethod 
    def clade_set(
        taxonomies: list[list],
        parent_name: Optional[str] = None, 
        index=0
    ) -> list[Clade]:
        names = list(set([
            taxonomy[index] 
            for taxonomy in taxonomies
            if Clade._safe_index_for(taxonomy, index) 
            and Clade._child_for(taxonomy, parent_name)
        ]))
        
        return [ 
            Clade(
                name=name, 
                members=Clade.clade_set(taxonomies, name, index + 1)
            ) for name in names
        ]

    @staticmethod
    def _child_for(
        taxonomy: list[str], parent_name: Optional[str]
    ) -> bool:
        return parent_name in taxonomy or not parent_name

    @staticmethod
    def _safe_index_for(taxonomy: list[str], index: int) -> bool:
        return index < len(taxonomy)
        
