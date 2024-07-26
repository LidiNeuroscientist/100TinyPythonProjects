from Utilities import Currency
from Utilities import Data


# PRINCIPAL PROGRAM
price = Data.readMoney('Type a PRICE: EUR ')
Currency.Summary(price, 20, 20)



# If you enter a letter with a number : EUR400.55 also will give a ERROR,
# We will solve it in next exercises; TREATING ERRORS

