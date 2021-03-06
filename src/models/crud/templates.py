from pydantic import BaseModel


class ExerciseTemplate(BaseModel):
    name: str
    sets: int
    reps: int


class WorkoutTemplate(BaseModel):
    name: str
    exerciseTemplates: list[ExerciseTemplate]
