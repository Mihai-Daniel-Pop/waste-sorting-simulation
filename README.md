This is a project which uses agent based models (ABM)
It uses Python and the Mesa(specifically the 2.2.1 version anything 3.x doesn't work) framework to simulate robots identifying trash and adding it to the corresponding bins
All visible in a grid like enviorment
### How to install
1. Clone repository
   git clone [https://github.com/Mihai-Daniel-Pop/waste-sorting-simulation.git](https://github.com/Mihai-Daniel-Pop/waste-sorting-simulation.git)
   cd waste-sorting-simulation
2. Create a virtual environment:
# Linux/Mac
    python3 -m venv .venv
    source .venv/bin/activate
# Windows
    python -m venv .venv
    .venv\Scripts\activate
3. Install dependencies:
    pip install -r requirements.txt

### How to use
1. Run the server
    python run.py 
    This will open your browser at the adress http://127.0.0.1:8521