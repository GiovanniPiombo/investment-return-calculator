import os
from colorama import init, Fore, Back, Style
from pyfiglet import Figlet
import matplotlib.pyplot as plt

init(autoreset=True)

def calculate_result(investment): 
    investment["Final Capital"] = investment["Initial Capital"] * (1 + investment["Annual Return"]/1200)**(12*investment["Duration (years)"]) + investment["Monthly Contribution"] * (((1 + investment["Annual Return"]/1200)**(12*investment["Duration (years)"]) - 1) / (investment["Annual Return"]/1200))
    investment["Total Invested"] = (investment["Monthly Contribution"] * 12 * investment["Duration (years)"]) + investment["Initial Capital"]
    investment["Profit"] = investment["Final Capital"] - investment["Total Invested"]
    return investment

def show_chart(investment):
    years = int(investment["Duration (years)"])
    monthly_return = investment["Annual Return"] / 1200
    capital = investment["Initial Capital"]
    monthly_contribution = investment["Monthly Contribution"]

    year_list = []
    capital_list = []
    invested_list = []

    total = capital
    for year in range(1, years + 1):
        months = year * 12
        total = capital * (1 + monthly_return) ** months + monthly_contribution * (((1 + monthly_return) ** months - 1) / monthly_return)
        year_list.append(year)
        capital_list.append(total)

    for year in year_list:
        invested_list.append(investment["Initial Capital"] + investment["Monthly Contribution"] * 12 * year)
        
    plt.plot(year_list, invested_list, 'r--', label="Total Invested")
    plt.plot(year_list, capital_list, marker='o', label="Capital")
    plt.legend()
    plt.title("Capital Growth Over Time")
    plt.xlabel("Year")
    plt.ylabel("Value (€)")
    plt.grid(True)
    plt.show()

def getValue(request):
    while(True):
        try:
            value = float(input(Fore.BLUE + Style.BRIGHT + request))
            if(value < 0):
                print("Negative values are not allowed ")
            else:
                return value
        except ValueError:
            print("Invalid Value! ")
        except Exception:
            print("An error occured, try again")

def main():
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        banner = Figlet(font='slant', justify='center')
        print(Fore.RED + banner.renderText('Investment Return'))
        investment = {}
        investment["Initial Capital"] = getValue("Initial Deposit : ")
        investment["Annual Return"] = getValue("Annual Return (%): ")
        investment["Monthly Contribution"] = getValue("Monthly Contribution: ")
        investment["Duration (years)"] = getValue("Investment Duration (years): ")
        investment = calculate_result(investment)
        print(Fore.BLUE + Style.BRIGHT + "Final Capital = " + str(investment["Final Capital"]))
        print(Fore.BLUE + Style.BRIGHT + "Total Invested = " + str(investment["Total Invested"]))
        print(Fore.BLUE + Style.BRIGHT + "Profit = " + str(investment["Profit"]))
        show_chart(investment)
        x = input(Fore.RED + Style.BRIGHT + "Do you want to run the program again? (y/n)")
        if x.lower() == "y":
            continue
        break

main()