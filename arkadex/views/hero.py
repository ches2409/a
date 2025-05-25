import reflex as rx

from arkadex.styles.styles import MAX_HEIGHT


def hero()->rx.Component:
    return rx.hstack(
        rx.container(
            bg="red",
            width="15vw",
            height="100%",
        ),
        rx.grid(
            rx.box(
                grid_column="1/14",
                grid_row="1/4",
                bg="orange",
                z_index="100",
            ),
            rx.flex(
                grid_column="1/2",
                grid_row="4/-1",
                bg="purple",
                z_index="100",
            ),
            rx.container(
                grid_column="2/-1",
                grid_row="2/14",
                bg="cadetblue",
                z_index="99",
            ),
            rx.hstack(
                grid_column="12/-1",
                grid_row="6/14",
                bg="darkgreen",
                z_index="100",
            ),
            rx.flex(
                grid_column="2/-1",
                grid_row="14/-1",
                bg="orchid",
                z_index="100",
            ),
            columns="16",
            rows="16",
            bg="grey",
            width="80vw",
            height="100%",
        ),
        rx.container(
            bg="green",
            width="5vw",
            height="100%",
        ),

        bg="violet",
        spacing="1",
        width="100%",
        height=MAX_HEIGHT
    )