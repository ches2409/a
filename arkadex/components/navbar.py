import reflex as rx

def navbar()->rx.Component:
    return rx.vstack(
        rx.text(
            "Where legends rise"
        ),
        rx.hstack(
            rx.hstack(
                "Registrate",
            ),
            rx.hstack(
                "Informate",
            ),
        ),
        bg="blue",
        width="100%",
        height="100%",
    )

