import uvicorn
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/headers")
async def read_headers(x_token: list[str] = Header(default=None), user_agent: str = Header(default="My User Agent 1.0")):
    return {"x-token": x_token, "user-agent": user_agent}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
