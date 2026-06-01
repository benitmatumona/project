import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


gas = pd.read_csv("data/gas_prices.csv")


def gas_price(*countries: str)-> bool:
    for country in countries:
        try:
            plt.plot(gas.Year, gas[country], label=country)
        except:
            print(f"invalid country name or format {country}")
        
        
    plt.title("Gas Price Over Time")
    plt.xlabel("Year")
    plt.ylabel("Price(USD)")
    plt.xticks(gas.Year[::3])
    plt.show()
    return True
    
    
gas_price("USA", "South Korea", "Canada", "China")