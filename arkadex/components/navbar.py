import reflex as rx

from arkadex.styles import styles


def navbar()->rx.Component:
    return rx.vstack(
        # rx.spacer(),
        rx.text(
            "Where legends rise",
            style=styles.font_title_style,
        ),
        rx.hstack(
            rx.spacer(),
            rx.hstack(
                rx.image(
                    src="user-plus.png",
                    height="1.5em",
                ),
                "Registrate",
                style=styles.font_horizontal_button_style,
            ),
            rx.hstack(
                rx.image(
                    src="chart-simple.png",
                    height="1.5em",
                ),
                "Informate",
                style=styles.font_horizontal_button_style,
            ),
            spacing="8",
            # bg="orange",
            align="end",
            width="65%",
        ),
        # bg="blue",
        spacing="1",
        width="100%",
        height="100%",
    )

