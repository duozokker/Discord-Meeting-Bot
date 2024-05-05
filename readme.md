# Discord Meeting Bot

This project is a Discord bot designed to facilitate meetings. It allows users to express their opinions or status through color-coded commands. The bot maintains a list of users in each category and can display this information in an embed.

## Color Codes

- Green: Agree
- Red: Disagree
- Yellow: Neutral/Question
- Blue: Stop (Indicates that the discussion is going in circles)

## Commands

- `!green`: Add yourself to the green category (Agree)
- `!red`: Add yourself to the red category (Disagree)
- `!yellow`: Add yourself to the yellow category (Neutral/Question)
- `!blue`: Add yourself to the blue category (Stop)
- `!reset`: Reset all categories

## Setup

1. Clone this repository.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Set up a bot on the Discord developer portal, get the token, and add the bot to your server.
4. Set your bot's token as an environment variable. In your project directory, create a `.env` file and add the following line:

    ```env
    TOKEN=your-bot-token
    ```

    Replace `your-bot-token` with your actual bot token. The bot will access this token with the following lines in `main.py`:

    ```python
    import os
    token = os.getenv('TOKEN')
    bot.run(token)
    ```

5. Run `main.py` to start the bot.

## Hosting on Heroku

This project is ready to be deployed on Heroku. The `Procfile` and `runtime.txt` files are already set up for deployment. You just need to create a new Heroku app, connect your GitHub repository, and deploy.

When deploying to Heroku, you'll need to set the bot token as a config var. In your Heroku app dashboard, go to Settings, reveal Config Vars, and add a new config var with the key `TOKEN` and the value as your bot token.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)