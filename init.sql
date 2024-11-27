CREATE TABLE beatsheets (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

CREATE TABLE beats (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    beatsheet_id INTEGER REFERENCES beatsheets(id)
);

CREATE TABLE acts (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    duration INTEGER,
    camera_angle TEXT,
    beat_id INTEGER REFERENCES beats(id)
);

-- Insert sample data into beatsheets
INSERT INTO beatsheets (title) VALUES
('Sample Beatsheet 1'),
('Sample Beatsheet 2'),
('Sample Beatsheet 3');

-- Insert sample data into beats
INSERT INTO beats (description, timestamp, beatsheet_id) VALUES
('sample beat 1.1', NOW(), 1),
('sample beat 1.2', NOW(), 1),
('sample beat 2', NOW(), 2);

-- Insert sample data into acts
INSERT INTO acts (description, timestamp, duration, camera_angle, beat_id) VALUES
('Mission Briefing', NOW(), 120, 'Wide shot', 1),
('Challenge', NOW(), 150, 'Close-up', 1),
('Action', NOW(), 150, 'Panoramic shot', 1),
('Twist', NOW(), 150, 'Close-up', 1),
('Success', NOW(), 150, 'Wide shot', 2),
('Meeting', NOW(), 200, 'Panoramic shot', 2);
('Connection', NOW(), 200, 'Close-up', 3);