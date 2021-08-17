# visualization
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


def plot_distribution(var, title="", xlabel=""):
    """
        Compute and plot distribution of variable
        
        Params:
            - var - pandas.Series
            - title - string. histogram title
            - xlabel - string. x axis label
    """
    plt.hist(var, bins="fd")
    plt.axvline(var.mean(), c="red", label=f"mean: {np.round(var.mean(), 2)}")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.legend()
    plt.show()
    
def plot_scatter_grid(dataset, X_columns, target, rows, cols, title):
    """
        Plot grid of scatter plots
        Params:
            - dataset - pandas.Dataframe
            - X_columns - list of columns names
            - target - taget column name
            - rows - number of rows
            - cols - number of cols
            - title
    """
    fig = plt.figure(figsize=(20, 20))
    gs = fig.add_gridspec(nrows=rows, ncols=cols)

    y = dataset[target]
    
    for row in range(rows):
        for col in range(cols):
            index = row * cols + col
            if index >= len(X_columns):
                break
                
            x_col = X_columns[index]
            ax = fig.add_subplot(gs[row, col])
            ax.scatter(dataset[x_col], y)
            
            ax.set_xlabel(x_col)
            ax.set_ylabel(target)
            
    plt.suptitle(title, fontsize=20)
    
def print_min_feature_info(dataset, feature):
    """
        Print information about feature minimum value
    """
    id_min = feature.idxmin()
    
    print(f"target: {dataset.loc[id_min].target}")
    print(f"{feature.name} : {feature.min()}")
    print(f"Excerpt:\n {dataset.loc[id_min].excerpt}")
    
    
def print_max_feature_info(dataset, feature):
    """
        Print information about feature maximum value
    """
    id_max = feature.idxmax()
    
    print(f"target: {dataset.loc[id_max].target}")
    print(f"{feature.name} : {feature.max()}")
    print(f"Excerpt:\n {dataset.loc[id_max].excerpt}")
