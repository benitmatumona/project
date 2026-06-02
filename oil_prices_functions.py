import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


gas = pd.read_csv("data/gas_prices.csv")
    

def gas_price(*countries: str)-> plt:
    """creates a plot according to any contry/countries specified"""
    for country in countries:
        try:
            plt.plot(gas.Year, gas[country], label=country)
        except:
            print(f"invalid country name or format {country}")
        
    plt.xlabel("Year")
    plt.ylabel("Price(USD)")
    plt.xticks(gas.Year[::3])
    set_title("Gas Price Over Time", plt)
    return plt
    

def save_plt(plt: plt, location: str)-> bool:
    """
    saves the file at a desired location according to the second argument
    """
    try:
        plt.savefig(location, dpi=300)
    except Exception as e:
        print(f"Error: {e}")
        return False


def set_title(title:str, plt: plt)-> None:
    plt.title(title, 
        fontdict={"fontsize": "20", "fontweight": "bold", }
        )