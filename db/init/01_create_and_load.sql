-- Drop old tables if exist
DROP TABLE IF EXISTS crm_events CASCADE;
DROP TABLE IF EXISTS crm_call_logs CASCADE;

CREATE TABLE crm_events (
    date_received              DATE,
    product                    TEXT,
    sub_product                TEXT,
    issue                      TEXT,
    sub_issue                  TEXT,
    consumer_complaint_narrative TEXT,
    tags                       TEXT,
    consumer_consent_provided  TEXT,
    submitted_via              TEXT,
    date_sent_to_company       DATE,
    company_response           TEXT,
    timely_response            TEXT,
    consumer_disputed          TEXT,
    complaint_id               TEXT,
    client_id                  TEXT
);

COPY crm_events
FROM '/data/CRMEvents.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',');

CREATE TABLE crm_call_logs (
    date_received  DATE,
    complaint_id   TEXT,
    rand_client    TEXT,
    phonefinal     TEXT,
    vru_line       TEXT,
    call_id        TEXT,
    priority       TEXT,
    type           TEXT,
    outcome        TEXT,
    server         TEXT,
    ser_start      TIME,
    ser_exit       TIME,
    ser_time       INTERVAL
);

COPY crm_call_logs
FROM '/data/CRMCallCenterLogs.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',');
