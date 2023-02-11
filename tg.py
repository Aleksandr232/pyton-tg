from social_spam import Telegram

tg = Telegram()
tg.connect_user(api_id=27301040, api_hash="24233e21b31e177f1fb52d7f5498a185", phone_number="89063207897")
# api_id and api_hash can be obtained from this link by creating an application:
# https://my.telegram.org/auth



# Start spamming by user list
users_list = [1162189615]
tg.start_selective_spam(users_list, message='Я Андрей воробей')
# Or so
tg.start_selective_spam(users_list)
# if the text you have already set



