import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_fuctions import set_title


fifa = pd.read_csv("data/fifa_data.csv")


def clean_fifa():
    fifa.Weight = [
        int(x.rstrip("lbs")) if type(x) == str else x for x in fifa.Weight
        ]


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


def box_plot(*teams: str)-> plt:
    """creates a plot according to any contry/countries specified"""   
    Overolls = {}
    for team in teams:
        try:
            Overolls[team] = fifa.loc[fifa[team] == team]["Overoll"]
        except:
            print(f"invalid country name or format {team}")
    
    plt.xlabel("Teams")
    plt.ylabel("Fifa Overoll Rating")
    set_title("Box Plot For Different teams", plt)
    boxes = plt.boxplot(Overolls.values(), label=Overolls.keys())
    change_colour(boxes)
    return plt


def change_colour(boxplots: plt.boxplot)-> None:
    for boxplot in boxplots:
        boxplot.set(color="ab0133")
        boxplot.set(facecolor="bd778899") 
