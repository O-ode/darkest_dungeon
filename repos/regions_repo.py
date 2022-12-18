from model.region_model import RegionModel


class RegionsRepo:
    _regions: list[RegionModel] = []
    _enemies_per_region: dict[str:str] = {}

    @classmethod
    def add_region_and_enemy_names(cls, region_name, enemy_names):
        region = RegionModel(region_name)
        cls._regions.append(region)
        cls._enemies_per_region.update({region_name: enemy_names})
