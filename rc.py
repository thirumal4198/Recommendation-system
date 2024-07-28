import streamlit as st
import pandas as pd
import pickle

# Load the pickled data
with open('cleaned_data.pkl', 'rb') as f:
    data = pickle.load(f)

with open('product_rec.pkl', 'rb') as f:
    product_rec = pickle.load(f)

# Function to get unique recommendations
def get_recommendations(cart_products, rules_df):
    recommended_products = []
    for item in cart_products:
        recommendations = rules_df[rules_df['Product'].apply(lambda x: item in x)]
        unique_recommendations = pd.Series([rec for sublist in recommendations['Recom'] for rec in sublist]).drop_duplicates().reset_index(drop=True)
        recommended_products.extend(unique_recommendations)
    return list(pd.Series(recommended_products).drop_duplicates().reset_index(drop=True))[:8]  # Return max 8 unique recommendations

# Streamlit app layout
st.title("E-commerce Recommendation System")

# Initialize session state for cart and recommended selections
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'recommended_selections' not in st.session_state:
    st.session_state.recommended_selections = []

# Create a two-column layout
col1, col2 = st.columns(2)

# Product selection in the left column
with col1:
    st.header("Select a Product")
    product_list = [item for sublist in product_rec['Product'] for item in sublist]
    product_list = list(set(product_list))  # Unique products
    selected_product = st.selectbox("Select a Product", product_list)
    quantity = st.number_input("Quantity", min_value=1, value=1, step=1)
    if st.button("Add to Cart"):
        st.session_state.cart.append((selected_product, quantity))
        st.success(f"Added {quantity} of {selected_product} to cart")

# Display recommendations in the right column
with col2:
    st.header("Recommended Products")
    if st.session_state.cart:
        cart_products = [item[0] for item in st.session_state.cart]
        recommended_products = get_recommendations(cart_products, product_rec)

        if recommended_products:
            st.write("Based on your cart items, we recommend the following products:")
            for i, product in enumerate(recommended_products):
                if st.checkbox(product, key=f'recommend_{i}'):
                    if product not in st.session_state.recommended_selections:
                        st.session_state.recommended_selections.append(product)
                else:
                    if product in st.session_state.recommended_selections:
                        st.session_state.recommended_selections.remove(product)

            if st.button("Add Selected Recommendations to Cart"):
                for product in st.session_state.recommended_selections:
                    st.session_state.cart.append((product, 1))  # Default quantity to 1
                st.session_state.recommended_selections.clear()  # Clear selections after adding to cart
                st.success("Selected recommended products added to cart.")
        else:
            st.write("No recommendations available.")
    else:
        st.write("Add items to your cart to see recommendations.")

# Display cart at the bottom
st.header("Cart")
if st.session_state.cart:
    cart_items = pd.DataFrame(st.session_state.cart, columns=['Product', 'Quantity'])

    for i, (product, quantity) in enumerate(st.session_state.cart):
        col1, col2, col3, col4 = st.columns(4)
        col1.write(product)
        new_quantity = col2.number_input('Quantity', min_value=1, value=quantity, step=1, key=f'qty_{i}')
        if col3.button('Update', key=f'update_{i}'):
            st.session_state.cart[i] = (product, new_quantity)
            st.experimental_rerun()
        if col4.button('Remove', key=f'remove_{i}'):
            st.session_state.cart.pop(i)
            #st.experimental_rerun()

    st.table(pd.DataFrame(st.session_state.cart, columns=['Product', 'Quantity']))
else:
    st.write('Your cart is empty.')

# Run the app (this line should be removed since it's not needed for Streamlit to work properly)
# if __name__ == '__main__':
#     st.run()
