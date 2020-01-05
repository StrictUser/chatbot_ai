import json
import apiai

# using api.ai - works with python v3.6


def send_message(message):
    request = apiai.ApiAI('7fa8d77c03744f709d1db596627c54d0').text_request()
    request.lang = 'en'
    request.session_id = 'session_1'
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    print (response["result"]["fulfillment"]["speech"])
    return response["result"]["action"]


print("Input your message: ")
message = input()
action = None

while True:
    action = send_message(message)
   if action == "smalltalk.greetings.buy":
       break
    message = input()

#  using dialogflow
'''
def send_message_dlgflw(project_id, session_id, messages, lang_code):
    import dialogflow_v2 as dialogflw
    session_clnt = dialogflw.SessionsClient()

    session = session_clnt.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for message in messages:
        text_input = dialogflw.types.TextInput(text=message,
                                               language_code=lang_code)

        query_input = dialogflw.types.QueryInput(text=text_input)

        response = session_clnt.detect_intent(session=session,
                                              query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected Intet: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfilment_text))
'''