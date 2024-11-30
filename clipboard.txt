How to Run the Service

	1.	Clone the Repository:

git clone https://github.com/Cdaprod/local-docker-transcription-service.git
cd local-docker-transcription-service


	2.	Set Environment Variables:
Create a .env file in the root directory:

RABBITMQ_USER=guest
RABBITMQ_PASS=guest
OPENAI_API_KEY=your_openai_api_key


	3.	Build and Run the Containers:

docker-compose up --build


	4.	Test the APIs:
	•	Transcription:

curl -X POST -F "audio=@path/to/audio.mp3" http://localhost:5000/transcribe


	•	Summarization:

curl -X POST -H "Content-Type: application/json" \
  -d '{"transcript": "Your transcript text here"}' \
  http://localhost:5000/summarize

Next Steps

1.	Deploy to Docker Hub or GitHub:
Push the repository and enable CI/CD for automatic builds.
2.	Integrate with RTMP Event Broker:
Use RabbitMQ to queue events from the RTMP server for transcription and summarization.