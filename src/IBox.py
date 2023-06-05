#Python import
from typing import TypedDict

class IBox(TypedDict):
    item : str
    description: str
    vendorCode: str
    vendor: str
    prodLine : str
