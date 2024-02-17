import random

MAX_INCREASE = 0.10  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.00
INITIAL_PRICE = 10.00
OUTPUT_FILE = "stock_prices.txt"

price = INITIAL_PRICE
days = 0

# Open the output file for writing
out_file = open(OUTPUT_FILE, 'w')

# Print the initial price
print(f"Starting price: ${price:.2f}")
print(f"Starting price: ${price:.2f}", file=out_file)

# Simulate the stock price until it falls below MIN_PRICE or rises above MAX_PRICE
while MIN_PRICE <= price <= MAX_PRICE:
    days += 1
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    # Print/write the price for the day
    print(f"On day {days} price is: ${price:.2f}")
    print(f"On day {days} price is: ${price:.2f}", file=out_file)

# Close the output file
out_file.close()