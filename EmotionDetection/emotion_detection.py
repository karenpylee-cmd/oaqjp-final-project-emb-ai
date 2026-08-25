import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)
    emotionPredictions_list = formatted_response['emotionPredictions']
    emotion_dict = emotionPredictions_list[0]

    anger_score = emotion_dict['emotion']['anger']
    disgust_score = emotion_dict['emotion']['disgust']
    fear_score = emotion_dict['emotion']['fear']
    joy_score = emotion_dict['emotion']['joy']
    sadness_score = emotion_dict['emotion']['sadness']
    score_dict = {'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score}

    # Get the emotion with the highest score
    dominant_emotion = max(score_dict, key=score_dict.get)
    score_dict['dominant_emotion'] = dominant_emotion

    return score_dict
    