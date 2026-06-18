agents = """
CREATE TABLE agents(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
speciality VARCHAR(50),
is_active BOOLEAN DEFAULT TRUE,
completed_missions INT DEFAILT 0,
failed_missions INT DEFAULT 0,
agent_rank ENUM("Junior", "Senior", "Commander")
);"""

mission = """
CREATE TABLE mission(
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(100),
description TEXT,
location VARCHAR(50),
difficulty INT,
importance INT,
status VARCHAR(15) DEFAULT NEW,
risk_level VARCHAR(8),
assigned_agent_id INT DEFAULT NULL)
"""