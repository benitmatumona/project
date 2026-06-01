import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


gas = pd.read_csv("data/gas_prices.csv")
fifa = pd.read_csv("data/fifa_data.csv")


def gas_price(*countries: str)-> plt:
    """creates a plot according to any contry/countries specified"""
    for country in countries:
        try:
            plt.plot(gas.Year, gas[country], label=country)
        except:
            print(f"invalid country name or format {country}")
        
        
    plt.title(
        "Gas Price Over Time", 
        fontdict={"fontsize": "20", "fontweight": "bold", }
        )
    plt.xlabel("Year")
    plt.ylabel("Price(USD)")
    plt.xticks(gas.Year[::3])
    return plt
    

def save_plt(plt: plt, location: str)-> bool:
    """saves the file at a desired location according to the second argument"""
    try:
        plt.savefig(location, dpi=300)
    except Exception as e:
        print(f"Error: {e}")
        return False


def fifa_hist()-> bool:
    bins = [40, 50, 60, 70, 80, 90, 100]
    plt.hist(fifa.Overoll, bins= bins)
    plt.title("Distribution Of Players According To Their Skills")
    plt.xticks(bins)
    plt.xlabel("Skill Level")
    plt.ylabel("number of players")
    return True
