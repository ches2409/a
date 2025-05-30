import reflex as rx

# def subscribe()->rx.Component:
#     return rx.box(
#         rx.flex(
#             rx.text(
#                 "Desata tu esencia"
#             )
#         ),
#         height="50vh",
#         width="100%",
#         # bg="orange"
#     )
def subscribe() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.flex(
                    rx.image(
                        src="logo.png",
                        width="10em",
                        height="auto",
                        # border_radius="25%",
                    ),
                    rx.heading(
                        "Crea tu cuenta",
                        size="6",
                        as_="h2",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.text(
                            "Estas registrado?",
                            size="3",
                            text_align="left",
                        ),
                        rx.link("Ingresa", href="#", size="3"),
                        spacing="2",
                        opacity="0.8",
                        width="100%",
                    ),
                    justify="start",
                    direction="column",
                    spacing="4",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="user@reflex.dev",
                        type="email",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.box(
                    rx.checkbox(
                        "Acepto terminos y condiciones",
                        default_checked=True,
                        spacing="2",
                    ),
                    width="100%",
                ),
                rx.button("Registrarse", size="3", width="100%"),
                rx.hstack(
                    rx.divider(margin="0"),
                    rx.text(
                        "O continuar con",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    rx.divider(margin="0"),
                    align="center",
                    width="100%",
                ),
                rx.center(
                    rx.icon_button(
                        rx.icon(tag="github"),
                        variant="ghost",
                        size="3",
                    ),
                    rx.icon_button(
                        rx.icon(tag="facebook"),
                        variant="ghost",
                        size="3",
                    ),
                    rx.icon_button(
                        rx.icon(tag="twitter"),
                        variant="ghost",
                        size="3",
                    ),
                    spacing="4",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            size="4",
            max_width="28em",
            width="100%",
        )
    )
