# Heart Attack Prediction

A machine learning project to predict the likelihood of heart attack based on patient data. The project leverages data science techniques to aid in early detection and prevention of heart attacks.

## Features

- Data preprocessing and visualization
- Machine learning model training and evaluation
- Prediction of heart attack risk based on input features
- Easy-to-use scripts for training, testing, and inference

## Technologies Used

- Python
- scikit-learn 
- pandas, numpy, matplotlib, seaborn

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
git clone https://github.com/RAJPAL18/heart-attack-prediction.git
cd heart-attack-prediction
pip install -r requirements.txt
```

### Dataset

- Use the provided dataset (or download from [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease) if not included).
- Place the dataset in the `data/` folder.

### Usage

#### Training the Model

```bash
python train.py --data data/heart.csv
```

#### Testing the Model

```bash
python test.py --model models/model.pkl --data data/test.csv
```

#### Predicting Heart Attack Risk

```bash
python predict.py --model models/model.pkl --input sample_input.json
```

### Example Input

```json
{
  "age": 45,
  "sex": 1,
  "cp": 3,
  "trestbps": 130,
  "chol": 230,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.2,
  "slope": 2,
  "ca": 0,
  "thal": 2
}
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions, contact [RAJPAL18](https://github.com/RAJPAL18).

## References

- [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
