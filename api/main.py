from fastapi import FastAPI


app = FastAPI()

app.route("/")
def h():
    return {
        "hellow":"world"
    }