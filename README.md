# Anki Flashcards Online Project

This project aims to create an online platform for users to access and study Anki flashcards. It leverages Docker to manage MySQL and MongoDB instances, ensuring a consistent and isolated development environment.

## Prerequisites

- Docker installed on your machine.
- Docker Compose installed on your machine.

## Getting Started

Follow these steps to set up the MySQL and MongoDB instances for the Anki Flashcards Online project.

### Step 1: Create a Docker Compose File

Create a `docker-compose.yml` file in your project directory. This file will define both the MySQL and MongoDB services, along with the necessary environment variables and initialization scripts.

```
yaml version: '3.8'

services: mysql: image: mysql:latest environment: MYSQL_ROOT_PASSWORD: MYSQLROOTPASSWORDMYSQLDATABASE:{MYSQL_DATABASE} MYSQL_USER: MYSQLUSERMYSQLPASSWORD:{MYSQL_PASSWORD} volumes: - mysql-data:/var/lib/mysql - ./init-mysql.sql:/docker-entrypoint-initdb.d/init-mysql.sql ports: - "3306:3306"

mongo: image: mongo:latest ports: - "27017:27017" volumes: - mongo-data:/data/db

volumes: mysql-data: mongo-data:
```

### Step 2: Create an `.env` File

Create a `.env` file in the root of your project directory. Add the MySQL root user, user, and password information to this file:

```
MYSQL_ROOT_PASSWORD=
MYSQL_USER= 
MYSQL_PASSWORD= 
MYSQL_DATABASE=OnlineFlashCards
```

### Step 3: Create the MySQL Initialization Script

Create a file named `init-mysql.sql` in the same directory as your `docker-compose.yml`. This script will create the `OnlineFlashCard` database and the `User` and `FlashCardDeck` tables.

```
sql CREATE DATABASE IF NOT EXISTS OnlineFlashCard; USE OnlineFlashCard;

CREATE TABLE User ( Gui VARCHAR(255) PRIMARY KEY, Name VARCHAR(255) NOT NULL, Mail VARCHAR(255) NOT NULL, Password VARCHAR(255) NOT NULL );

CREATE TABLE FlashCardDeck ( FlashCardGui VARCHAR(255) PRIMARY KEY, Gui VARCHAR(255), FOREIGN KEY (Gui) REFERENCES User(Gui) );
```


### Step 4: Run Docker Compose

With the `docker-compose.yml` and `init-mysql.sql` files in place, you can start your services by running the following command in the terminal from the directory containing your `docker-compose.yml`:

```
bash docker-compose up -d
```

This command will:

- Pull the latest MySQL and MongoDB images from Docker Hub.
- Initialize MySQL with the specified root user, database, and user credentials.
- Run the `init-mysql.sql` script to create the `OnlineFlashCard` database and the `User` and `FlashCardDeck` tables.
- Start the MySQL and MongoDB services in detached mode.

### Step 5: Verify the Setup

- **MySQL**: You can connect to your MySQL database using any MySQL client with the credentials specified in the `.env` file.
- **MongoDB**: You can connect to your MongoDB instance using a MongoDB client. The `FlashCardGui` will be the key for MongoDB records, but since MongoDB is schema-less, you'll need to ensure your application logic handles the `FlashCardGui` as the unique identifier for records.
