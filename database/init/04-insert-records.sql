
-- Insert records into ROLES table
INSERT INTO ROLES (ROLE_NAME, ROLE_DESCRIPTION)
VALUES 
    ('Admin', 'Administrator with full access'),
    ('User', 'Regular user with limited access');

-- Insert records into ACTIVE_STATUS table
INSERT INTO ACTIVE_STATUS (ACTIVE_STATUS_NAME, ACTIVE_STATUS_DESCRIPTION)
VALUES
    ('Active', 'User is active and can log in'),
    ('Inactive', 'User is inactive and cannot log in'),
    ('Suspended', 'User is temporarily suspended'),
    ('Pending', 'User registration is pending approval');
