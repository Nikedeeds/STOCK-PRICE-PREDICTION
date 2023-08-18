def get_predicted_close_price(entities):
    stock_symbol = None
    date = None

    # Extract stock_symbol and date from entities
    for entity_text, entity_label in entities:
        if entity_label == 'STOCK_SYMBOL':
            stock_symbol = entity_text
        elif entity_label == 'DATE':
            date = entity_text

    # TODO: Call the logic functiion to fetch the predicted close price
    predicted_close = fetch_predicted_close_price(stock_symbol, date)

    return predicted_close
def main():
    st.title("Stock Prediction Chatbot")

    user_input = st.text_input("User: ")
    if st.button("Submit"):
        entities = extract_entities(user_input)
        response = get_response(user_input, entities)
        st.text("Bot: " + response)

if __name__ == "__main__":
    main()