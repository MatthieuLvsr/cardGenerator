from mechanics.element import Element


class CarElements:
    TECHNO_BLADE = Element(
        "Techno-Blade",
        ascii_color="\033[36m",  # Cyan
    )
    CYBER_BOOST = Element(
        "Cyber-Boost",
        ascii_color="\033[96m",  # Light Cyan
    )
    BIO_MECH = Element(
        "Bio-Mech",
        ascii_color="\033[92m",  # Light Green
    )
    ELECTRO_DRIVE = Element(
        "Electro-Drive",
        ascii_color="\033[93m",  # Yellow
    )
    NANO_RACER = Element(
        "Nano-Racer",
        ascii_color="\033[95m",  # Magenta
    )
    PLASMA_JET = Element(
        "Plasma-Jet",
        ascii_color="\033[35m",  # Purple
    )
    QUANTUM_SHIFT = Element(
        "Quantum-Shift",
        ascii_color="\033[94m",  # Blue
    )
    STEALTH_SKULL = Element(
        "Stealth-Skull",
        ascii_color="\033[90m",  # Dark Gray
    )
    HYPER_FORCE = Element(
        "Hyper-Force",
        ascii_color="\033[91m",  # Red
    )
    MECH_BEAST = Element(
        "Mech-Beast",
        ascii_color="\033[33m",  # Orange
    )

    ALL = [
        TECHNO_BLADE, CYBER_BOOST, BIO_MECH, ELECTRO_DRIVE,
        NANO_RACER, PLASMA_JET, QUANTUM_SHIFT, STEALTH_SKULL,
        HYPER_FORCE, MECH_BEAST
    ]
    _ELEMENTS_BY_NAME = {element.name.lower(): element for element in ALL}

    def get_element_by_name(name: str) -> Element:
        return CarElements._ELEMENTS_BY_NAME[name.lower()]
