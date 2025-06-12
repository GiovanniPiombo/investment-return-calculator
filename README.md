
# Investment Return Calculator

A simple Python application that calculates the growth of an investment over time, including monthly contributions and compound interest. The program also visualizes the capital growth compared to the total invested amount using a chart.

## Features

- Calculate final capital based on initial deposit, annual return, monthly contributions, and investment duration.
- Show total invested amount and profit.
- Display a clear growth chart using Matplotlib.
- User-friendly terminal interface with colorful text (using Colorama) and ASCII art banners (using PyFiglet).
- Input validation to prevent invalid or negative values.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/GiovanniPiombo/investment-return-calculator.git
cd investment-return-calculator
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

*Note:* The dependencies are `colorama`, `pyfiglet`, and `matplotlib`.

## Usage

Run the program:

```bash
python investment_return_calculator.py
```

Follow the on-screen prompts to enter:

- Initial Deposit
- Annual Return (in %)
- Monthly Contribution
- Investment Duration (in years)

The program will then calculate and display:

- Final Capital
- Total Invested
- Profit

It will also show a chart illustrating the capital growth over time.

## Example

```
Initial Deposit : 10000
Annual Return (%): 5
Monthly Contribution: 200
Investment Duration (years): 10
```

Results will be :

!=[Example Chart](Example.png)
```
Final Capital : 47526.55086603624
Total Invested (%) : 34000.0
Profit : 13526.55086603624
```
## License

This project is licensed under the MIT License.
