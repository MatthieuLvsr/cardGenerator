from mechanics.rarity import Rarity


class CarRarity:
    COMMON = Rarity("common", 0)
    UNCOMMON = Rarity("uncommon", 1)
    RARE = Rarity("rare", 2)
    MYTHIC = Rarity("mythic", 3)
    LEGENDARY = Rarity("legendary", 4)

    ALL = [
        COMMON,
        UNCOMMON,
        RARE,
        MYTHIC,
        LEGENDARY,
    ]

    RARITY_BY_NAME = {rarity.name: rarity for rarity in ALL}

    @classmethod
    def get_rarity_by_name(cls, name: str) -> Rarity:
        if name not in cls.RARITY_BY_NAME:
            return cls.RARE
        return cls.RARITY_BY_NAME[name]
