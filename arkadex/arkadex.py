import reflex as rx

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


app = rx.App()
app.add_page(index)
