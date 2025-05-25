import reflex as rx

import arkadex.styles.styles as styles
from arkadex.components.button import button_round
from arkadex.components.button_square import button_square
from arkadex.styles.colors import Color

from arkadex.styles.fonts import Font
from arkadex.styles.styles import BASE_STYLE, Size, MAX_HEIGHT


def header()->rx.Component:
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
            rx.flex(
                rx.text(
                    "Where legends rise",
                    style=styles.font_title_style,
                ),
                align="end",
                grid_column="1/15",
                grid_row="2/5",
                # bg="orange",
                z_index="100",
            ),
            rx.flex(
                rx.text(
                    "Donde los valientes no juegan... compiten y destrozan",
                    style=styles.font_vertical_style,
                ),

                align="end",
                justify="end",

                grid_column="1/5",
                grid_row="5/-1",
                # bg="green",
                z_index="100",
            ),
            rx.grid(

                rx.box(
                    rx.vstack(
                        rx.text(
                            "Ver equipos",
                            style=styles.font_vertical_button_style,
                        ),
                        button_round(
                            "gamepad-modern",
                        ),
                        align="center"
                    ),
                    grid_column="1/3",
                    grid_row="5/8",
                    # bg="darkgreen",
                    z_index="100",
                ),
                rx.box(
                    rx.vstack(
                        button_round(
                            "alien-8bit"
                        ),
                        rx.text(
                            "Ver partidas",
                            style=styles.font_vertical_button_style,
                        ),
                        align="center"
                    ),
                    grid_column="2/4",
                    grid_row="6/9",
                    # bg="green",
                    z_index="99",
                ),
                rx.vstack(
                    rx.text(
                        "Entra",
                        style=styles.font_body_style,
                        # bg="blue"
                    ),
                    rx.text(
                        "DESATA TU ESENCIA",
                        style=styles.font_body_style,
                        font_size=Size.XBIG.value,
                        # bg="blue"
                    ),
                    rx.text(
                        "Domina sin piedad",
                        style=styles.font_body_style,
                        # bg="blue"
                    ),
                    justify="center",
                    grid_column="4/13",
                    grid_row="5/10",
                    # bg="green",
                ),
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "Regístrate",
                                style=styles.font_horizontal_button_style,
                                align="right",
                            ),
                            margin="0 0 0 -5em",
                            width="100%",
                            # bg="orange"
                        ),
                        button_square(
                            "user-plus",
                        ),


                    ),
                    style=styles.align_style_center,
                    grid_column="13/15",
                    grid_row="4/6",
                    # bg="darkgreen",
                ),
                rx.box(
                    rx.vstack(
                        button_square(
                            "chart-simple",
                        ),
                        rx.box(
                            rx.text(
                                "Infórmate",
                                style=styles.font_horizontal_button_style,
                                align="right",
                            ),

                            margin="0 0 0 -5em",
                            width="100%",
                            # bg="orange"
                        ),
                        # spacing="2",
                    ),
                    # width="4rem",
                    # height="100%",
                    grid_column="15/17",
                    grid_row="5/7",
                    # bg="green",
                ),

                # background_image="url(bag1.png)",
                # background_repeat="no-repeat",
                # background_size="100% 100%",
                # background_position="center",

                grid_column="5/-1",
                grid_row="2/15",
                # bg="pink",
                z_index="90",

                columns="16",
                rows="10",
            ),
            rx.flex(
                rx.text(
                    "Somos Kódigo, Kaos y Kontrol",
                    style=styles.font_subtitle_style,
                    font_size=Size.DOUBLE.value,

                ),
                align="end",
                grid_column="5/17",
                grid_row="15/-1",
                # bg="orange",
                z_index="100",
            ),

            columns="20",
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