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
        root_name: Optional[str] = None, 
        index=0
    ) -> list[Clade]:
        names = []
        for taxonomy in taxonomies:
            if index >= len(taxonomy):
                continue
            if (
                taxonomy[index] not in names
            ) and (
                root_name in taxonomy or not root_name
            ):
                names.append(taxonomy[index])
        
        return [
            Clade(
                name=name, 
                members=Clade.clade_set(
                    taxonomies, name, index + 1
                )
            ) for name in names
        ]
   
