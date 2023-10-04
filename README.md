**Repository Name**: 
```
Nightlight-Data-Visualization
```

---

**README.md**:
```
# Nightlight Data Visualization

This repository contains scripts and tools to visualize nightlight data from `.tif` files stored in an S3 bucket.

## Overview

The main script, `tif_to_dfs.py`, fetches a specified `.tif` file from an S3 bucket and visualizes the data using `matplotlib`. The data represents nightlight observations and can be used for various analytical purposes.

## Prerequisites

- Python 3.11.5
- Required Python libraries: `boto3`, `botocore`, `rasterio`, `matplotlib`

## Usage

1. Clone the repository:
```
git clone https://github.com/[Your_GitHub_Username]/Nightlight-Data-Visualization.git
```

2. Navigate to the repository directory:
```
cd Nightlight-Data-Visualization
```

3. Run the visualization script:
```
./tif_to_dfs.py
```

## Contributing

If you have suggestions or improvements, feel free to fork this repository and create a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License.

## Acknowledgements

- Data source: `globalnightlight` S3 bucket
- Special thanks to [Ariane] for the initial setup and visualization script.
```

---
