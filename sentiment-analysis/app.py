# from spin_sdk import http
# from spin_sdk.http import Request, Response
# from spin_sdk import llm
# import json
# import re

# PROMPT = """<<SYS>>
# You are a bot that generates sentiment analysis responses. Respond with a single positive, negative, or neutral.
# <</SYS>>
# [INST]
# Follow the pattern of the following examples:

# User: Hi, my name is Bob
# Bot: neutral

# User: I am so happy today
# Bot: positive

# User: I am so sad today
# Bot: negative
# [/INST]

# User: """

# def handle_request(request):
#     request_body = json.loads(request.body)
#     sentence = request_body["sentence"].strip()
#     result = llm.infer_with_options("llama2-chat", PROMPT + sentence, llm.InferencingParams(temperature=0.5, max_tokens=3000))
#     response_body = json.dumps({"sentence": re.sub(r"\\nBot\: ", "", result.text)})
#     return Response(
#         200, {"content-type": "application/json"}, bytes(response_body, "utf-8")
#     )


from spin_sdk import http
from spin_sdk.http import Request, Response
from spin_sdk import llm
import json
import re

PROMPT = """<<SYS>>
You are a bot that generates sentiment analysis responses. Respond with a single positive, negative, or neutral.
<</SYS>>
[INST]
Follow the pattern of the following examples:

User: Hi, my name is Bob
Bot: neutral

User: I am so happy today
Bot: positive

User: I am so sad today
Bot: negative
[/INST]

User: """

class IncomingHandler(http.IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        request_body = json.loads(request.body)
        sentence = request_body["sentence"].strip()
        result = llm.infer_with_options("llama2-chat", PROMPT + sentence, llm.InferencingParams(temperature=0.5, max_tokens=3000))
        response_body = json.dumps({"sentence": re.sub("\\nBot\: ", "", result.text)})
        return Response(
            200, {"content-type": "application/json"}, bytes(response_body, "utf-8")
        )