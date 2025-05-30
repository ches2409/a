import reflex as rx

def footer()->rx.Component:
    return rx.flex(
        rx.image(
            src="logo_horizontal.png"
        ),
        # height="100%",
        # width="100vw",
        align="center",
        justify="center",
        # bg="orange"

    )

