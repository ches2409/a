from tkinter.constants import VERTICAL

import reflex as rx

from enum import Enum

from .colors import TextColor, Color
from .fonts import Font

MAX_WIDTH = "100vw"
MAX_HEIGHT = "100vh"

STYLESHEETS=[
    # "https://fonts.gstatic.com",
    "https://fonts.googleapis.com/css2?family=Aldrich&family=Bruno+Ace+SC&family=Electrolize&display=swap",
    "https://fonts.googleapis.com/css2?family=Audiowide&display=swap",
    "https://fonts.googleapis.com/css2?family=Orbitron:wght@400..900&display=swap"
    # "/static/styles.css"
]

class Size(Enum):
    ZERO = "0"
    XSMALL = "0.5em"
    SMALL = "0.7em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    DOUBLE="2em"
    LARGE = "3em"
    BIG = "4em"
    XBIG = "5em"
    BUTTON = "2.5em"

class Title():
    pass



BASE_STYLE={

    "background_color": Color.PRIMARY.value,

    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "border_radius":Size.DEFAULT
    }
}

font_title_style=dict(
    font_family=Font.TITLE.value,
    font_size=Size.BIG.value,
    color=TextColor.TITLE.value,
)
font_subtitle_style=dict(
    font_family=Font.SUBTITLE.value,
    font_size=Size.LARGE.value,
    color=TextColor.TITLE.value,
)
font_body_style=dict(
    font_family=Font.BODY.value,
    font_size=Size.LARGE.value,
    color=TextColor.TERTIARY.value,
)
font_vertical_style=dict(
    font_family=Font.VERTICAL.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.ACCENT.value,
    writing_mode= "vertical-lr",
)
font_button_style=dict(
    font_family=Font.BUTTON.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.SECONDARY.value,
)
font_accent_style=dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.ACCENT.value,
)
