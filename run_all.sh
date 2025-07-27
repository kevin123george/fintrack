#!/bin/bash

echo "🔧 Activating Python virtual environment..."
source venv/bin/activate

# 1. Run stock_api.py (assumed to be a Flask or FastAPI server)
echo "🐍 Starting stock_api.py..."
nohup python stock_api.py > stock_api.log 2>&1 &

# Wait for Python API to start (adjust as needed)
sleep 3

# 2. Build Java backend
echo "📦 Building Java FinTrack backend..."
./gradlew bootJar

# 3. Run the built Spring Boot JAR
echo "🚀 Starting Java FinTrack backend..."
nohup java -jar build/libs/fintrack-0.0.1-SNAPSHOT.jar > backend.log 2>&1 &

# Wait for Java backend to start
sleep 5

# 4. Run CLI tool
echo "🖥️ Launching CLI tool..."
python cli_tool.py
