import reflex as rx

from arkadex.styles import styles
from arkadex.views.about import about
from arkadex.views.hero import hero
from arkadex.views.teams import teams


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        rx.box(
            hero(),
            about(),
            background_image="url(bg_body.png)",
            background_repeat="no-repeat",
            background_size="60% 130vh",
            background_position="50% 10%",
        ),
        teams(),

        width="100%",
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index)
