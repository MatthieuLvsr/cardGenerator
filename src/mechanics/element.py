from dataclasses import dataclass, field


@dataclass
class Element:
    name: str
    ascii_color: str = None

    def with_ascii_color(self, text: str) -> str:
        if self.ascii_color is None:
            return text
        return f"{self.ascii_color}{text}\033[0m"

    def __repr__(self):
        return self.name

    def ascii_name(self):
        return self.with_ascii_color(self.name)

    def __hash__(self) -> int:
        return hash(self.name)