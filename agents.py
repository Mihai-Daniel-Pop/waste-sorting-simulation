from mesa import Agent

class TrashItem(Agent): #general waste item template
    def __init__(self, unique_id, model, category):
        super().__init__(unique_id, model) #get mesa base agent initialized
        self.category = category   
        self.is_sorted = False

class ScannerAgent(Agent): #scans waste items
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model) #initialize agent from mesa

    def step(self):
        cell_contents = self.model.grid.get_cell_list_contents([self.pos]) #content of current cell
        
        for obj in cell_contents:
            if isinstance(obj, TrashItem):
                print(f"Scanner {self.unique_id} detected: {obj.category}") #scan and print category

class SortingAgent(Agent): 
    def __init__(self, unique_id, model, target_category): #here
        super().__init__(unique_id, model) #initialize agent from mesa
        self.target_category = target_category #categorty handled by this sotrer
        self.items_collected = 0 

    def step(self): 
        cell_contents = self.model.grid.get_cell_list_contents([self.pos]) #if the garbage is on the same cell as sorter
        
        for obj in cell_contents:
            if isinstance(obj, TrashItem) and not obj.is_sorted: #if trash item and not sorted
                if obj.category == self.target_category: #and it matches the category this sorter handles
                    self.collect_trash(obj) #colletion
                else:
                    print(f"Sorter ({self.target_category}) ignores {obj.category}") #or moving on

    def collect_trash(self, trash): #collect trash method
        trash.is_sorted = True  #if sorted
        self.items_collected += 1  #increment count of garbage 
        self.model.grid.remove_agent(trash) 
        self.model.schedule.remove(trash) #"delete" trash from model
        print(f"SUCCESS: {self.target_category} Sorter collected an item!")