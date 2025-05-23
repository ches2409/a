from tkinter.constants import VERTICAL

import reflex as rx

from enum import Enum

from .colors import TextColor, Color
from .fonts import Font

MAX_WIDTH = "100vw"
MAX_HEIGHT = "100vh"

STYLESHEETS=[
    "https://fonts.googleapis.com",
    "https://fonts.gstatic.com",
    "https://fonts.googleapis.com/css2?family=Aldrich&family=Bruno+Ace+SC&family=Electrolize&display=swap",
    "https://fonts.googleapis.com/css2?family=Bruno+Ace&display=swap",
    "https://fonts.googleapis.com/css2?family=Electrolize&display=swap"
    # "/static/styles.css"
]

class Size(Enum):
    ZERO = 0
    XSMALL = 0.5
    SMALL = 0.7
    DEFAULT = 1
    MEDIUM = 1.5
    DOUBLE=2
    LARGE = 3
    BIG = 4
    XBIG = 5
    BUTTON = 2.5

class Title():
    pass

BASE_STYLE={

    "background_color": Color.PRIMARY.value,

    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "border_radius":f"{Size.DEFAULT}em"
    },

    "TITLE": {
        "font_family": Font.TITLE.value,
        "font_size": f"{Size.BIG.value}em",
        "color": TextColor.TITLE.value,
    },
    "SUBTITLE":{
        "font_family": Font.TITLE.value,
        "font_size":f"{Size.LARGE.value}em",
        "color": TextColor.TITLE.value,
    },
    "BODY":{
        "font_family": Font.BODY.value,
        "font_size":f"{Size.XBIG.value}em",
        "color": TextColor.TERTIARY.value,
    },
    "VERTICAL":{
        "font_family": Font.VERTICAL.value,
        "font_size":f"{Size.MEDIUM.value}em",
        "color": TextColor.ACCENT.value,
        "writing_mode": "vertical-lr",
        # "text-orientation": "mixed",
    }

}
