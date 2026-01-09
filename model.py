import random
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agents import ScannerAgent, SortingAgent, TrashItem

class WasteModel(Model):
    def __init__(self, width=20, height=1):
        super().__init__() #initialize model and view
        self.grid = MultiGrid(width, height, torus=False) #torus makes trash "fall off"
        self.schedule = RandomActivation(self) #agents act on random order one per step
        self.width = width #store width to see if trash reached end
        
        scanner = ScannerAgent(self.next_id(), self) 
        self.grid.place_agent(scanner, (0, 0)) #makes a scanner at start
        self.schedule.add(scanner)

        categories = ["plastic", "paper", "metal", "glass"] #srotable garbage types
        for i, cat in enumerate(categories):
            sorter = SortingAgent(self.next_id(), self, cat)
            self.grid.place_agent(sorter, (5 + (i * 5), 0))  #sorters at 5,10,15,20
            self.schedule.add(sorter)

    def spawn_trash(self):
        if random.random() < 0.3:
            cat = random.choice(["plastic", "paper", "metal", "glass", "biodegradable"])
            item = TrashItem(self.next_id(), self, cat)
            self.grid.place_agent(item, (0, 0))
            self.schedule.add(item) #creating trash at start from a random category

    def move_trash(self): #each step we move all instances of trash one cell to the right
        for agent in self.schedule.agents:
            if isinstance(agent, TrashItem):
                x, y = agent.pos
                if x < self.width - 1:
                    self.grid.move_agent(agent, (x + 1, y))
                else:
                    self.grid.remove_agent(agent)
                    self.schedule.remove(agent)

    def step(self):
        self.spawn_trash()
        self.move_trash()
        self.schedule.step()