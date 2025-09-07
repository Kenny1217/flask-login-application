
-- Create database user
CREATE USER flask_app_user WITH ENCRYPTED PASSWORD 'admin';

-- Add grants to user
GRANT ALL PRIVILEGES ON DATABASE flask_app_database TO flask_app_user;
