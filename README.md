# VTU Telegram Bot

Welcome to the VTU Telegram Bot repository! This project aims to provide a seamless and efficient way to purchase Virtual Top Up (VTU) services through a Telegram bot, utilizing TRX (Tron) for payments.

## Features

- **Easy VTU purchases**: Users can buy airtime, data bundles, and other VTU services directly through Telegram.
- **Secure TRX payments**: Transactions are handled securely using the Tron blockchain.
- **User-friendly interface**: Interact with the bot through simple Telegram commands.
- **Automated transactions**: Payments and VTU top-ups are processed automatically.

## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you set up the VTU Telegram Bot on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- A Tron wallet with TRX for transactions
- A Telegram account
- BotFather on Telegram to create your bot and get the API token

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/debugtitan/vtu.git
    cd vtu
    ```

2. **Create a virtual environment and activate it**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Set up environment variables**

    Create a `.env` file in the project root directory and add the following:

    ```plaintext
    TELEGRAM_API_TOKEN=your_telegram_api_token
    wallet_phrase=your_wallet_phrase
    ```

2. **Run the bot**

    ```bash
    python 
    ```

3. **Interact with your bot on Telegram**

    Search for your bot in the Telegram app using the username you created with BotFather and start interacting with it.

## Commands

- `/start` - Welcome message and initial setup.
- `/buy_airtime` - Guide to purchasing airtime.
- `/buy_data` - Guide to purchasing data bundles.
- `/balance` - Check your TRX wallet balance.
- `/help` - List of available commands.

## Configuration

Modify the `config.py` file to customize the bot's behavior, such as transaction limits, supported VTU services, and more.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need further assistance, feel free to open an issue or contact the repository owner.

Happy coding!
