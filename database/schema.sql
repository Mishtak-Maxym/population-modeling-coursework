CREATE TABLE model_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE experiment_scenarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_type_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    n0 REAL NOT NULL,
    r REAL,
    k REAL,
    a REAL,
    sigma REAL,
    steps INTEGER,
    time_start REAL,
    time_end REAL,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_type_id) REFERENCES model_types(id)
);

CREATE TABLE simulation_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario_id INTEGER NOT NULL,
    seed INTEGER,
    status TEXT NOT NULL DEFAULT 'completed',
    figure_filename TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (scenario_id) REFERENCES experiment_scenarios(id)
);

CREATE TABLE simulation_points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,
    step_index INTEGER NOT NULL,
    time_value REAL,
    population_value REAL NOT NULL,
    FOREIGN KEY (run_id) REFERENCES simulation_runs(id)a
);

CREATE TABLE age_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE leslie_matrix_values (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario_id INTEGER NOT NULL,
    row_index INTEGER NOT NULL,
    column_index INTEGER NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (scenario_id) REFERENCES experiment_scenarios(id)
);

CREATE TABLE user_stories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    goal TEXT NOT NULL,
    benefit TEXT NOT NULL,
    acceptance_criteria TEXT
);
