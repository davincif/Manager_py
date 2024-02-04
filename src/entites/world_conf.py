from engine_layer import EngineLayer


class WorldConf:
    """Holds all properties of customization available for the world."""

    world_size_x: int
    world_size_y: int
    generation__seed: float
    generation__biome_inertia: float
    generation__heat_loss: float
    generation__reheat_per_contiguos_title: float
    generation__reheat_cap: float
    generation__reheat_ignore_neighborn_threshold: float
    generation__conside_biome_on_diagonal: bool

    def load(self, conf_file="src/default.conf.yml"):
        """Loads all the customization for the world generation in the configuration file.

        Args:
            conf_file: where the configuration file is.
        """
        conf = EngineLayer.configLoader(conf_file)

        [self.world_size_x, self.world_size_y] = conf["world"]["size"]
        self.generation__seed = conf["world"]["generation"]["seed"]
        self.generation__biome_inertia = conf["world"]["generation"]["biome_inertia"]
        self.generation__heat_loss = conf["world"]["generation"]["heat_loss"]
        self.generation__heat_loss = conf["world"]["generation"]["heat_loss"]
        self.generation__reheat_per_contiguos_title = conf["world"]["generation"][
            "reheat_per_contiguos_title"
        ]
        self.generation__reheat_cap = conf["world"]["generation"]["reheat_cap"]
        self.generation__reheat_ignore_neighborn_threshold = conf["world"][
            "generation"
        ]["reheat_ignore_neighborn_threshold"]
        self.generation__conside_biome_on_diagonal = conf["world"]["generation"][
            "conside_biome_on_diagonal"
        ]
