import reflex as rx

from arkadex.styles import styles


def button_square(icon:str)->rx.Component:
    return rx.button(
        rx.image(
            src=f"{icon}.svg",
            height=styles.Size.DOUBLE,
        ),
        height=styles.Size.BIG.value,
        width="8em",

        border_radius="1em",
        box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
        background_image="linear-gradient(60deg,#AF40FF,#5B42F3 20%,#00DDEB)",
        opacity=1,
    )