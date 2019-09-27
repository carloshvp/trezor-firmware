# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class DebugLinkLayout(p.MessageType):
    MESSAGE_WIRE_TYPE = 9001

    def __init__(
        self,
        lines: List[str] = None,
    ) -> None:
        self.lines = lines if lines is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('lines', p.UnicodeType, p.FLAG_REPEATED),
        }
