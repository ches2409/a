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
                grid_column="1/14",
                grid_row="1/4",
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
                grid_column="1/2",
                grid_row="4/-1",
                # bg="purple",
                z_index="100",
            ),
            rx.box(
                rx.grid(
                    rx.hstack(
                        rx.spacer(),
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
                            # bg="yellow"
                        ),
                        rx.vstack(
                            button_action("play",
                                          "png"
                            ),
                            justify="center",
                            height="100%",
                            # bg="orange"
                        ),

                        grid_column="9/12",
                        grid_row="2/5",
                        # bg="pink",
                        z_index="100",
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
                            font_size=styles.Size.XBIG.value,
                            # bg="blue"
                        ),
                        rx.text(
                            "Domina sin piedad",
                            style=styles.font_body_style,
                            # bg="blue"
                        ),
                        justify="center",
                        grid_column="4/9",
                        grid_row="5/12",
                        # bg="violet",
                        z_index="100",
                    ),
                    columns="12",
                    rows="12",
                    # bg="grey",
                    width="100%",
                    height="100%",

                ),
                background_image="url(bg_container.png)",
                background_repeat="no-repeat",
                background_size="80% 100%",
                background_position="right",
                grid_column="2/-1",
                grid_row="2/14",
                # bg="cadetblue",
                z_index="99",
            ),
            rx.hstack(
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
                    z_index="100",
                ),
                rx.spacer(),
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
                    z_index="99",
                ),
                grid_column="14/16",
                grid_row="8/14",
                # bg="darkgreen",
                z_index="100",


            ),
            rx.flex(
                grid_column="2/-1",
                grid_row="14/-1",
                # bg="orchid",
                z_index="100",
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