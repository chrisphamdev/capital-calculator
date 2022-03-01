# This function takes the user's input
def taking_input():
    starting_balance = int(input('Enter your current savings: '))
    annual_contribution = int(input('Enter your anual contribution: '))
    annual_return_rate = int(input('Enter your expected annual return rate in %: '))
    duration = int(input('Enter the number of years of your savings duration: '))

    return starting_balance, annual_contribution, annual_return_rate, duration

# This function calculates the net worth based on the given information
def calculations(starting_bal, contribution, rate, duration):
    capital = starting_bal
    for i in range(duration):
        capital += contribution
        capital = capital * ((100 + rate)/100)

    return capital

# Putting it all together
def capital_calculator():
    starting_balance, annual_contribution, annual_return_rate, duration = taking_input()
    capital = calculations(starting_balance, annual_contribution, annual_return_rate, duration)
    print('Your net worth after {} years is: ${:.1f}'.format(duration, capital))

capital_calculator()