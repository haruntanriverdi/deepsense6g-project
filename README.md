# Radar Aided 6G Beam Prediction: Deep Learning Algorithms and Real-World Demonstration
This is a python code package related to the following article:
Umut Demirhan, and Ahmed Alkhateeb, "[Radar Aided 6G Beam Prediction: Deep Learning Algorithms and Real-World Demonstration](https://ieeexplore.ieee.org/document/9771564),", in 2022 IEEE Wireless Communications and Networking Conference (WCNC), 2022, pp. 2655-2660

## Installation steps
1. Download [the radar aided beam prediction dataset of DeepSense 6G/Scenario 9](https://deepsense6g.net/radar-aided-beam-prediction/).
2. Clone the repository into a directory.
3. Extract the dataset into the repository directory 
4. Install the requeirements
```
pip install -r requirements.txt
```
5. For training run 
```
python training_ml.py
```
6. For testing model result
```
python scenario9_radar_beam-prediction_inference.py
```

## Conclusion 

Current Result

| Solution       | Top-1 | Top-2 | Top-3 | Top-4 | Top-5 |
| :------------- | ----- | ----- | ----- | ----- | ----- |
| Radar Cube     | 41.65 | 60.88 | 74.37 | 87.18 | 91.91 |
| Range Velocity | 42.33 | 60.88 | 74.20 | 83.81 | 89.54 |
| Range Angle    | 45.70 | 65.60 | 79.60 | 88.36 | 93.25 |

Our Result

| Solution       | Top-1 | Top-2 | Top-3 | Top-4 | Top-5 |
| :------------- | ----- | ----- | ----- | ----- | ----- |
| AdvencedCube   | 40.81 | 60.71 | 74.03 | 87.18 | 92.07 |
| Range Velocity | 42.66 | 59.87 | 72.68 | 81.96 | 88.70 |
| Range Angle    |45.19  | 65.43 | 78.92 | 87.86 | 93.09 |