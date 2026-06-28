-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS finance;

-- Create the user 'finance' that can connect from any host ('%')
-- Replace 'your_strong_password' with a secure password
CREATE USER 'finance'@'%' IDENTIFIED BY '!QAZ2wsx#EDC4rfv';

-- Grant all privileges on the 'finance' database to the 'finance' user
GRANT ALL PRIVILEGES ON finance.* TO 'finance'@'%';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Optional: To verify the grants for the user
SHOW GRANTS FOR 'finance'@'%';
