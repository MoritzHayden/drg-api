import csv
import requests
import json

from datetime import datetime, timedelta
from typing import Optional
from core.util.constants import DEEP_DIVE_METADATA_URL, DEEP_DIVE_INFORMATION_URL
from core.util.json_encoder import JSONEncoder
from v1.model.deep_dives import (
    Anomaly,
    Biome,
    Type,
    DeepDives,
    Stage,
    Variant,
    Warning
)


def get_deep_dive_metadata():
    response = requests.get(DEEP_DIVE_METADATA_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch deep dive metadata")


def get_deep_dive_information() -> str:
    response = requests.get(DEEP_DIVE_INFORMATION_URL)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to fetch deep dive information")


def construct_deep_dives(metadata: dict, information: str) -> DeepDives:
    # Unpack metadata
    expiration_time: datetime = datetime.fromisoformat(metadata["ExpirationTime"])
    end_time: str = expiration_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    start_time: str = (expiration_time - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = list(csv.reader(information.splitlines(), delimiter=','))

    # Construct Deep Dive Variant
    dd_seed: int = metadata["Seed"]
    dd_name: str = data[5][2]
    dd_biome: Biome = map_biome(data[6][2])
    dd_type: Type = Type.DEEP_DIVE
    dd_stage_1: Stage = Stage(id=1,
                              primary=data[8][2],
                              secondary=data[9][2],
                              anomaly=map_anomaly(data[10][3]),
                              warning=map_warning(data[10][2]))
    dd_stage_2: Stage = Stage(id=1,
                              primary=data[12][2],
                              secondary=data[13][2],
                              anomaly=map_anomaly(data[14][3]),
                              warning=map_warning(data[14][2]))
    dd_stage_3: Stage = Stage(id=1,
                              primary=data[16][2],
                              secondary=data[17][2],
                              anomaly=map_anomaly(data[18][3]),
                              warning=map_warning(data[18][2]))
    dd_variant: Variant = Variant(type=dd_type,
                                  name=dd_name,
                                  biome=dd_biome,
                                  seed=dd_seed,
                                  stages=[dd_stage_1, dd_stage_2, dd_stage_3])

    # Construct Elite Deep Dive Variant
    edd_seed: int = metadata["SeedV2"]
    edd_name: str = data[5][7]
    edd_biome: Biome = map_biome(data[6][7])
    edd_type: Type = Type.ELITE_DEEP_DIVE
    edd_stage_1: Stage = Stage(id=1,
                               primary=data[8][7],
                               secondary=data[9][7],
                               anomaly=map_anomaly(data[10][8]),
                               warning=map_warning(data[10][7]))
    edd_stage_2: Stage = Stage(id=1,
                               primary=data[12][7],
                               secondary=data[13][7],
                               anomaly=map_anomaly(data[14][8]),
                               warning=map_warning(data[14][7]))
    edd_stage_3: Stage = Stage(id=1,
                               primary=data[16][7],
                               secondary=data[17][7],
                               anomaly=map_anomaly(data[18][8]),
                               warning=map_warning(data[18][7]))
    edd_variant: Variant = Variant(type=edd_type,
                                   name=edd_name,
                                   biome=edd_biome,
                                   seed=edd_seed,
                                   stages=[edd_stage_1, edd_stage_2, edd_stage_3])

    return DeepDives(startTime=start_time, endTime=end_time, variants=[dd_variant, edd_variant])


def map_biome(biome: str) -> Optional[Biome]:
    try:
        return Biome(biome)
    except ValueError:
        return None


def map_anomaly(anomaly: str) -> Optional[Anomaly]:
    try:
        return Anomaly(anomaly)
    except ValueError:
        return None


def map_warning(warning: str) -> Optional[Warning]:
    try:
        return Warning(warning)
    except ValueError:
        return None


def save_json(schema: DeepDives):
    with open("v1/json/deep_dives.json", "w") as file:
        file.write(json.dumps(schema.dict(), cls=JSONEncoder, indent=2))


def refresh():
    # Fetch the deep dive metadata and information
    metadata = get_deep_dive_metadata()
    information = get_deep_dive_information()

    # Aggregate the deep dive data
    deep_dives = construct_deep_dives(metadata, information)

    # Save the deep dive data to a JSON file
    save_json(deep_dives)


if __name__ == "__main__":
    refresh()
