from fastapi import FastAPI
import uvicorn


app = FastAPI()

app.route("/")
def h():
    return {
        "hellow":"world"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)