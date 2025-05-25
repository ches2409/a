import reflex as rx

from arkadex.styles import styles
from arkadex.views.about import about
from arkadex.views.hero import hero


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        hero(),
        about(),
        background_image="url(bg_body.png)",
        background_repeat="no-repeat",
        background_size="60% 80%",
        background_position="50% 40%",
        width="100%",
        # height="100vh",
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index)
