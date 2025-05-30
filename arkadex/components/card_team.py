import reflex as rx
from reflex import button

from arkadex.components.button import button_rounded
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
    return rx.vstack(
        rx.hstack(
            rx.flex(
                rx.image(
                    src=f"{image}.png",
                    # max_height="none",
                    height="100%",
                    width="100%",
                    object_fit="contain",
                    object_position="right top",

                ),
                # align_content="flex-start",
                # justify_content="flex-start",
                position="realative",
                height="35em",
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
                height="100%",
                width="60%",
                # bg="green"
            ),

        ),
    
        rx.flex(
            rx.text(
                "Dark plays. Sharp minds.",
                margin_right="2em",
            ),
            button_rounded(
                "swords",
                "svg"
            ),
            align="center",
            justify="end",
            height="4em",
            width="96%",
            # bg="violet",
        ),
        spacing="3",
        # height="100%",
        width="45%",
        # bg="violet",
    )