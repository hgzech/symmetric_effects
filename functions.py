from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def show_demo():
    df = pd.DataFrame({"Intercept":[1,1,1,1],
                     "b_0": [400,400,400,400],
                     "is_pull":[.5,.5,-.5,-.5],
                     "b_1": [0,0,0,0],
                     "Response":["Pull","Pull","Push","Push"],
                     "b_2": [0,0,0,0],
                     "is_happy":[.5,-.5,.5,-.5],
                     "Expression":["Happy","Angry","Happy","Angry"],
                     "b_3": [0,0,0,0]})
    #df["rt"] = df.b_0 + df.is_pull * df.b_1 + df.is_happy * df.b_2 + df.is_pull * df.is_happy * df.b_3
    print(df[["Intercept", "b_0", "Response", "is_pull", "b_1", "Expression", "is_happy", "b_2", "b_3"]])
    def plot_func(main_happy, main_pull,happy_x_pull):
        df["b_1"] = main_pull
        df["b_2"] = main_happy
        df["b_3"] = happy_x_pull
        df["rt"] = df.b_0 + df.is_pull * df.b_1 + df.is_happy * df.b_2 + df.is_pull * df.is_happy * df.b_3
        print(df[["Intercept", "Response", "Expression", "rt"]])
        sns.lineplot(x="Response", y="rt", hue="Expression", data=df)

    interact(plot_func, main_happy = widgets.FloatSlider(value=0,
                                                   min=-100,
                                                   max=100,
                                                   step=5),
                        main_pull = widgets.FloatSlider(value=0,
                                                   min=-100,
                                                   max=100,
                                                   step=5),
                    happy_x_pull = widgets.FloatSlider(value=0,
                                                   min=-100,
                                                   max=100,
                                                   step=5));
