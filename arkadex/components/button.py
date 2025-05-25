import reflex as rx
from pygments.styles.dracula import background

from arkadex.styles import styles


def button_rounded(icon:str, extension:str)->rx.Component:
    return rx.button(
        rx.image(
            src=f"{icon}.{extension}",
        ),
        height=styles.Size.BIG.value,
        width=styles.Size.BIG.value,

        border_radius="1em",
        box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
        background_image="linear-gradient(60deg,#AF40FF,#5B42F3 20%,#00DDEB)",
        # box_sizing="border-box",
        # color="white",
        opacity=1,
    )