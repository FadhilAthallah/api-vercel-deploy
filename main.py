#import package
from fastapi import FastAPI, Request, Response, HTTPException, Header

#testing api token key
API_KEY = "testingapitokenkey1234" 

#create new object
app = FastAPI()
@app.get('/')
def gethome():
    return{
        "message":"This is my API. Welcome!"
    }

@app.get('/see-headers')
def readHeaders(request:Request):
    #mengambil headers dari request
    headers = request.headers
    return{
        "message":'isi headers',
        'headers':headers.get('User-Agent')
    }

@app.get("/example")
def read_example_headers(request: Request):
    headers = request.headers
    # Access specific header values
    user_agent = headers.get("user-agent")
    authorization = headers.get("authorization")
    custom_header = headers.get("custom-header")

    return {
        "User-Agent": user_agent,
        "Authorization": authorization,
        "Custom-Header": custom_header
    }
@app.get("/example2")
def example_endpoint():
    content = "Hello, this is the response content."

    # Create a Response object and set custom headers
    response = Response(content=content)
    response.headers["X-Custom-Header"] = "This is custom value"
    response.headers["Authorization"] = "pass_token_1234"

    return response

@app.get("/protected")
def protect(api_key: str = Header(None)):

  if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

  return {"message":"This endpoint is protected by API Token Key.",
          "data":{"1":{"username":"lis","password":"nyamandilambung"},
                  "2":{"username":"gif","password":"whitecoffe"},
                  "3":{"username":"titan","password":"kopiluwak"}
          }
    }