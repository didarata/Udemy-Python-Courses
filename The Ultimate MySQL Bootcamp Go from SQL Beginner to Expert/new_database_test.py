from asyncio.windows_events import NULL

from mysqlx.protobuf.mysqlx_crud_pb2 import TABLE

CREATE TABLE IF NOT EXISTS jobs (
    jobs_id INT AUTO_INCREMENT PRIMARY KEY,
    titles VARCHAR(255) NOT NULL,
    start_date DATE,
    due_date DATE,
    status TINYINT,NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;