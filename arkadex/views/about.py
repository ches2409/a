import reflex as rx

from arkadex.components.button import button_rounded
from arkadex.styles import styles
from arkadex.styles.styles import MAX_WIDTH


def about()->rx.Component:
    return rx.grid(
        rx.vstack(
            rx.vstack(

                rx.vstack(
                    rx.vstack(
                        rx.text(
                            "No somos casuales. No vinimos aprobar",
                        ),
                        rx.text(
                            "Vinimos a escribir nuestro nombre en los codigos del juego.",
                        ),
                        rx.text(
                            [
                                rx.text(
                                    "somos ",
                                    rx.text(
                                        "KÓDIGO",
                                        as_="span",
                                        style=styles.font_accent_style
                                    ),
                                    ": pensamos como estrategas, leemos el meta y creamos el nuestro.",
                                    as_="span",

                                )
                            ]
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
                        margin_left="4rem"
                    ),
                    rx.text(
                        "Somos ArkadeX",
                        style=styles.font_subtitle_style,
                        align_self="end",
                        # bg="violet"
                    ),
                    width="100%",
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
                    width="80%",
                    align="center",
                    # bg="violet"
                ),
                # bg="red",
                width="100%",

            ),
            grid_column="1/11",
            grid_row="2/9",
            # bg="green",
            z_index="99"
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
            grid_column="7/13",
            grid_row="7/9",
            # bg="purple",
            z_index="100",
        ),
        rx.flex(
            rx.text(
                "Kódigo cargado. Kaos aceptado. Kontrol ejecutado",
                style=styles.font_vertical_style,
            ),
            grid_column="13/19",
            grid_row="1/11",
            # bg="orange",
            z_index="100",
        ),

        columns="20",
        rows="10",
        # bg="grey",
        width="100%",
        height="60vh",
    )