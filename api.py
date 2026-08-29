from fastapi import FastAPI, HTTPException

from classification_logic import classify_creature


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Animal Classification API"
    }


@app.get("/classify")
def classify(name: str):

    if name.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Name cannot be empty"
        )

    try:
        result = classify_creature(name)

        return {
            "name": name,
            "classification": result,
            "model": "qwen2.5:0.5b"
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"AI model error: {str(error)}"
        )