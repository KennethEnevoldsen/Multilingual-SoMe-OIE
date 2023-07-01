import json
from pathlib import Path

data_folder = Path(__file__).parent / "data"
filename = "export_35704_project-35704-at-2023-06-30-23-51-9a727c20.json"
data_path = data_folder / filename

with open(data_path) as f:
    data = json.load(f)

for sample in data:
    # sample = data[0]
    assert len(sample["annotations"]) == 1
    annotations = sample["annotations"][0]["result"]

    words_to_add = [
        anno["value"]["text"] for anno in annotations if anno["type"] == "textarea"
    ]
    words_to_add = [w for word in words_to_add for w in word]

    if len(words_to_add) == 0:
        continue
    original_text = sample["data"]["text"]
    ext_text = original_text + " ||| " + " ".join(words_to_add)
    sample["data"]["text"] = ext_text
    sample["meta"]["original_text"] = original_text

with open(data_folder / "extended_data.json", "w") as f:
    json.dump(data, f)
