from fastapi import FastAPI, HTTPException
from summarizer import summarize_medical_record


app = FastAPI()


patient_medical_record ="""
Patient: John Doe, 58yo Male.
Records:
- 2026-01-10: Routine checkup. BP 120/80, HR 72. Healthy.
- 2026-02-15: Follow up. BP 135/85, HR 78. Patient reports stress.
- 2026-04-01: Urgent care visit. BP 155/95, HR 92. Complaining of headaches.
- 2026-04-20: Today. BP 162/100, HR 98.
"""

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/summarizer-agent/summarize")
def read_root():
    return summarize_medical_record(patient_medical_record)
