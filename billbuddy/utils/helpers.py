from typing import Dict, List, Optional
from telegram import KeyboardButton, InlineKeyboardButton


def create_keyboard_button(
    buttons, buttons_per_column=1, button_header=None, button_footer=None
):
    # Check if button_footer is not None
    if button_footer is None:
        button_footer = []

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


def create_inline_button(
    buttons: Dict[str, str],
    buttons_per_column: int = 1,
    button_header: Optional[Dict[str, str]] = None,
    button_footer: Optional[Dict[str, str]] = None,
    callback_text: Optional[str] = None,
) -> List[List[InlineKeyboardButton]]:

    menu = [
        [
            InlineKeyboardButton(
                text, callback_data=callback_text + data if callback_text else data
            )
            for text, data in list(buttons.items())[i : i + buttons_per_column]
        ]
        for i in range(0, len(buttons), buttons_per_column)
    ]

    if button_header:
        header_button = list(button_header.items())[0]
        menu.insert(
            0,
            [
                InlineKeyboardButton(
                    header_button[0],
                    callback_data=(
                        callback_text + header_button[1]
                        if callback_text
                        else header_button[1]
                    ),
                )
            ],
        )

    if button_footer:
        footer_buttons = [
            InlineKeyboardButton(
                text, callback_data=callback_text + data if callback_text else data
            )
            for text, data in button_footer.items()
        ]
        menu.append(footer_buttons)

    return menu
