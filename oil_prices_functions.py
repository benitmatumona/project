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


def fifa_hist()-> bool:
    bins = [40, 50, 60, 70, 80, 90, 100]
    plt.hist(fifa.Overoll, bins= bins)
    plt.xticks(bins)
    plt.xlabel("Skill Level")
    plt.ylabel("number of players")
    set_title(
        "Distribution Of Players According To Their Skills", plt
        )
    return True


def preferred_foot_numbers(foot: str)-> int:
    return fifa.loc[fifa["Preferred Foot"] == foot].count()[0]


def preferred_foot_pie_chart()-> plt:
    labels = ["left", "right"]
    colors = ["blue", "red"]
    left = preferred_foot_numbers("left")
    right = preferred_foot_numbers("right")
    plt.pie(left, right, labels=labels, 
            colors=colors, autopct="%.2f%%")
    set_title("Distribution Of Players According To Their Preferred Foot"
              ,plt)
    return plt


def set_title(title:str, plt: plt)-> None:
    plt.title(title, 
        fontdict={"fontsize": "20", "fontweight": "bold", }
        )


def weigth_pie_chat():
    light = fifa.loc[fifa.Weigth < 125].count()[0]
    light_medium = fifa.loc[fifa.Weigth >= 125 and fifa.Weigth < 150].count()[0]
    medium = fifa.loc[fifa.Weigth >= 150 and fifa.Weigth < 175].count()[0]
    medium_heavy = fifa.loc[fifa.Weigth >= 175 and fifa.Weigth < 200].count()[0]
    heavy = fifa.loc[fifa.Weigth >= 200].count()[0]

    weigths = [light, light_medium, medium, medium_heavy, heavy]
    labels = ["light", "light_medium", "medium", "medium_heavy", "heavy"]
    explode = [0.4, 0.2, 0, 0, 0.4]

    plt.style.use("ggplot")
    plt.pie(weigths, labels=labels, autopct="%.2f%%", 
            pctdistance=0.8, explode=explode)
    set_title("Weight Distribution Of Players in (lbs)", plt)