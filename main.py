import os
import json

def update_json_with_music(folder_path, output_json_path):
    # Initialize the JSON structure
    music_data = {
        "_ids": [],
        "_loopMode": 0,
        "_selected": 0,
        "_shuffled": True
    }

    # add the music files to the JSON
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.mp3', '.wav', '.ogg')):  # Add more extensions if needed
                full_path = os.path.join(root, file)
                music_data["_ids"].append({"path": full_path, "type": 1})

    # Write the updated JSON to a file
    with open(output_json_path, 'w') as json_file:
        json.dump(music_data, json_file, indent=2)

folder_path = "D:\\Programs\\Steam\\steamapps\\common\\ULTRAKILL\\CyberGrind\\Music"
output_json_path = "slot1.json"

update_json_with_music(folder_path, output_json_path)
