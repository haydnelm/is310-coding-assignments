For my assignment I used the europeana API (instructions on how to use this API are in the assignment). My search queuery was simply "lasagna". 

For the API that I chose to use, I went with steam. Steam is a popular gaming platform, I'm sure many of you already knew that. I did something very simple and extracted my own steam profile data. I didn't do anything complicated. In order to use steam's API, you'll need to install it using the following commands:

    pip install python-steam-api

    pip install steam

It's pretty simple to use. You import using:

    from steam_web_api import Steam

After that, you can create your key with steamKey = Steam('STEAM_API_KEY'). Note: you'll need to create an API key on steam's website.

The command that I used to get my profile data is as follows:

    user_details = steam.users.get_user_details("STEAM_USER_ID")


In order to use any of the APIs you'll need to generate API keys and authenticate that appropriately. Use steamKey = Steam('STEAM_API_KEY') for steam.