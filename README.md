# Recommendation-system

## Overview
This project is an E-commerce recommendation system built using Python and Streamlit. The application allows users to select products, add them to a cart, and receive product recommendations based on the items in their cart. The system uses the Apriori algorithm for generating association rules from the dataset.

## Features
  Product selection and quantity input
  
  Add products to the cart
  
  View cart with options to increase or decrease quantities or remove items
  
  Receive recommendations based on cart contents
  
  Recommendations are generated using the Apriori algorithm
  
  User-friendly interface built with Streamlit

## Clone the repository:

    git clone https://github.com/yourusername/repo-name.git
    cd repo-name
    
## Create and activate a virtual environment:

    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`

## Install the required dependencies:

    pip install -r requirements.txt
    
Run the Streamlit app:

    streamlit run app.py

## Usage
### Start the application:
  Run the Streamlit app as described above.

### Select a product and quantity:
  Use the sidebar to select a product from the dropdown and specify the quantity.

### Add to cart:
  Click the "Add to Cart" button to add the selected product and quantity to the cart.

### View and manage cart:
  The cart is displayed at the bottom of the main page, where you can adjust quantities or remove items.

### View recommendations:
  Recommendations based on the items in your cart are displayed on the right side of the page.

## Dataset
The dataset used in this project was obtained from Kaggle and includes the following columns:

BillNo

Itemname

Quantity

Date

Price

CustomerID

Country

## Apriori Algorithm
The Apriori algorithm is used to generate association rules from the transaction data. It identifies frequent itemsets and derives rules that highlight the relationships between items in the dataset.

## Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss the changes you would like to make.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Special thanks to the contributors of the open-source libraries and tools used in this project.
Thanks to Kaggle for providing the dataset.
