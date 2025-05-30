import reflex as rx

from arkadex.components.card_team import card_team
from arkadex.styles import styles


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
                # margin_bottom="-1vh",
                position="relative",
                grid_column="1/4",
                grid_row="1/-1",
                z_index="100",
                # bg="orange",
            ),
            rx.container(
                rx.center(
                    rx.vstack(
                        rx.flex(
                            rx.text(
                                "Facciones del Kaos",
                                style=styles.font_subtitle_style,
                                # width="100%",
                                # height="10em",
                                # bgcolor="purple",
                            ),
                            # align="center",
                            justify="center",
                            width="100%",
                            height="30%",
                            # bg="purple",
                        ),
                        rx.vstack(
                            rx.spacer(),
                            rx.text(
                                "En Arkadex no solo formamos equipos.",
                                style=styles.font_default_style,
                                font_size="1.2em",
                            ),
                            rx.text(
                                "Formamos facciones diseñadas para la guerra digital.",
                                style=styles.font_default_style,
                                font_size="1.2em",
                            ),
                            rx.text(
                                "Cada escuadra tiene su estilo, su especialidad y su fuego.Juntos, representamos una fuerza imparable en cada torneo, juego o partida clasificatoria.",
                                style=styles.font_default_style,
                                font_size="1.2em",
                                align="center",
                            ),
                            rx.text(
                                "¿Qué núcleo define tu estilo? ¿Dónde vibra tu energía?",
                                style=styles.font_default_style,
                                font_size="1.2em",
                            ),
                            spacing="1",
                            justify="center",
                            align="center",
                            align_self="center",
                            width="60%",
                            height="50%",
                            # bg="forestgreen",
                        ),

                        width="100%",
                        height="100%",
                        # bg="chartreuse",
                        background_image="url(bg_container_teams.png)",
                        background_repeat="no-repeat",
                        background_size="100% 100%",
                        background_position="center",
                        # background_origin="center",
                    ),
                    width="100%",
                    height="40vh",
                    # bg="orange",
                ),
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
                # margin_bottom="-5vh",
                position="relative",
                grid_column="6/-1",
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
            card_team(
                "noxkore",
                "Estrategas invisibles, verdugos del silencio",
                "NOXCORE es sigilo, trampa y precisión encubierta.Se mueven como sombras; piensan como maestros. Ganan desde la oscuridad, nunca desde el ruido. Si los ves... ya es tarde.",
                "Juego mental, rotaciones letales, engaño táctico.",
                "Dominan MOBAs, Siege y arenas con visión estratégica.",
                "Juegan con tu mente, no con tus mecánicas."
            ),
            card_team(
                "kryptax",
                "Saboteadores del meta. Arquitectos del caos",
                "Krypta no sigue el meta. Lo hackea, lo explota.Su estilo es caos adaptativo, genialidad espontánea. Nunca verás dos partidas iguales. Improvisan victoria desde el error.",
                "Estrategias rotas, picks absurdos, juego fluido.",
                "Ideales para modos alternos y torneos flex.",
                "Cuando pierden, crean. Cuando ganan, rompen.",
            ),
            card_team(
                "synthex",
                "Precisión artificial. Frialdad absoluta",
                "Synthex es control puro, mente fría y cálculo letal. Cada paso es un algoritmo, cada ataque una fórmula. Ganan con estrategia, dominan con disciplina total. No sienten presión. La ejecutan.",
                "Macrojuego, control de mapa, ejecución táctica.",
                "Reinan en MOBAs, RTS y shooters estratégicos.",
                "No improvisan. Solo optimizan.",
            ),
            card_team(
                "ravex",
                "Furia cinética, sin tregua ni reversa",
                "Krypta no sigue el meta. Lo hackea, lo explota.Su estilo es caos adaptativo, genialidad espontánea. Nunca verás dos partidas iguales. Improvisan victoria desde el error.",
                "Agresión explosiva, entrada frontal, ritmo constante.",
                "Dominan shooters, battle royale y juegos frenéticos.",
                "Cazan rápido. Caen tarde. Huyen nunca.",
            ),
            flex_wrap="wrap",
            justify_content="space-around",
            height="50%",
            width="100%",
            # bg="cyan",

        ),

        background_image="url(bg_teams.png)",
        background_repeat="no-repeat",
        background_size="40% 70%",
        background_position="top",
        # background_origin="center",
        spacing="1",
        # bg="lightgreen",
        height="200vh",
        width="100%",
    )