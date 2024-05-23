# EcoNest

## Overview

EcoNest is a web application designed to help users discover average rental prices in neighborhoods near specific landmarks. Whether you're relocating for work, studying abroad, or simply curious about housing costs in various areas, EcoNest provides you with up-to-date and accurate rent data.

This project was developed during the hackathon "Override" in September 2023.

## Features

- **Search by Landmark**: Enter a landmark to find the average rent in nearby neighborhoods.
- **Interactive Map**: Visualize rental prices on an interactive map for easy comparison.
- **Filter Options**: Filter results by property type, number of bedrooms, and price range.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following software installed on your machine:

- [Python](https://www.python.org/) (v3.8 or later)
- [Django](https://www.djangoproject.com/) (v3.x or later)
- [MongoDB](https://www.mongodb.com/) (for database)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ArshdKhan/EcoNest.git
   cd EcoNest
   ```

2. **Set up a virtual environment and activate it**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory and add the following variables:
   ```
   MONGODB_URI=your_mongodb_connection_string
   MAP_API_KEY=your_map_api_key
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

   The application will open in your default browser at `http://localhost:8000`.

## Usage

1. **Search for a Landmark**: Enter the name of a landmark in the search bar.
2. **View Average Rents**: See average rental prices displayed on the map.
3. **Apply Filters**: Use filters to narrow down your search based on your preferences.

---

Thank you for using EcoNest! We hope it helps you find the perfect place to live.
