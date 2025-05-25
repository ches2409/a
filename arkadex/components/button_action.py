import reflex as rx

from arkadex.styles import styles


def button_action(icon:str, extension:str)->rx.Component:
    return rx.button(
        rx.image(
            src=f"{icon}.{extension}",
            height=styles.Size.BIG.value,

        ),
        # align_items="center",
        # justify_content="center",
        height="9em",
        width="9em",

        border_radius="50%",
        bg=styles.Color.PRIMARY.value,
    )