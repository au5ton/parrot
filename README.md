# parrot

Exposes Minecraft RCON as a REST API. Driven by subprocess calls to [Tiiffi/mcrcon](https://github.com/Tiiffi/mcrcon).


## Installation + Usage

- Clone repo
- `pip3 install -r requirements.txt`
- `mkdir ~/.parrot-mc`
- `cp config.example.ini ~/.parrot-mc/config.ini`
- Update MCRCON information in your preferred text editor: 
  
  `nano ~/.parrot-mc/config.ini`

- Get help:

  `./server.py --help`

- Run the server:
  
  `./server.py`

- Access the server: `http://127.0.0.1:5000/`
