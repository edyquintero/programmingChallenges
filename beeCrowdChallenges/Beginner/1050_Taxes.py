total_money = float(input())


def calculate_tax(total_money):
    total_tax = 0

    if total_money > 2000:
        remaining = total_money - 2000

        if remaining > 1000:
            total_tax += 1000 * 0.08
            remaining -= 1000

            if remaining > 1500:
                total_tax += 1500 * 0.18
                remaining -= 1500

                if remaining > 0:
                    total_tax += remaining * 0.28
            else:
                total_tax += remaining * 0.18
        else:
            total_tax += remaining * 0.08

    return total_tax


tax = calculate_tax(total_money)

if tax == 0:
    print("Isento")
else:
    print(f"R$ {tax:.2f}")
