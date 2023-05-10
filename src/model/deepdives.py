from pydantic import BaseModel, Field
from enum import Enum


class Biome(str, Enum):
    """
    The biome which the Deep Dive variant takes place in.

    Enum Values:
    - Crystalline Caverns
    - Salt Pits
    - Fungus Bogs
    - Radioactive Exclusion Zone
    - Dense Biozone
    - Glacial Strata
    - Hollow Bough
    - Azure Weald
    - Magma Core
    - Sandblasted Corridors
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

    Enum Values:
    - Critical Weakness
    - Double XP
    - Gold Rush
    - Golden Bugs
    - Low Gravity
    - Mineral Mania
    - Rich Atmosphere
    - Volatile Guts
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

    Enum Values:
    - Cave Leech Cluster
    - Elite Threat
    - Exploder Infestation
    - Haunted Cave
    - Lethal Enemies
    - Low Oxygen
    - Mactera Plague
    - Parasites
    - Regenerative Bugs
    - Rival Presence
    - Shield Disruption
    - Swarmageddon
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
    A stage within of Deep Dive variant.

    Attributes:
    - id (int): The stage ID (e.g. 1, 2, 3).
    - primary (str): The primary objective for the stage.
    - secondary (str): The secondary objective for the stage.
    - anomaly (Anomaly | None): The anomaly for the stage, if any.
    - warning (Warning | None): The warning for the stage, if any.
    """
    id: int = Field(example=1)
    primary: str = Field(example="7 Aquarqs")
    secondary: str = Field(example="Black Box")
    anomaly: Anomaly | None
    warning: Warning | None


class Variant(BaseModel):
    """
    A variant of the Deep Dive.

    Attributes:
    - variant (str): The variant type (e.g. "Deep Dive", "Elite Deep Dive").
    - name (str): The name of the variant.
    - biome (str): The biome of the variant.
    - seed (int): The seed for the variant.
    - stages (list[Stage]): The stages within the variant.
    """
    variant: str = Field(example="Elite Deep Dive")
    name: str = Field(example="Morning Darkness")
    biome: Biome
    seed: int = Field(example=2775396360)
    stages: list[Stage]


class DeepDives(BaseModel):
    """
    A collection of the weekly Deep Dives.

    Attributes:
    - startTime (str): The start time of the Deep Dives event.
    - endTime (str): The end time of the Deep Dives event.
    - variants (list[Variant]): The variants of Deep Dives available during the event.
    """
    startTime: str = Field(example="2023-05-04T11:00:00Z")
    endTime: str = Field(example="2023-05-11T11:00:00Z")
    variants: list[Variant]
