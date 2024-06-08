from engine_layer.interfaces.engine_layer_interface import EngineConfigurationsType


class _GlobalTerrainsProps:
    is_constructable: bool
    symbol: str
    graphic_symbol: str
    font_color: str


class _GlobalTerrains:
    grass: _GlobalTerrainsProps
    water: _GlobalTerrainsProps
    forest: _GlobalTerrainsProps
    mountains: _GlobalTerrainsProps

    def __init__(self):
        self.grass = _GlobalTerrainsProps()
        self.water = _GlobalTerrainsProps()
        self.forest = _GlobalTerrainsProps()
        self.mountains = _GlobalTerrainsProps()


class _Generation:
    seed: float
    biome_inertia: float
    heat_loss: float
    reheat_per_contiguos_title: float
    reheat_cap: float
    reheat_ignore_neighborn_threshold: float
    conside_biome_on_diagonal: bool


class WorldConf:
    """Holds all properties of customization available for the world."""

    world_size_x: int
    world_size_y: int

    generation: _Generation
    global_terrains: _GlobalTerrains

    def __init__(self):
        self.generation = _Generation()
        self.global_terrains = _GlobalTerrains()

    def load(self, conf: EngineConfigurationsType):
        """Loads all the customization for the world generation in the configuration file.

        Args:
            conf_file: where the configuration file is.
        """
        [self.world_size_x, self.world_size_y] = conf["world"]["size"]

        ## Generation settings
        self.generation.seed = conf["world"]["generation"]["seed"]
        self.generation.biome_inertia = conf["world"]["generation"]["biome_inertia"]
        self.generation.heat_loss = conf["world"]["generation"]["heat_loss"]
        self.generation.heat_loss = conf["world"]["generation"]["heat_loss"]
        self.generation.reheat_per_contiguos_title = conf["world"]["generation"][
            "reheat_per_contiguos_title"
        ]
        self.generation.reheat_cap = conf["world"]["generation"]["reheat_cap"]
        self.generation.reheat_ignore_neighborn_threshold = conf["world"]["generation"][
            "reheat_ignore_neighborn_threshold"
        ]
        self.generation.conside_biome_on_diagonal = conf["world"]["generation"][
            "conside_biome_on_diagonal"
        ]

        ## Global Terrains settings
        # Grass settings
        self.global_terrains.grass.is_constructable = conf["world"]["global_terrains"][
            "GRASS"
        ]["is_constructable"]
        self.global_terrains.grass.symbol = conf["world"]["global_terrains"]["GRASS"][
            "symbol"
        ]
        self.global_terrains.grass.graphic_symbol = conf["world"]["global_terrains"][
            "GRASS"
        ]["graphic_symbol"]
        self.global_terrains.grass.font_color = conf["world"]["global_terrains"][
            "GRASS"
        ]["font_color"]

        # Water settings
        self.global_terrains.water.is_constructable = conf["world"]["global_terrains"][
            "WATER"
        ]["is_constructable"]
        self.global_terrains.water.symbol = conf["world"]["global_terrains"]["WATER"][
            "symbol"
        ]
        self.global_terrains.water.graphic_symbol = conf["world"]["global_terrains"][
            "WATER"
        ]["graphic_symbol"]
        self.global_terrains.water.font_color = conf["world"]["global_terrains"][
            "WATER"
        ]["font_color"]

        # Forest settings
        self.global_terrains.forest.is_constructable = conf["world"]["global_terrains"][
            "FOREST"
        ]["is_constructable"]
        self.global_terrains.forest.symbol = conf["world"]["global_terrains"]["FOREST"][
            "symbol"
        ]
        self.global_terrains.forest.graphic_symbol = conf["world"]["global_terrains"][
            "FOREST"
        ]["graphic_symbol"]
        self.global_terrains.forest.font_color = conf["world"]["global_terrains"][
            "FOREST"
        ]["font_color"]

        # Mountains settings
        self.global_terrains.mountains.is_constructable = conf["world"][
            "global_terrains"
        ]["MOUNTAINS"]["is_constructable"]
        self.global_terrains.mountains.symbol = conf["world"]["global_terrains"][
            "MOUNTAINS"
        ]["symbol"]
        self.global_terrains.mountains.graphic_symbol = conf["world"][
            "global_terrains"
        ]["MOUNTAINS"]["graphic_symbol"]
        self.global_terrains.mountains.font_color = conf["world"]["global_terrains"][
            "MOUNTAINS"
        ]["font_color"]
