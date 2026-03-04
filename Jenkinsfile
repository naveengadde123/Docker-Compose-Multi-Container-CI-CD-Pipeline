pipeline {
    agent { label 'ubuntu-agent' }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/naveengadde123/Docker-Compose-Multi-Container-CI-CD-Pipeline'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }
    }
}