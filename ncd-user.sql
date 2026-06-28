-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS ncd;

-- Create the user 'ncd' that can connect from any host ('%')
-- Replace 'your_strong_password' with a secure password
CREATE USER 'ncd'@'%' IDENTIFIED BY '!QAZ2wsx#EDC4rfv';

-- Grant all privileges on the 'ncd' database to the 'ncd' user
GRANT ALL PRIVILEGES ON ncd.* TO 'ncd'@'%';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Optional: To verify the grants for the user
SHOW GRANTS FOR 'ncd'@'%';
