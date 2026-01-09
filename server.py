from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from agents import ScannerAgent, SortingAgent, TrashItem
from model import WasteModel

def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true", 
        "r": 0.8, 
        "Layer": 0
    } #default portrayal fo agents

    if isinstance(agent, TrashItem): #if garbage item how to draw it
        portrayal["Layer"] = 1 #forefront
        portrayal["r"] = 0.5 #smaller than 0.8 like others
        
        if agent.category == "plastic":
            portrayal["Color"] = "red"
        elif agent.category == "paper":
            portrayal["Color"] = "blue"
        elif agent.category == "metal":
            portrayal["Color"] = "grey"
        elif agent.category == "glass":
            portrayal["Color"] = "green"
        elif agent.category == "biodegradable":
            portrayal["Color"] = "brown"
        else:
            portrayal["Color"] = "black"

    elif isinstance(agent, ScannerAgent): #scanner agent look and how to draw it
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.9
        portrayal["h"] = 0.9
        portrayal["Color"] = "black"
        portrayal["Layer"] = 0
        portrayal["text"] = "SCAN"
        portrayal["text_color"] = "white"

    elif isinstance(agent, SortingAgent): #sotrer agent look and how to draw it, same zise as scanner
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.9
        portrayal["h"] = 0.9
        portrayal["Layer"] = 0
        
        if agent.target_category == "plastic":
            portrayal["Color"] = "#ffcccc" #red
        elif agent.target_category == "paper":
            portrayal["Color"] = "#ccccff" #blue
        elif agent.target_category == "metal":
            portrayal["Color"] = "#cccccc" #grey
        elif agent.target_category == "glass":
            portrayal["Color"] = "#ccffcc" #green
        else:
            portrayal["Color"] = "black"
            
    return portrayal

grid = CanvasGrid(agent_portrayal, 25, 1, 1000, 100) #widht 25 height 1 pixel size 1000x100

server = ModularServer(
    WasteModel, 
    [grid], 
    "Intelligent Garbage Sorter", 
    {"width": 25, "height": 1} # FIX: Pass width=25
)

server.port = 8521