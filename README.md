```markdown
# ForecastX-Intelligent-Stock-Price-Prediction

## Description

ForecastX-Intelligent-Stock-Price-Prediction is a project that utilizes LSTM (Long Short-Term Memory) models to predict stock prices. It includes data retrieval, preprocessing, model training, evaluation, and a simple user interface (UI) for obtaining predicted prices based on user input.

## What it does

The project performs the following tasks:

- Retrieves historical stock data for a given stock symbol using the Yahoo Finance API.
- Preprocesses and prepares the data for model training.
- Trains an LSTM model using the prepared data.
- Evaluates the performance of the trained model using various metrics such as mean absolute error, mean squared error, root mean squared error, and R-squared.
- Saves the trained model for future use.
- Provides a user interface (UI) where users can input stock data (open price, high price, low price, and volume) and obtain predicted prices based on the trained model.

## Project Structure

The project consists of the following files:

- `Stocks.ipynb`: Jupyter Notebook file containing the code for data preparation, model setup, data retrieval, preprocessing, model training, and evaluation.
- `UI.py`: Python script for creating a simple UI interface using Gradio library to interact with the trained model.
- `StockPricePrediction.h5`: Saved trained model file.
- `README.md`: Documentation file providing an overview of the project and instructions for usage.

## Requirements

Make sure you have the following dependencies installed:

- pandas
- yfinance
- datetime
- scikit-learn
- plotly
- numpy
- keras
- gradio
- tensorflow


## How to run

To run the project, follow these steps:

1. Clone the project repository:

```
git clone https://github.com/YourGithubName/ForecastX-Intelligent-Stock-Price-Prediction
```

2. Install the project dependencies:

```
cd ForecastX-Intelligent-Stock-Price-Prediction
pip install -r requirements.txt
```

3. Open the Jupyter Notebook file `Stocks.ipynb` and run the code cells sequentially to perform data preparation, model setup, data retrieval, preprocessing, model training, and evaluation.

4. Once the model training is complete, the trained model will be saved as `StockPricePrediction.h5`.

5. Run the Python script `UI.py` to launch the user interface (UI) where you can input stock data and obtain predicted prices:

```
python UI.py
```

6. In the UI interface, enter the required stock data (open price, high price, low price, and volume).

7. The predicted price will be displayed as the output.

```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

This project was developed by [Your Name]. Special thanks to the contributors and the open-source community for providing the necessary tools and libraries.

Feel free to contribute and enhance the project!

Please make sure to replace `[Your Name]` in the License section with your name or the appropriate attribution.
