import time

# Жадібний алгоритм
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

# Алгоритм динамічного програмування
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Функція для порівняння ефективності алгоритмів
def compare_algorithms(amount):
    print(f"Сума: {amount}")

    # Жадібний алгоритм
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time
    print("Жадібний алгоритм:", greedy_result, f"(Час: {greedy_time:.8f} секунд)")

    # Алгоритм динамічного програмування
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time
    print("Динамічне програмування:", dp_result, f"(Час: {dp_time:.8f} секунд)")

    print()

# Приклад використання
amounts_to_test = [11113, 2724153, 42197, 9942149]
for amount in amounts_to_test:
    compare_algorithms(amount)
