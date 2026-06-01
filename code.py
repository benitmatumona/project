import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


gas = pd.read_csv("data/gas_prices.csv")


def gas_price(*countries: str)-> plt:
    for country in countries:
        try:
            plt.plot(gas.Year, gas[country], label=country)
        except:
            print(f"invalid country name or format {country}")
        
        
    plt.title("Gas Price Over Time", fontdict={"fontsize": "20", "fontweight": "bold", })
    plt.xlabel("Year")
    plt.ylabel("Price(USD)")
    plt.xticks(gas.Year[::3])
    return plt
    

def save_plt(plt: plt, location: str)-> bool:
    try:
        plt.savefig(location, dpi=300)
    except Exception as e:
        print(f"Error: {e}")
        return False



graph = gas_price("USA", "South Korea", "Canada", "China")
graph.show()