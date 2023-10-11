import io
import json

from google.cloud import aiplatform

project = "622502247148"
endpoint_id = "2387631281157439488"
location = "us-central1"


def predict(input_text):
    """Predicts the output text for the given input text."""

    # Create a client.
    client = aiplatform.PredictionServiceClient()

    # Create a request.
    request = aiplatform.types.PredictRequest(
        endpoint=client.endpoint_path(project, location, endpoint_id),
        instances=[
            {
                "input_text": input_text,
            }
        ],
    )

    # Send the request and get the response.
    response = client.predict(request)

    # Handle the response.
    for prediction in response.predictions:
        return prediction.get("output_text")


if __name__ == "__main__":
    # Get the input text from the user.
    input_text = input("Input text: ")

    # Predict the output text.
    output_text = predict(input_text)

    # Print the output text to the console.
    print("Output text:", output_text)
