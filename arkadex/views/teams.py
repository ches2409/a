import reflex as rx

from arkadex.styles import styles
from arkadex.styles.styles import MAX_HEIGHT


def teams()->rx.Component:
    return rx.vstack(
        rx.grid(

            rx.box(
                rx.image(
                    src="val.png",
                    position="absolute",
                    right="0",
                    bottom="0",

                    height="70vh",
                ),
                margin_bottom="-5vh",
                position="relative",
                grid_column="1/3",
                grid_row="1/-1",
                z_index="100",
                # bg="orange",
            ),
            rx.container(
                rx.vstack(
                    rx.text(
                        "En Arkadex no solo formamos equipos.",
                    ),
                    rx.text(
                        "Formamos facciones diseñadas para la guerra digital.",
                    ),
                    rx.text(
                        "Cada escuadra tiene su estilo, su especialidad y su fuego.Juntos, representamos una fuerza imparable en cada torneo, juego o partida clasificatoria.",
                    ),
                    rx.text(
                        "¿Qué núcleo define tu estilo? ¿Dónde vibra tu energía?",
                    ),
                ),

                background_image="url(bg_container_teams.png)",
                background_repeat="no-repeat",
                background_size="100% 100%",
                # background_position="left",
                background_origin="content - box",

                padding="3em",
                grid_column="2/8",
                grid_row="3/9",
                z_index="99",
                # bg="brown",
            ),
            rx.box(
                rx.image(
                    src="apex.png",
                    position="absolute",
                    left="0",
                    bottom="0",

                    height="70vh",
                ),
                margin_bottom="-5vh",
                position="relative",
                grid_column="7/-1",
                grid_row="1/-1",
                z_index="100",
                # bg="purple",
            ),
            columns="8",
            rows="8",
            height="50%",
            width="100%",
            # bg="olive",
        ),
        rx.flex(
            height="50%",
            width="100%",
            # bg="cyan",
        ),
        background_image="url(bg_teams.png)",
        background_repeat="no-repeat",
        background_size="40% 70%",
        background_position="center",
        # background_origin="center",
        spacing="1",
        # bg="lightgreen",
        height="150vh",
        width="100%",
    )