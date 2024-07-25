from spin_sdk import http
from spin_sdk.http import Request, Response
from spin_sdk import llm

class IncomingHandler(http.IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        res = llm.infer_with_options("llama2-chat", "write code to implement an Array in Java, C++, JavaScript and Rust", llm.InferencingParams(temperature=0.5, max_tokens=1024))
        return Response(
            200,
            {"content-type": "text/plain"},
            bytes(res.text, "utf-8")
        )
