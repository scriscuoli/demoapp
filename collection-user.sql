-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS collection;

-- Create the user 'collection' that can connect from any host ('%')
-- Replace 'your_strong_password' with a secure password
CREATE USER 'collection'@'%' IDENTIFIED BY '!QAZ2wsx#EDC4rfv';

-- Grant all privileges on the 'collection' database to the 'collection' user
GRANT ALL PRIVILEGES ON collection.* TO 'collection'@'%';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Optional: To verify the grants for the user
SHOW GRANTS FOR 'collection'@'%';
