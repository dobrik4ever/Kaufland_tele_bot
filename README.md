# Kaufland_tele_bot
 Want some sales tracking at your local Kaufland?

This is an unofficial Telegram bot, whose main purpose is
to help poor students buy products efficiently

Its main tasks are:

    1.  Monitor the https://www.kaufland.de/angebote/aktuelle-woche.html once a week:
        a.  Parse the Categories, prices, discounts etc.
        b.  Every product must be documented inside the pandas.DataFrame and .xlsx
            product should contain the product name, category, price, discount, url to image
        
    2.  Texting with the users via Telegram. It should:
        a.  Send the newsletter every week
        b.  Handle the requests from users
        c.  Make short list out of each category with name, price and discount
        d.  Make long list out of each category with name, price, photo and discount
        e.  Have the buit-in keyboard with categories and options
    
You need to know that the Parser will handle the 1st task as a separate program
and it will be called only from "server.py". The Telegram bot should be a separate program too.
It should be written as a class and used from "server.py".

The main hint is to parallelize with threads the Monitoring and Texting parts. Don't forget
to use the .lock .acquire methods to prevent the usage of the same files simultaneously.
