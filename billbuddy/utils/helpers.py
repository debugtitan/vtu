from telegram import KeyboardButton


def create_keyboard_button(
    buttons, buttons_per_column=1, button_header=None, button_footer=None
):

    main_buttons = (
        buttons
        if not button_header
        else [
            button
            for button in buttons
            if button not in button_header and button not in button_footer
        ]
    )

    menu = [
        main_buttons[i : i + buttons_per_column]
        for i in range(0, len(main_buttons), buttons_per_column)
    ]

    if button_header:
        menu.insert(0, [KeyboardButton(button_header)])
    if button_footer:
        menu.append([KeyboardButton(_button) for _button in button_footer])
    return menu
