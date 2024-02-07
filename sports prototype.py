from FastAPI import FastAPI


APP=FastAPI()

Stats_sports_list={
    "Football":"%",
    "Basketball":"%",
    "Baseball":"%",
    "Soccer":"%",
}

@app.get("/Stats-sports")
def Stats-sports():
    return Stats-sports