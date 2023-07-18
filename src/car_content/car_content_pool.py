from dataclasses import dataclass, field
import random

from car_elements import CarElements

from mechanics.element import Element


@dataclass
class Detail:
    relation: str
    detail: str
    quantifier: str | None = None

    def text(self, adjective: str = None):
        quantifier = f"{self.quantifier} " if self.quantifier else ""
        if adjective:
            return f"{self.relation} {quantifier}{adjective} {self.detail}"
        return f"{self.relation} {quantifier}{self.detail}"

    def __hash__(self) -> int:
        return hash(self.detail)


@dataclass
class CarType:
    name: str
    details: list[Detail] = field(default_factory=list)

    def __hash__(self) -> int:
        return hash(self.name)
    

def with_detail(detail: str, quantifier: str = None) -> Detail:
    return Detail(relation="with", detail=detail, quantifier=quantifier)


WITH_MISSILE_LAUNCHER = with_detail("missile launcher", "a")
WITH_MACHINE_GUN = with_detail("machine gun", "a")
WITH_PLASMA_CANNON = with_detail("plasma cannon", "a")
WITH_RAILGUN = with_detail("railgun", "a")
WITH_ENERGY_BEAM_EMITTER = with_detail("energy beam emitter", "an")
WITH_GRENADE_LAUNCHER = with_detail("grenade launcher", "a")

WEAPONS = [
    WITH_MISSILE_LAUNCHER,
    WITH_MACHINE_GUN,
    WITH_PLASMA_CANNON,
    WITH_RAILGUN,
    WITH_ENERGY_BEAM_EMITTER,
    WITH_GRENADE_LAUNCHER,
]

WITH_REINFORCED_PLATING = with_detail("reinforced plating")
WITH_BULLETPROOF_GLASS = with_detail("bulletproof glass")
WITH_ELECTROMAGNETIC_SHIELD = with_detail("electromagnetic shield")
WITH_CARBON_NANOTUBE_ARMOR = with_detail("carbon nanotube armor")
WITH_ENERGY_ABSORBING_SHIELD = with_detail("energy-absorbing shield")

ARMOR = [
    WITH_REINFORCED_PLATING,
    WITH_BULLETPROOF_GLASS,
    WITH_ELECTROMAGNETIC_SHIELD,
    WITH_CARBON_NANOTUBE_ARMOR,
    WITH_ENERGY_ABSORBING_SHIELD,
]

WITH_STREAMLINED_FINS = with_detail("streamlined fins")
WITH_HYDRODYNAMIC_FINS = with_detail("hydrodynamic fins")
WITH_SONAR_FINS = with_detail("sonar fins")

FINS = [
    WITH_STREAMLINED_FINS,
    WITH_HYDRODYNAMIC_FINS,
    WITH_SONAR_FINS,
]

WITH_DUAL_EXHAUST_PIPES = with_detail("dual exhaust pipes")
WITH_FLAMING_EXHAUST = with_detail("flaming exhaust")
WITH_SMOKE_EMITTING_EXHAUST = with_detail("smoke-emitting exhaust")

EXHAUST = [
    WITH_DUAL_EXHAUST_PIPES,
    WITH_FLAMING_EXHAUST,
    WITH_SMOKE_EMITTING_EXHAUST,
]

WITH_LED_LIGHTS = with_detail("LED lights")
WITH_XENON_HEADLIGHTS = with_detail("xenon headlights")
WITH_NEON_UNDERGLOW = with_detail("neon underglow")

LIGHTS = [
    WITH_LED_LIGHTS,
    WITH_XENON_HEADLIGHTS,
    WITH_NEON_UNDERGLOW,
]

WITH_FUSION_REACTOR = with_detail("fusion reactor")
WITH_PLASMA_ENGINE = with_detail("plasma engine")
WITH_QUANTUM_GENERATOR = with_detail("quantum generator")

ENERGY_CORE = [
    WITH_FUSION_REACTOR,
    WITH_PLASMA_ENGINE,
    WITH_QUANTUM_GENERATOR,
]

WITH_AFTERBURNER = with_detail("afterburner")
WITH_TURBO_THRUSTER = with_detail("turbo thruster")
WITH_GRAVITIC_PROPULSION = with_detail("gravitic propulsion")

JET_ENGINE = [
    WITH_AFTERBURNER,
    WITH_TURBO_THRUSTER,
    WITH_GRAVITIC_PROPULSION,
]


# SEDAN = CarType("sedan", [
#     WITH_BULLETPROOF_GLASS,
#     WITH_REINFORCED_PLATING,
#     WITH_LED_LIGHTS,
# ])

SEDAN = CarType("sedan")

# SUV = CarType("SUV", [
#     WITH_BULLETPROOF_GLASS,
#     WITH_REINFORCED_PLATING,
#     WITH_ENERGY_ABSORBING_SHIELD,
# ])

# SUV = CarType("SUV")

# SPORTS_CAR = CarType("sports-car", [
#     WITH_MISSILE_LAUNCHER,
#     WITH_MACHINE_GUN,
#     WITH_PLASMA_CANNON,
#     WITH_RAILGUN,
#     WITH_ENERGY_BEAM_EMITTER,
#     WITH_GRENADE_LAUNCHER,
#     WITH_XENON_HEADLIGHTS,
# ])
SPORTS_CAR = CarType("sports-car")

# TRUCK = CarType("truck", [
#     WITH_BULLETPROOF_GLASS,
#     WITH_REINFORCED_PLATING,
#     WITH_DUAL_EXHAUST_PIPES,
# ])
# TRUCK = CarType("truck")

# MUSCLECAR = CarType("musclecar", [
#     WITH_MISSILE_LAUNCHER,
#     WITH_MACHINE_GUN,
#     WITH_PLASMA_CANNON,
#     WITH_RAILGUN,
#     WITH_ENERGY_BEAM_EMITTER,
#     WITH_GRENADE_LAUNCHER,
#     WITH_FLAMING_EXHAUST,
# ])
MUSCLECAR = CarType("musclecar")

# SUPERBIKE = CarType("superbike", [
#     WITH_TURBO_THRUSTER,
#     WITH_SMOKE_EMITTING_EXHAUST,
# ])
SUPERBIKE = CarType("superbike")

# CONCEPT_CAR = CarType("concept-car", [
#     WITH_AFTERBURNER,
#     WITH_BULLETPROOF_GLASS,
# ])
CONCEPT_CAR = CarType("concept-car")

# DRONE_RACER = CarType("drone-racer", [
#     WITH_QUANTUM_GENERATOR,
#     WITH_STREAMLINED_FINS,
# ])
DRONE_RACER = CarType("drone-racer")

# OFF_ROAD = CarType("off-road", [
#     WITH_REINFORCED_PLATING,
#     WITH_HYDRODYNAMIC_FINS,
# ])
OFF_ROAD = CarType("off-road")

# ARMORED_TRANSPORTER = CarType("armored-transporter", [
#     WITH_REINFORCED_PLATING,
#     WITH_ENERGY_ABSORBING_SHIELD,
#     WITH_RAILGUN,
# ])
ARMORED_TRANSPORTER = CarType("armored-transporter")

# HYPERCAR = CarType("hypercar", [
#     WITH_FUSION_REACTOR,
#     WITH_PLASMA_ENGINE,
# ])
HYPERCAR = CarType("hypercar")

# HOVERCRAFT = CarType("hovercraft", [
#     WITH_ENERGY_ABSORBING_SHIELD,
#     WITH_HYDRODYNAMIC_FINS,
#     WITH_SONAR_FINS,
# ])
HOVERCRAFT = CarType("hovercraft")

# JET_RACER = CarType("jet-racer", [
#     WITH_PLASMA_ENGINE,
#     WITH_AFTERBURNER,
# ])
JET_RACER = CarType("jet-racer")

# STEALTH_BIKE = CarType("stealth-bike", [
#     WITH_SMOKE_EMITTING_EXHAUST,
#     WITH_SONAR_FINS,
# ])
STEALTH_BIKE = CarType("stealth-bike")


TECHNO_BLADE = [SEDAN,SPORTS_CAR,MUSCLECAR,SUPERBIKE,ARMORED_TRANSPORTER,JET_RACER]
CYBER_BOOST = [SEDAN,SPORTS_CAR,MUSCLECAR,SUPERBIKE,CONCEPT_CAR,DRONE_RACER,HOVERCRAFT,STEALTH_BIKE]
# BIO_MECH = [SEDAN,SUV,TRUCK,MUSCLECAR,CONCEPT_CAR,HOVERCRAFT]
BIO_MECH = [SEDAN,  MUSCLECAR,CONCEPT_CAR,HOVERCRAFT]
ELECTRO_DRIVE = [SEDAN,SPORTS_CAR,MUSCLECAR,CONCEPT_CAR,HYPERCAR]
NANO_RACER = [SUPERBIKE,CONCEPT_CAR,HYPERCAR,JET_RACER,STEALTH_BIKE]
PLASMA_JET = [MUSCLECAR,SUPERBIKE,CONCEPT_CAR,DRONE_RACER,HYPERCAR,JET_RACER,STEALTH_BIKE]
QUANTUM_SHIFT = [SPORTS_CAR,MUSCLECAR,SUPERBIKE,CONCEPT_CAR,DRONE_RACER,HYPERCAR,STEALTH_BIKE]
STEALTH_SKULL = [SUPERBIKE,DRONE_RACER,HYPERCAR,JET_RACER,STEALTH_BIKE]
# HYPER_FORCE = [SEDAN,SUV,SPORTS_CAR,TRUCK,MUSCLECAR,OFF_ROAD,ARMORED_TRANSPORTER]
HYPER_FORCE = [SEDAN,SPORTS_CAR,MUSCLECAR,OFF_ROAD,ARMORED_TRANSPORTER]
# MECH_BEAST = [SUV,TRUCK,MUSCLECAR,OFF_ROAD,ARMORED_TRANSPORTER,STEALTH_BIKE]
MECH_BEAST = [MUSCLECAR,OFF_ROAD,ARMORED_TRANSPORTER,STEALTH_BIKE]

MODELS_BY_TYPE = {
    CarElements.TECHNO_BLADE: TECHNO_BLADE,
    CarElements.CYBER_BOOST: CYBER_BOOST,
    CarElements.BIO_MECH: BIO_MECH,
    CarElements.ELECTRO_DRIVE: ELECTRO_DRIVE,
    CarElements.NANO_RACER: NANO_RACER,
    CarElements.PLASMA_JET: PLASMA_JET,
    CarElements.QUANTUM_SHIFT: QUANTUM_SHIFT,
    CarElements.STEALTH_SKULL: STEALTH_SKULL,
    CarElements.HYPER_FORCE: HYPER_FORCE,
    CarElements.MECH_BEAST: MECH_BEAST,
}

# ENVIRONMENTS_BY_TYPE = {
# CarElements.TECHNO_BLADE: [
# "narrow and winding streets of a cyberpunk metropolis",
# "a network of labyrinthine underground tunnels",
# "an urban maze of intertwined buildings and futuristic skyscrapers",
# ],
# CarElements.CYBER_BOOST: [
# "futuristic highways suspended in the air",
# "a gravity-defying race track inside a transparent dome",
# "a circuit winding through an abandoned industrial zone",
# ],
# CarElements.BIO_MECH: [
# "an urban jungle where nature has reclaimed the city",
# "a secret laboratory filled with tubes and containers of genetic experiments",
# "a post-apocalyptic landscape with cybernetic ruins overrun by vegetation",
# ],
# CarElements.ELECTRO_DRIVE: [
# "a high-tech electric charging station in the heart of the city",
# "a race through a field of giant wind turbines and solar panels",
# "an electromagnetically charged track where vehicles glide frictionlessly",
# ],
# CarElements.NANO_RACER: [
# "a circuit through a network of nanorobots, where trajectories can transform at any moment",
# "a race inside a quantum computer, with moving fractal graphics",
# "an immersive virtual environment created by virtual reality",
# ],
# CarElements.PLASMA_JET: [
# "an urban desert with columns of fire and plasma storms",
# "a race through giant plasma tubes, where pilots must avoid deadly energy bolts",
# "a track located atop a plasma tower, featuring high-speed loops and jumps",
# ],
# CarElements.QUANTUM_SHIFT: [
# "a race through dimensional portals, where vehicles instantly shift from one point to another",
# "a circuit immersed in intense gravitational fields, where pilots must master spatio-temporal distortions",
# "a track built around a black hole, with extreme gravitational forces",
# ],
# CarElements.STEALTH_SKULL: [
# "a race in a dark and rainy quarter of the city, with narrow alleys and flickering neons",
# "a circuit through an abandoned industrial complex, with dark areas and motion detectors",
# "a nocturnal urban environment, with luminous holograms and shadows concealing traps",
# ],
# CarElements.HYPER_FORCE: [
# "a race on a floating platform above a precipice, with daring jumps and tight turns",
# "a circuit in a secret military compound, with dynamic obstacles and containment areas",
# "a cyberpunk battlefield, with explosions and debris littering the ground",
# ],
# CarElements.MECH_BEAST: [
# "a race through a polluted industrial zone, with toxic fumes and giant machinery",
# "a devastated urban battlefield, with debris and collapsed buildings",
# "a track set within a robot production facility, with assembly lines and moving mechanical arms",
# ],
# }

ENVIRONMENTS_BY_TYPE = {
CarElements.TECHNO_BLADE: [
"cyberpunk city streets",
"underground tunnels",
"futuristic skyscrapers",
],
CarElements.CYBER_BOOST: [
"suspended futuristic highways",
"gravity-defying race track",
"abandoned industrial zone",
],
CarElements.BIO_MECH: [
"urban jungle",
"genetic experiment laboratory",
"post-apocalyptic cybernetic ruins",
],
CarElements.ELECTRO_DRIVE: [
"high-tech electric charging station",
"field of giant wind turbines and solar panels",
"electromagnetically charged track",
],
CarElements.NANO_RACER: [
"network of nanorobots",
"quantum computer simulation",
"virtual reality environment",
],
CarElements.PLASMA_JET: [
"urban desert with plasma storms",
"giant plasma tubes",
"track atop a plasma tower",
],
CarElements.QUANTUM_SHIFT: [
"dimensional portals",
"gravitational field circuit",
"track around a black hole",
],
CarElements.STEALTH_SKULL: [
"dark and rainy urban quarter",
"abandoned industrial complex",
"nocturnal urban environment",
],
CarElements.HYPER_FORCE: [
"floating platform above a precipice",
"secret military compound",
"cyberpunk battlefield",
],
CarElements.MECH_BEAST: [
"polluted industrial zone",
"devastated urban battlefield",
"robot production facility",
],
}


GLOBAL_DETAIL_ADJECTIVES = [
"white",
"dark",
"golden",
"regal",
"ornate",
"ancient",
]

DETAIL_ADJECTIVES_BY_TYPE = {
CarElements.TECHNO_BLADE: ["sharp", "reflective", "metallic", "tapered", "pointed"],
CarElements.CYBER_BOOST: ["electrifying", "energetic", "turbo", "flashy", "dazzling"],
CarElements.BIO_MECH: ["organic", "biomechanical", "sinuous", "scaly", "mutant"],
CarElements.ELECTRO_DRIVE: ["electric", "scout", "electrochromic", "energy-intensive", "electromagnetic"],
CarElements.NANO_RACER: ["nanotechnological", "miniature", "futuristic", "digital", "programmable"],
CarElements.PLASMA_JET: ["plasma", "burning", "solar", "eruptive", "sparkling"],
CarElements.QUANTUM_SHIFT: ["quantum", "dematerialized", "enigmatic", "distorted", "ephemeral"],
CarElements.STEALTH_SKULL: ["stealthy", "obscure", "shadowy", "camouflaged", "dark"],
CarElements.HYPER_FORCE: ["powerful", "oversized", "overpowering", "imposing", "massive"],
CarElements.MECH_BEAST: ["mechanical", "robust", "industrial", "powerful", "epic"],
}

COLOR_BY_TYPE = {
CarElements.TECHNO_BLADE: "cyan",
CarElements.CYBER_BOOST: "light cyan",
CarElements.BIO_MECH: "light green",
CarElements.ELECTRO_DRIVE: "yellow",
CarElements.NANO_RACER: "magenta",
CarElements.PLASMA_JET: "purple",
CarElements.QUANTUM_SHIFT: "blue",
CarElements.STEALTH_SKULL: "dark gray",
CarElements.HYPER_FORCE: "red",
CarElements.MECH_BEAST: "orange",
}

AMBIENCE_BY_TYPE = {
CarElements.TECHNO_BLADE: [
"Neon blue lighting",
"Bright light lines",
"Futuristic nocturnal city backdrop",
"Electric circuit background",
],
CarElements.CYBER_BOOST: [
"Dynamic and colorful lighting",
"Flashing light effects",
"Holographic backdrop",
"Starry night sky",
],
CarElements.BIO_MECH: [
"Bioluminescent glow",
"Mysterious and organic atmosphere",
"Genetic laboratory background",
"Overgrown urban landscape",
],
CarElements.ELECTRO_DRIVE: [
"Vivid electric lighting",
"Sparkling energy effects",
"Dynamic electric lines background",
"Electrified twilight sky",
],
CarElements.NANO_RACER: [
"Fluid and changing lighting",
"Moving particle effects",
"Abstract digital world backdrop",
"Fractal architecture background",
],
CarElements.PLASMA_JET: [
"Burning plasma lighting",
"Flames and sparks effects",
"Energetically torn sky background",
"Thunder and lightning backdrop",
],
CarElements.QUANTUM_SHIFT: [
"Pulsating and strobe lighting",
"Spatio-temporal distortion effects",
"Black hole and galaxy background",
"Distorted futuristic urban landscape",
],
CarElements.STEALTH_SKULL: [
"Dark and contrasting lighting",
"Smoke and fog effects",
"Obscure urban alleyways backdrop",
"Neon-lit nocturnal sky",
],
CarElements.HYPER_FORCE: [
"Intense and powerful lighting",
"Speed and motion effects",
"Rushing urban landscapes backdrop",
"Starry night sky with light trails",
],
CarElements.MECH_BEAST: [
"Industrial and rugged lighting",
"Rusty metal and smoke effects",
"Post-apocalyptic environments background",
"Devastated urban landscape with debris and ruins",
],
}

ALL_SUBJECTS = [*TECHNO_BLADE,*CYBER_BOOST,*BIO_MECH,*ELECTRO_DRIVE,*NANO_RACER,*PLASMA_JET,*QUANTUM_SHIFT,*STEALTH_SKULL,*HYPER_FORCE,*MECH_BEAST]
ALL_SUBJECTS_BY_NAME = {subject.name: subject for subject in ALL_SUBJECTS}


def get_rarity_adjectives_set(rarity_index: int) -> set[str]:
    if rarity_index == 0:
        return {"simple", "basic"}
    if rarity_index == 1:
        return {"strong", "uncommon"}
    if rarity_index == 2:
        return {"rare", "special"}
    if rarity_index == 3:
        return {"epic", "mythical"}
    if rarity_index == 4:
        return {"legendary"}
    else:
        return {""}
    
def get_style_suffix(element: Element | None) -> set[str]:
    # if series_index == 0:
    #     return {"anime chibi drawing style, pastel background"}
    # if series_index == 1:
    #     return {"anime sketch with watercolor"}
    # if series_index == 2:
    #     return {"polished final by studio ghibli"}
    # else:
    #     return {"anime sketch"}
    # return {"polished final by studio ghibli"}
    return {f"anime sketch with {get_color(element)} watercolor"}
    
def get_random_style_suffix(element: Element | None) -> str:
    return random.choice(list(get_style_suffix(element)))


def get_random_rarity_adjective(rarity_index: int) -> str:
    return random.choice(list(get_rarity_adjectives_set(rarity_index)))


def get_model_types(element: Element) -> set[CarType]:
    return MODELS_BY_TYPE.get(element)

def get_closest_match(subject_override: str):
    if subject_override in ALL_SUBJECTS_BY_NAME:
        return ALL_SUBJECTS_BY_NAME[subject_override]
    else:
        # Create a new subject with the name of the override.
        return CarType(subject_override)


def get_environments(element: Element) -> set[str]:
    return ENVIRONMENTS_BY_TYPE.get(element)

def get_color(element: Element) -> set[str]:
    return COLOR_BY_TYPE.get(element)


def get_random_ambience(element: Element) -> str:
    # Get a random ambience, but don't return the last one, which is for fully evolved pokemon.
    return random.choice(AMBIENCE_BY_TYPE.get(element)[:-1])


def get_random_detail_adjective(element: Element) -> str:
    # joined_adjectives = GLOBAL_DETAIL_ADJECTIVES + DETAIL_ADJECTIVES_BY_TYPE.get(
    #     element
    # )
    # return random.choice(joined_adjectives)
    return random.choice(DETAIL_ADJECTIVES_BY_TYPE.get(element))