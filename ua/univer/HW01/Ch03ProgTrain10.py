# Money Counting Game
numberOf5KopeckCoins = int(input("Enter the number of five-kopeck coins: "))
numberOf10KopeckCoins = int(input("Enter the number of ten-kopeck coins: "))
numberOf50KopeckCoins = int(input("Enter the number of fifty-kopeck coins: "))
coinDenomination5 = 5
coinDenomination10 = 10
coinDenomination50 = 50
coinDenomination5 /= 100
coinDenomination10 /= 100
coinDenomination50 /= 100
money5KopeckCoins = numberOf5KopeckCoins * coinDenomination5
money10KopeckCoins = numberOf10KopeckCoins * coinDenomination10
money50KopeckCoins = numberOf50KopeckCoins * coinDenomination50
total = money5KopeckCoins + money10KopeckCoins + money50KopeckCoins
if total == 1:
    print("Congratulations, you are the winner.")
else:
    if total < 1:
        print("You have less than 1 RUB")
    else:
        print("You have more than 1 RUB")
