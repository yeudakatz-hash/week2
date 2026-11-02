# def parse_percentage(text):
#     try:
#         if not text.endswith("%"):
#             raise ValueError("must end with %")
#         number = int(text[:-1])
#         if int(number) > 100:
#             raise ValueError("must be lass than 100")
#         if int(number) < 0:
#             raise ValueError("must be big than 0")
#         return number
#     except ValueError as error:
#         return error
#
# print(parse_percentage(text= "75%"))
# print(parse_percentage(text= "75"))
# print(parse_percentage(text= "-2%"))
# print(parse_percentage(text= "120%"))


# import logging
# print("jjjj")
# logging.error("hiii")





import logging
from http.cookiejar import debug

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="my_logs.log"
)

logging.warning(debug)


























