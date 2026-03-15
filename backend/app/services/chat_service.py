from app.ml.predict import predict_response


def get_chatbot_response(message: str):
    return predict_response(message)