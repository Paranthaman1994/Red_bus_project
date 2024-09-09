# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

## Project Overview

The **Redbus Data Scraping and Filtering with Streamlit Application** is designed to automate the extraction, 
storage, and visualization of bus travel data from the Redbus website. By leveraging Selenium for web scraping and Streamlit 
for building an interactive web application, this project addresses critical needs in the transportation industry, such as market analysis, 
customer service enhancement, and competitor analysis.

## Domain
- **Transportation**

## Problem Statement

The project aims to revolutionize the transportation industry by providing a comprehensive solution for collecting,
analyzing, and visualizing bus travel data. By utilizing Selenium to scrape data from Redbus, the project automates the 
extraction of detailed information such as bus routes, schedules, prices, and seat availability.
The resulting data and analysis tools significantly improve operational efficiency and strategic planning.

## Business Use Cases

The solution can be applied to various business scenarios, including:

- **Travel Aggregators:** Providing real-time bus schedules and seat availability for customers.
- **Market Analysis:** Analyzing travel patterns and preferences for market research.
- **Customer Service:** Enhancing user experience by offering customized travel options based on data insights.
- **Competitor Analysis:** Comparing pricing and service levels with competitors.

## Approach

### 1. Data Scraping

- Use **Selenium** to automate the extraction of Redbus data, including routes, schedules, prices, and seat availability.

### 2. Data Storage

- Store the scraped data in a structured **SQL database** for easy retrieval and analysis.

### 3. Streamlit Application

- Develop a **Streamlit application** to display and filter the scraped data.
- Implement various filters such as bus type, route, price range, star rating, and seat availability.

### 4. Data Analysis/Filtering

- Use SQL queries to retrieve and filter data based on user inputs.
- Enable users to interact with and filter the data dynamically through the Streamlit application.

## Results

- Successfully scrape data from at least 10 Government State Bus Transport services on the Redbus website using Selenium. Also include private bus information for selected routes.
- Store the data in a structured SQL database.
- Develop an interactive and user-friendly Streamlit application for data filtering and visualization.

## Technical Tags

- **Web Scraping**
- **Selenium**
- **Streamlit**
- **SQL**
- **Data Analysis**
- **Python**
- **Interactive Application**

### Source

- **Data Source:** Data is scraped from the Redbus website.
- **Link:** [Redbus](https://www.redbus.in/)

### Format

- **Storage:** The scraped data is stored in a SQL database.

### Required Fields

- **Bus Route Name:** Captures the start and end locations of each bus journey.
- **Bus Route Link:** Link to detailed route information.
- **Bus Name:** Name of the bus or service provider.
- **Bus Type:** Type of bus (Sleeper/Seater/AC/Non-AC).
- **Departing Time:** Scheduled departure time.
- **Duration:** Total journey duration.
- **Reaching Time:** Expected arrival time.
- **Star Rating:** Rating provided by passengers.
- **Price:** Ticket cost.
- **Seat Availability:** Number of seats available at the time of data scraping.

## Database Schema

### Table: `bus_routes`

| Column Name    | Data Type | Description                               |
|----------------|-----------|-------------------------------------------|
| `id`           | INT       | Primary Key (Auto-increment)              |
| `route_name`   | TEXT      | Bus Route information for each state      |
| `route_link`   | TEXT      | Link to the route details                 |
| `busname`      | TEXT      | Name of the bus                           |
| `bustype`      | TEXT      | Type of the bus                           |
| `departing_time` | TIME    | Departure time                            |
| `duration`     | TEXT      | Duration of the journey                   |
| `reaching_time` | TIME     | Arrival time                              |
| `star_rating`  | FLOAT     | Rating of the bus                         |
| `price`        | DECIMAL   | Price of the ticket                       |
| `seats_available` | INT    | Number of seats available                 |
