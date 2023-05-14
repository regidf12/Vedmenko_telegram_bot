# Welcome to Regidf

# Vkontakte_bot :robot:

The bot facilitates the work of Vedmenko production employees.

## Installation :gear:

If you are cloning a project, run it first, otherwise you can download the source on the release page and skip this step.

    git clone https://github.com/White-prince/Vedmenko_telegram_bot.git
    
You will need to install the libraries before starting the assistant

    pip install vk_api
    
You will also need a token to run your bot

## Usege :information_source:

The token can be received in telegram from the bot: [@Botfather](https://t.me/BotFather). You can also get a token for payment according to his instructions..

    TOKEN = ''
    

    PMTOKEN = ''

Write the command in the terminal:

    python main.py

## About the code :electron:

- The file message.py contains login information

Running code :
    
    if __name__ == '__main__':
        executor.start_polling(dp, loop=loop)
 
All other features are pretty standard.

Hope this code helps you
