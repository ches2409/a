import reflex as rx

from arkadex.styles import styles
from arkadex.styles.colors import TextColor
from arkadex.styles.styles import Size


def card_team(
        image:str,
        subtitle:str,
        description:str,
        gaming_style_1:str,
        gaming_style_2:str,
        gaming_style_3:str,
)->rx.Component:
    return rx.hstack(
    rx.flex(
        rx.image(
            src=f"{image}.png",
            height="100%",

        ),
        justify_content="flex-end",
        height="50%",
        width="35%",
        # bg="red"
    ),
    rx.vstack(
        rx.flex(
            rx.text(
                subtitle,
                style=styles.font_default_style,
                font_size=Size.DOUBLE.value,
                align="center",

            ),
            align="center",
            justify="center",
            # bg="orange",
            width="100%",
            height="100%",
        ),
        rx.flex(
            rx.text(
                description,
                style=styles.font_default_style,

            ),
            padding="0 2em",
            margin="0 auto",
            text_align="justify",
            align="center",
            # bg="pink",
            width="100%",
            height="100%",
        ),
        rx.vstack(
            rx.flex(
                rx.text(
                    gaming_style_1,
                    style=styles.font_default_style,
                    color=TextColor.ACCENT

                ),
                align="center",
                justify="center",
                # bg="yellow",
                width="100%",
                height="100%",
            ),
            rx.flex(
                rx.text(
                    gaming_style_2,
                    style=styles.font_default_style,
                    color=TextColor.ACCENT

                ),
                align="center",
                justify="center",
                #                             bg="blue",
                width="100%",
                height="100%",
            ),
            rx.flex(
                rx.text(
                    gaming_style_3,
                    style=styles.font_default_style,
                    color=TextColor.ACCENT

                ),
                align="center",
                justify="center",
                #                             bg="maroon",
                width="100%",
                height="100%",
            ),
            spacing="1",
            height="100%",
            width="100%",
            #                         bg="olive"
        ),
        height="50%",
        width="50%",
        #                     bg="green"
    ),
    spacing="3",
    # height="100%",
    width="50%",
    # bg="violet",
)