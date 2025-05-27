import reflex as rx

from arkadex.components.button import button_rounded
from arkadex.components.button_action import button_action
from arkadex.components.navbar import navbar
from arkadex.styles import styles
from arkadex.styles.styles import MAX_HEIGHT


def hero()->rx.Component:
    return rx.hstack(
        rx.container(
            rx.image(
                src="logoVertical.png",
                width="20vh",
                margin_top="5vh",
            ),
            # bg="red",
            width="15vw",
            height="100%",
        ),
        rx.grid(
            rx.box(
                navbar(),
                margin_top="-1.5em",
                grid_column="1/14",
                grid_row="2/4",
                # bg="red",
                z_index="100",
            ),
            rx.flex(
                rx.text(
                    "Donde los valientes no juegan... compiten y destrozan",
                    style=styles.font_vertical_style,
                ),
                align="end",
                justify="end",
                grid_column="1/2",
                grid_row="4/-1",
                # bg="blue",
                z_index="100",
            ),
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Únete",
                            style=styles.font_horizontal_button_style,
                            font_size="2.5em",
                        ),
                        rx.text(
                            "a la arena",
                            style=styles.font_horizontal_button_style,
                        ),
                        spacing="0",
                        align_items="end",
                        justify="center",
                        height="100%",
                        width="85%",
                        # bg="yellow"

                    ),
                    rx.vstack(
                        button_action(
                            "play",
                            "png"
                        ),
                        justify="center",
                        height="100%",
                        width="15%",
                        # bg="orange"

                    ),
                    padding_top="1.5em",
                    height="25%",
                    width="100%",
                    # bg="darkgreen",
                ),
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Entra",
                            style=styles.font_body_style,
                            # bg="blue"
                        ),
                        rx.text(
                            "DESATA TU ESENCIA",
                            style=styles.font_body_style,
                            font_size=styles.Size.XBIG.value,
                            # bg="blue"
                        ),
                        rx.text(
                            "Domina sin piedad",
                            style=styles.font_body_style,
                            # bg="blue"
                        ),
                        padding_left="5%",
                        justify="center",
                        z_index="100",

                        height="100%",
                        width="70%",
                        # bg="pink",
                    ),
                    rx.hstack(
                        rx.spacer(),
                        rx.box(
                            rx.vstack(
                                button_rounded(
                                    "gamepad-modern",
                                    "svg"
                                ),
                                rx.text(
                                    "Ver equipos",
                                    style=styles.font_vertical_button_style,
                                ),
                                align="center"
                            ),
                            # bg="darkgreen",
                        ),
                        # rx.spacer(),
                        rx.box(
                            rx.vstack(
                                button_rounded(
                                    "alien-8bit",
                                    "svg"
                                ),
                                rx.text(
                                    "Ver partidas",
                                    style=styles.font_vertical_button_style,
                                ),
                                align="center"
                            ),
                            # bg="green",
                        ),
                        rx.spacer(),
                        spacing="6",
                        align="center",


                        height="100%",
                        width="30%",
                        # bg="blue",
                    ),
                    spacing="1",
                    height="75%",
                    width="100%",
                    # bg="darkorange",
                ),

                background_image="url(bg_container.png)",
                background_repeat="no-repeat",
                background_size="100% 100%",
                background_position="right",

                spacing="1",
                grid_column="4/-1",
                grid_row="2/13",
                # bg="green",
                z_index="99",
            ),
            columns="16",
            rows="16",
            # bg="grey",
            width="80vw",
            height="100%",
        ),
        rx.container(
            # bg="green",
            width="5vw",
            height="100%",
        ),

        # bg="violet",
        spacing="1",
        width="100%",
        height=MAX_HEIGHT
    )