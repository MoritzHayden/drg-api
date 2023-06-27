from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Type(str, Enum):
    """
    The type of the Deep Dive variant.
    """
    DEEP_DIVE = "Deep Dive"
    ELITE_DEEP_DIVE = "Elite Deep Dive"


class Biome(str, Enum):
    """
    The biome which the Deep Dive variant takes place in.
    """
    CRYSTALLINE_CAVERNS = "Crystalline Caverns"
    SALT_PITS = "Salt Pits"
    FUNGUS_BOGS = "Fungus Bogs"
    RADIOACTIVE_EXCLUSION_ZONE = "Radioactive Exclusion Zone"
    DENSE_BIOZONE = "Dense Biozone"
    GLACIAL_STRATA = "Glacial Strata"
    HOLLOW_BOUGH = "Hollow Bough"
    AZURE_WEALD = "Azure Weald"
    MAGMA_CORE = "Magma Core"
    SANDBLASTED_CORRIDORS = "Sandblasted Corridors"


class Anomaly(str, Enum):
    """
    An anomaly that can appear in a Deep Dive stage.
    """
    CRITICAL_WEAKNESS = "Critical Weakness"
    DOUBLE_XP = "Double XP"
    GOLD_RUSH = "Gold Rush"
    GOLDEN_BUGS = "Golden Bugs"
    LOW_GRAVITY = "Low Gravity"
    MINERAL_MANIA = "Mineral Mania"
    RICH_ATMOSPHERE = "Rich Atmosphere"
    VOLATILE_GUTS = "Volatile Guts"


class Warning(str, Enum):
    """
    A warning that can appear in a Deep Dive stage.
    """
    CAVE_LEECH_CLUSTER = "Cave Leech Cluster"
    ELITE_THREAT = "Elite Threat"
    EXPLODER_INFESTATION = "Exploder Infestation"
    HAUNTED_CAVE = "Haunted Cave"
    LETHAL_ENEMIES = "Lethal Enemies"
    LOW_OXYGEN = "Low Oxygen"
    MACTERA_PLAGUE = "Mactera Plague"
    PARASITES = "Parasites"
    REGENERATIVE_BUGS = "Regenerative Bugs"
    RIVAL_PRESENCE = "Rival Presence"
    SHIELD_DISRUPTION = "Shield Disruption"
    SWARMAGEDDON = "Swarmageddon"


class Stage(BaseModel):
    """
    A stage within the Deep Dive variant.
    """
    id: int = Field(description="The sequencing index for the stage.",
                    example=1)
    primary: str = Field(description="The primary objective for the stage.",
                         example="7 Aquarqs")
    secondary: str = Field(description="The secondary objective for the stage.",
                           example="Black Box")
    anomaly: Optional[Anomaly] = Field(default=None,
                                       description="The anomaly for the stage, if any.",
                                       example="Critical Weakness")
    warning: Optional[Warning] = Field(default=None,
                                       description="The warning for the stage, if any.", example="Cave Leech Cluster")


class Variant(BaseModel):
    """
    A Deep Dive variant.
    """
    type: Type = Field(description="The type of the variant.",
                       example="Elite Deep Dive")
    name: str = Field(description="The name of the variant.",
                      example="Morning Darkness")
    biome: Biome = Field(description="The biome of the variant.",
                         example="Crystalline Caverns")
    seed: int = Field(description="The seed for the variant.",
                      example=2775396360)
    stages: list[Stage] = Field(description="The stages within the variant.")


class DeepDives(BaseModel):
    """
    A collection of the weekly Deep Dives.
    """
    startTime: str = Field(description="The ISO 8601 start time of the Deep Dives.",
                           example="2023-05-11T11:00:00Z")
    endTime: str = Field(description="The ISO 8601 end time of the Deep Dives.",
                         example="2023-05-18T11:00:00Z")
    variants: list[Variant] = Field(description="The Deep Dive variants.")
