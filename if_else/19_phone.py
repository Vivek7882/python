def cheaper_option():
    # Input prices and fees
    price_usa = float(input("Enter iPhone 17 Pro Max price in the USA (USD): "))
    tax_rate_usa = float(input("Enter sales tax % in the USA (like 8.25 for 8.25%): "))
    currency_rate = float(input("Enter conversion rate (1 USD to INR): "))
    price_india = float(input("Enter iPhone 17 Pro Max price in India (INR): "))
    import_duty_percent = float(input("Enter import duty % if bringing to India: "))

    # Calculate total cost in USA in USD
    tax_amount_usa = (price_usa * tax_rate_usa) / 100
    total_usa_usd = price_usa + tax_amount_usa

    # Convert USA cost to INR
    total_usa_inr = total_usa_usd * currency_rate

    # Apply import duty (if applicable)
    duty_amount = (total_usa_inr * import_duty_percent) / 100
    total_usa_inr_with_duty = total_usa_inr + duty_amount

    # Print results
    print("\n--- Cost Summary ---")
    print(f"Total cost if bought in USA (converted to INR): ₹{total_usa_inr:.2f}")
    print(f"Total cost after import duty: ₹{total_usa_inr_with_duty:.2f}")
    print(f"Cost in India: ₹{price_india:.2f}")

    # Decision
    if total_usa_inr_with_duty < price_india:
        print("\n📌 It’s cheaper to buy the iPhone in the USA!")
    elif price_india < total_usa_inr_with_duty:
        print("\n📌 It’s cheaper to buy the iPhone in India!")
    else:
        print("\n📌 Costs are almost the same!")


if __name__ == "__main__":
    cheaper_option()
