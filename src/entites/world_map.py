from utils.luky import choose_from, update_seed
from .enums.world_tile_type import WorldTitleType
from .world_conf import WorldConf
from .world_tile import WorldTile

type heat_mash = dict[WorldTitleType, float]
type heat_map = list[list[heat_mash]]


class WorldMap:
    map: list[list[WorldTile]]
    conf: WorldConf

    def __init__(self) -> None:
        self.conf = WorldConf()
        self.conf.load()

        update_seed(self.conf.generation.seed)
        self.__generate()

    def __generate(self):
        self.map = self.__create_empty_map()

        self._generate_biomes()

    def __create_empty_map(self):
        new_map: list[list[WorldTile]] = []

        for i in range(self.conf.world_size_y):
            new_map.append([])

            for j in range(self.conf.world_size_x):
                title = WorldTile((i, j))
                new_map[i].append(title)

        return new_map

    def _generate_biomes(self):
        heatmap: heat_map = []

        # initial terrain
        self.map[0][0].type = choose_from(WorldTitleType.get_value_list())

        # generate all tarrains
        for i in range(self.conf.world_size_y):
            if i > 0:
                heatmap.append([])

            for j in range(self.conf.world_size_x):
                if i == 0 and j == 0:
                    heatmap.append(
                        [{self.map[0][0].type: self.conf.generation.biome_inertia}]
                    )
                else:
                    current_heatmap = self.__calculate_heat_mash(
                        cell=(i, j),
                        heatmap=heatmap,
                        consider_diagonal=self.conf.generation.conside_biome_on_diagonal,
                    )
                    heatmap[i].append(current_heatmap)
                    self.__add_title_change_chances_to_heatmash(current_heatmap)

                    new_biome = choose_from(
                        list(current_heatmap.keys()), list(current_heatmap.values())
                    )

                    self.map[i][j].set_biome(new_biome, self.conf.global_terrains)

    def __add_title_change_chances_to_heatmash(self, heatmashes: heat_mash):
        biggest_probability = max(heatmashes.values())
        heatmashes[WorldTitleType.NONE] = 1 - biggest_probability

    def __calculate_heat_mash(
        self, cell: tuple[int, int], heatmap: heat_map, consider_diagonal: bool
    ) -> heat_mash:
        cooled_down_heatmashs: list[heat_mash] = []

        cells_to_check: list[tuple[int, int]] = []
        last_i = cell[0] - 1
        last_j = cell[1] - 1
        next_j = cell[1] + 1

        # ortogonal
        if last_i >= 0:
            cells_to_check.append((last_i, cell[1]))
        if last_j >= 0:
            cells_to_check.append((cell[0], last_j))

        # diagonal
        if consider_diagonal:
            if last_i >= 0:
                if last_j >= 0:
                    cells_to_check.append((last_i, last_j))
                if next_j < self.conf.world_size_x:
                    cells_to_check.append((last_i, next_j))

        # cooldown heat mashes
        for cell in cells_to_check:
            heatmash = {**heatmap[cell[0]][cell[1]]}
            cooled_down_heatmashs.append(heatmash)
            biomes_to_remove = []
            for biome in heatmash:
                if heatmash[biome] <= self.conf.generation.heat_loss:
                    biomes_to_remove.append(biome)
                else:
                    heatmash[biome] -= self.conf.generation.heat_loss
            for biome in biomes_to_remove:
                del heatmash[biome]

        return self.__averege_heat_from(cooled_down_heatmashs)

    def __averege_heat_from(self, heatmashes: list[heat_mash]) -> heat_mash:
        average_heat_map: heat_mash = {}
        all_heats: dict[WorldConf, list[float]] = {}

        # gather all hearts together
        for heatmash in heatmashes:
            for biome in heatmash:
                if biome in all_heats:
                    all_heats[biome].append(heatmash[biome])
                else:
                    all_heats[biome] = [heatmash[biome]]

        # avarage all biomes with reheat
        for biome in all_heats:
            similar_titles = len(all_heats[biome])
            reheat_intensity = min(
                max(
                    similar_titles
                    - self.conf.generation.reheat_ignore_neighborn_threshold,
                    0,
                )
                * self.conf.generation.reheat_per_contiguos_title,
                self.conf.generation.reheat_cap,
            )
            average_heat_map[biome] = (
                sum(all_heats[biome]) / similar_titles + reheat_intensity
            )

        return average_heat_map
