<img height=150 src="img/Cyan_Parrot.png">

# parrot

Exposes Minecraft RCON as a REST API. Driven by subprocess calls to [Tiiffi/mcrcon](https://github.com/Tiiffi/mcrcon).

When the server is started, [Tiiffi/mcrcon](https://github.com/Tiiffi/mcrcon) is installed to `~/.parrot-mc/` and the files are `chmod`'d to have execute permission. If this action is impossible in your environment, manually modifying Parrot might be necessary.

## Dependencies
- Python 3.6+
- Node.js (`node`) accessible in PATH

## Installation + Usage

- Clone repo
- `pip3 install -r requirements.txt`
- `mkdir ~/.parrot-mc`
- Update configuration:
  - (Option 1): Create a config.ini file

    `cp config.example.ini ~/.parrot-mc/config.ini`
  
  - (Option 2): Specify these environment variables at runtime: `MCRCON_HOST`, `MCRCON_PORT`, `MCRCON_PASS`.

- Run the server:
  
  `gunicorn server:app`

- Access the server: `http://127.0.0.1:8000/`

## API

### `GET /`
### `GET /api/cmd/<command>`
### `GET /api/list`
### `GET /api/slots`
### `GET /api/player/<player>`
