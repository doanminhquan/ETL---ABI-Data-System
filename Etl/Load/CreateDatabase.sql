DROP DATABASE IF EXISTS DemoETL;

CREATE DATABASE DemoETL;

USE DemoETL;

Create TABLE users(
    user_id nvarchar(256) primary key,
    device_brand_name nvarchar(100),
    device_operating_system nvarchar(100),
    device_operating_system_version nvarchar(100),
    first_open_date datetime
);

Create TABLE session(
    session_id nvarchar(256) primary key NULL,
    user_id nvarchar(256),
    start_time datetime,
    duration bigint(255) NULL
);

CREATE TABLE event(
    event_id nvarchar(256) primary key,
    event_date date,
    event_time datetime,
    event_name text,
	event_parameter text,
    event_previous_time datetime,
    user_id nvarchar(256)
);

CREATE TABLE retention(
    date_retention datetime,
    retenrion_rate_d1 float,
    retenrion_rate_d3 float,
    retenrion_rate_d5 float,
    retenrion_rate_d7 float,
    retenrion_rate_d30 float
);

CREATE TABLE engagement_time(
    user_id nvarchar(256),
    session_times_per_day int,
    time_per_day bigint
);

CREATE TABLE advertising(
    ads_id nvarchar(256),
    user_id nvarchar(256),
    ad_type nvarchar(100),
    ad_duration int,
    ad_achievement text,
    ad_revenue int
);