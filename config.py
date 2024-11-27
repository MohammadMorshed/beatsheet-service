import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/beatsheet_db")

NEXT_ACT_TRAINING_DATA = [
    # Classic story arcs
    ["Intro", "Setup", "Conflict", "Climax", "Resolution"],
    ["Prologue", "Intro", "Conflict", "Twist", "Climax", "Denouement"],
    ["Intro", "Exposition", "Conflict", "Cliffhanger", "Climax", "Resolution"],
    ["Introduction", "Rising Action", "Climax", "Falling Action", "Conclusion"],

    # Episodic sequences
    ["Episode Start", "Setup", "Mini-Conflict", "Resolution", "Transition"],
    ["Setup", "Challenge", "Conflict", "Breakthrough", "Resolution"],
    ["Backstory", "Setup", "Minor Conflict", "Major Conflict", "Resolution"],

    # Action-oriented sequences
    ["Mission Briefing", "Challenge", "Action", "Twist", "Success"],
    ["Setup", "Ambush", "Chase", "Victory", "Debrief"],
    ["Tension", "Conflict", "Fight Scene", "Climax", "Aftermath"],

    # Drama and emotional arcs
    ["Meeting", "Connection", "Misunderstanding", "Reconciliation", "Closure"],
    ["Setback", "Reflection", "Plan", "Action", "Success"],
    ["Loss", "Grief", "Understanding", "Acceptance", "Growth"],

    # Mystery/thriller arcs
    ["Discovery", "Investigation", "Complication", "Revelation", "Resolution"],
    ["Clue Found", "Investigation", "Red Herring", "Breakthrough", "Final Showdown"],
    ["Setup", "Suspense", "Climax", "Twist Ending", "Resolution"],

    # Comedy sequences
    ["Setup", "Joke", "Reaction", "Conflict", "Punchline"],
    ["Misunderstanding", "Escalation", "Ridiculous Resolution", "Reconciliation"],
    ["Setup", "Wacky Scenario", "Chaos", "Climax", "Happy Ending"],

    # Fantasy or adventure arcs
    ["Call to Adventure", "Preparation", "Journey", "Obstacle", "Victory"],
    ["Setup", "Quest Given", "Challenge", "Betrayal", "Redemption"],
    ["Ordinary World", "Inciting Event", "Journey", "Climax", "Return"],

    # Sci-fi arcs
    ["Introduction", "Discovery", "Complication", "Resolution", "Aftermath"],
    ["First Contact", "Conflict", "Compromise", "Resolution", "New Era"],
    ["Setup", "Experiment", "Failure", "Breakthrough", "Impact"],

    # Unique and creative arcs
    ["Dream Sequence", "Realization", "Action", "Revelation", "Closure"],
    ["Intro", "Conflict", "Split Timeline", "Reunion", "Resolution"],
    ["Setback", "Support", "Action", "Climax", "Transformation"],
    ["Introduction", "Choice", "Consequence", "Recovery", "Resolution"],
    ["Preparation", "Challenge", "Failure", "Retry", "Success"],

    # Nonlinear narratives
    ["Climax", "Backstory", "Conflict", "Resolution", "Prologue"],
    ["Ending", "Flashback", "Conflict", "Setup", "Finale"],
    ["Twist", "Conflict", "Climax", "Intro", "Resolution"],
]