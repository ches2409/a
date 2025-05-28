import reflex as rx

from arkadex.styles import styles


def button_action(icon:str, extension:str)->rx.Component:
    return rx.button(
        rx.image(
            src=f"{icon}.{extension}",
            height=styles.Size.BIG.value,
            margin_left=".6em",

        ),
        # align_items="center",
        # justify_content="center",

        height="7em",
        width="7em",

        border_radius="50%",
        bg=styles.Color.PRIMARY.value,
    )