from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional, List
import locale
from datetime import datetime
import os

app = FastAPI()

# --- SQLite DB config ---
os.makedirs("./data", exist_ok=True)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./glossary.db")
engine = create_engine(DATABASE_URL, echo=False)


# --- Модель данных ---
class Term(SQLModel, table=True):
    keyword: str = Field(primary_key=True)
    description: str


class TermCreate(BaseModel):
    description: str


# --- Создание таблиц ---
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# --- CRUD ---
@app.get("/terms", response_model=List[Term])
def get_all_terms():
    with Session(engine) as session:
        return session.exec(select(Term)).all()


@app.get("/terms/{keyword}", response_model=Term)
def get_term(keyword: str):
    with Session(engine) as session:
        term = session.get(Term, keyword)
        if not term:
            raise HTTPException(status_code=404, detail="Term not found")
        return term


@app.post("/terms/{keyword}", response_model=Term)
def post_term(keyword: str, term_data: TermCreate):
    with Session(engine) as session:
        if session.get(Term, keyword):
            raise HTTPException(status_code=400, detail="Term already exists")
        term = Term(keyword=keyword, description=term_data.description)
        session.add(term)
        session.commit()
        return term


@app.put("/terms/{keyword}", response_model=Term)
def update_term(keyword: str, term_data: TermCreate):
    with Session(engine) as session:
        term = session.get(Term, keyword)
        if not term:
            raise HTTPException(status_code=404, detail="Term not found")
        term.description = term_data.description
        session.add(term)
        session.commit()
        return term


@app.delete("/terms/{keyword}")
def delete_term(keyword: str):
    with Session(engine) as session:
        term = session.get(Term, keyword)
        if not term:
            raise HTTPException(status_code=404, detail="Term not found")
        session.delete(term)
        session.commit()
        return {"result": "deleted successfully"}


# --- Прочие маршруты ---
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/author')
def read_about():
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    return {'author': "Nick", "datetime": datetime.now().strftime("%A, %d.%m.%Y, %H:%M").title()}
