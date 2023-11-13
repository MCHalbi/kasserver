from dataclasses import dataclass
from typing import Iterator, Tuple


@dataclass(frozen=True)
class KasAuth:
    login: str
    passphrase: str
    type: str

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        return iter(
            [
                ("kas_login", self.login),
                ("kas_auth_type", self.type),
                ("kas_auth_data", self.passphrase),
            ]
        )
