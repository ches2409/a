import reflex as rx

from arkadex.styles import styles
from arkadex.views.header import header
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.center(
        header(),
        width="100%"
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index)
