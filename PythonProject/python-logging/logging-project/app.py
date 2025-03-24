# # import logging

# # # Configure logging settings

# # logging.basicConfig(
# #     level=logging.DEBUG,
# #     format='%(asctime)s - %(name)% - %(levelname)% - %(message)s',
# #     datefmt='%Y-%m-%d %H:%M:%S',
# #     handlers=[
# #         logging.FileHandler('app1.log'),
# #         logging.StreamHandler()
# #     ]
# # )

# # logger = logging.getLogger("ArithmeticApp")


# # def add(a, b):
# #     result = a+b
# #     # logger.debug(f"Adding {a} + { b}", result)
# #     # logger.debug(f"Adding {a} + {b} = {result}")
# #     return result


# # sum = add(3, 4)
# # print(sum)


# # # def add(a, b):
# # #     result = a + b
# # #     logger.debug(f"Adding : ", result)
# # #     return result
# # #

# # # def sub(a, b):
# # #     result = a - b
# # #     logger.debug(f"Subtraction {a} - { b} = { result}")
# # #     return result


# # # def multiply(a, b):
# # #     result = a * b
# # #     logger.debug(f"Multiplying {a} * { b} = { result}")
# # #     return result


# # # def divide(a, b):
# # #     try:

# # #         result = a / b
# # #         logger.debug(f"Division {a} + { b} = { result}")
# # #         return result
# # #     except ZeroDivisionError:
# # #         logger.error("Division by zero error")
# # #         result None


# # # add(10, 15)
# # # sub(15, 10)
# # # multiply(4, 5)
# # # divide(5, 6)


# import logging

# # Configure logging settings
# logging.basicConfig(
#     level=logging.DEBUG,
#     # Fixed format here
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[
#         logging.FileHandler('app1.log'),
#         logging.StreamHandler()
#     ]
# )

# logger = logging.getLogger("ArithmeticApp")


# def add(a, b):
#     result = a + b
#     logger.debug(f"Adding {a} + {b} = {result}")  # Log the addition result
#     return result


# def sub(a, b):
#     result = a - b
#     # Log the subtraction result
#     logger.debug(f"Subtracting {a} - {b} = {result}")
#     return result


# def multiply(a, b):
#     result = a * b
#     # Log the multiplication result
#     logger.debug(f"Multiplying {a} * {b} = {result}")
#     return result


# def divide(a, b):
#     try:
#         result = a / b
#         # Log the division result
#         logger.debug(f"Dividing {a} / {b} = {result}")
#         return result
#     except ZeroDivisionError:
#         logger.error("Division by zero error")
#         return None  # Return None in case of a division by zero


# # Example usage
# sum_result = add(3, 4)
# print(sum_result)

# difference = sub(15, 10)
# print(difference)

# product = multiply(4, 5)
# print(product)

# quotient = divide(5, 0)
# print(quotient)
