import folium
import pandas as pd
from pathlib import Path

def create_sound_map():
    # Read the locations data
    df = pd.read_csv('data/locations.csv')
    
    # Initialize the map (centered arbitrarily — fit_bounds will adjust it)
    m = folium.Map(
        location=[41.0365, 28.9814],  # Center of İstiklal Caddesi
        zoom_start=16,
        tiles='OpenStreetMap'
    )
    
    # Add markers for each sound location
    for _, row in df.iterrows():
        # Create HTML content for the popup
        html = f'''
        <div style="width: 200px;">
            <h4>{row['name']}</h4>
            <audio controls style="width: 100%;">
                <source src="{row['soundfile']}" type="audio/mp4">
                Your browser does not support the audio element.
            </audio>
            <p>{row['description']}</p>
            <p><small>Recorded: {row['timestamp']}</small></p>
        </div>
        '''
        
        # Create the marker with popup
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(html, max_width=300),
            tooltip=row['name']
        ).add_to(m)
    
    # Fit the map to all markers
    bounds = df[['latitude', 'longitude']].values.tolist()
    m.fit_bounds(bounds)
    
    # Save the map
    output_file = 'index.html'
    m.save(output_file)
    print(f"Map has been generated and saved as {output_file}")

if __name__ == "__main__":
    create_sound_map() 