import reflex as rx

def subscribe()->rx.Component:
    return rx.box(
        rx.flex(
            rx.text(
                "Desata tu esencia"
            )
        ),
        height="50vh",
        width="100%",
        # bg="orange"
    )
