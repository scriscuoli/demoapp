-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS accounts;

-- Create the user 'accounts' that can connect from any host ('%')
-- Replace 'your_strong_password' with a secure password
CREATE USER 'accounts'@'%' IDENTIFIED BY 'SpenceR315!!';

-- Grant all privileges on the 'accounts' database to the 'accounts' user
GRANT ALL PRIVILEGES ON accounts.* TO 'accounts'@'%';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Optional: To verify the grants for the user
SHOW GRANTS FOR 'accounts'@'%';
