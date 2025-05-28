# Sound Map Project

An interactive digital map that captures and reflects the sonic environment of İstiklal Caddesi and Taksim area. This project allows users to explore different sounds recorded at specific locations through an interactive map interface.

## Features

- Interactive map with clickable markers
- Audio playback for each location
- Descriptive information about each sound
- Zoomable and navigable interface
- Single HTML file output for easy sharing

## Project Structure

```
SoundMap/
├── data/
│   ├── audio/         # Audio recordings
│   └── locations.csv  # Sound location data
├── generate_map.py    # Main script to generate the map
├── requirements.txt   # Project dependencies
└── README.md         # This file
```

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Place your audio recordings in the `data/audio` directory

3. Create or update the `data/locations.csv` file with your sound data

4. Run the map generation script:
   ```bash
   python generate_map.py
   ```

5. Open the generated `index.html` in a web browser

## Data Format

The `locations.csv` file should contain the following columns:
- name: Name of the sound
- description: Short description of the sound
- latitude: GPS latitude
- longitude: GPS longitude
- soundfile: Path to the audio file
- timestamp: When the sound was recorded 