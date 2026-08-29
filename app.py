import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/classify"


st.title("AI Animal Classification")

st.write(
    "Enter the name of a creature and the local Qwen AI model "
    "will classify it."
)


name = st.text_input(
    "Enter creature name"
)


if st.button("Classify"):

    if name.strip() == "":

        st.error(
            "Please enter a creature name."
        )

    else:

        try:

            response = requests.get(
                API_URL,
                params={
                    "name": name
                },
                timeout=60
            )

            response.raise_for_status()

            data = response.json()

            classification = data["classification"]

            if classification == "Unknown":

                st.warning(
                    f"{name.title()} could not be classified."
                )

            else:

                st.success(
                    f"{name.title()} → {classification}"
                )

            st.write(
                f"Model: {data['model']}"
            )

        except requests.exceptions.RequestException as error:

            st.error(
                f"Unable to connect to FastAPI: {error}"
            )