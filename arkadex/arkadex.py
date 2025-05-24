import reflex as rx
from pygments.styles.dracula import background

from arkadex.styles import styles

from arkadex.views.header import header
from arkadex.views.about import about


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.vstack(
        header(),
        about(),
        # background_image="url(logoVertical.png)",
        # background_repeat="no-repeat",
        # background_size="auto 100%",
        # background_position="center",
        width="100%",
        # height="100vh",
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index)
