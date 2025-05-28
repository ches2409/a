import reflex as rx

from arkadex.components.button import button_rounded
from arkadex.styles import styles
from arkadex.styles.styles import MAX_WIDTH


def about()->rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.flex(
                rx.text(
                    "Somos Kódigo, Kaos y Kontrol",
                    style=styles.font_heading_style,
                    margin_right="1em",
                ),

                justify="end",
                width="100%",
                height="15%",
                # bg="pink",
            ),
            rx.grid(
                rx.vstack(
                    rx.vstack(

                        rx.text(
                            "No somos casuales. No vinimos aprobar",
                        ),
                        rx.text(
                            "Vinimos a escribir nuestro nombre en los codigos del juego.",
                        ),
                        rx.text(
                            "somos ",
                            rx.text(
                                "kÓDIGO",
                                as_="span",
                                style=styles.font_accent_style
                            ),
                            ": pensamos como estrategas, leemos el meta y creamos el nuestro.",
                            as_="span",

                        ),
                        rx.text(
                            "somos ",
                            rx.text(
                                "KAOS",
                                as_="span",
                                style=styles.font_accent_style
                            ),
                            ": impredecibles, agresivos, imposibles de replicar.",
                            as_="span",

                        ),
                        rx.text(
                            "somos ",
                            rx.text(
                                "KONTROL",
                                as_="span",
                                style=styles.font_accent_style
                            ),
                            ": ejecutamos con precisión milimétrica y mentalidad de campeón.",
                            as_="span",

                        ),
                        width="100%",
                        # padding_top="1em",
                        # padding_left="em",
                        # bg="purple",

                    ),

                    rx.text(
                        "Somos ArkadeX",
                        style=styles.font_subtitle_style,
                        align_self="end",
                        margin_right="2rem",

                        # bg="green",
                    ),


                    rx.vstack(

                        rx.text(
                            "No importa como entres."
                        ),
                        rx.text(
                            "Importa como juegas."
                        ),
                        rx.text(
                            "Y en Arkadex se juega para Dominar."
                        ),
                        width="50%",
                        align="center",
                        # bg="blue"

                    ),

                    background_image="url(bg_about.png)",
                    background_repeat="no-repeat",
                    background_size="100% 100%",
                    # background_position="left",
                    background_origin= "content - box",

                    spacing="1",

                    grid_column="1/6",
                    grid_row="1/6",

                    padding_left="4em",
                    justify="center",
                    width="100%",
                    height="100%",
                    # bg="violet",
                    z_index="100",
                ),
                rx.hstack(
                    rx.box(
                        button_rounded(
                            "user-bounty-hunter",
                            "svg"
                        ),
                        # wiodth=styles.Size.BIG.value,
                        align_content="center",
                        # bg="green",
                        width="4rem",
                        height="100%",
                    ),
                    rx.flex(
                        rx.text(
                            "Despierta tu leyenda",
                            style=styles.font_horizontal_button_style,
                        ),
                        justify_content="center",
                        direction="column",
                        height="100%",
                    ),

                    grid_column="4/-1",
                    grid_row="5/-1",
                    width="100%",
                    height="100%",
                    # bg="chartreuse",
                    z_index="101",
                ),
                columns="6",
                rows="6",
                width="100%",
                height="85%",
                # bg="purple",
            ),
            spacing="1",
            width="60%",
            height="100%",
            # bg="orange",
        ),
        rx.flex(
            rx.text(
                "Kódigo cargado. Kaos aceptado. Kontrol ejecutado",
                style=styles.font_vertical_style,
            ),
            rx.box(
                rx.image(
                    src="jinx.png",
                    position="absolute",
                    lef="0",
                    bottom="0",

                    height="100vh",
                ),
                position="relative",
                width="100%",
                height="100%",
                # bg="orange",
            ),

            width="40%",
            height="100%",
            # bg="maroon",
        ),
        spacing="1",
        width="100%",
        height="60vh",
        # bg="blue",
    )