-- Create the user with the required privileges and set the password
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';

-- Make sure the privileges are applied immediately
FLUSH PRIVILEGES;
