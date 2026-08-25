pipeline {
    agent any
    stages {
        stage('1. Validar Entorno') {
            steps {
                bat 'python --version'
                bat 'pip install pandas'
            }
        }
        stage('2. Inicializacion') {
            steps {
                bat 'python initialize.py'
            }
        }
        stage('3. Extraccion Raw') {
            steps {
                bat 'python extract.py'
            }
        }
        stage('4. Perfilamiento y Calidad') {
            steps {
                bat 'python profile.py'
                bat 'python quality.py'
            }
        }
        stage('5. Transformacion Silver') {
            steps {
                bat 'python transform.py'
            }
        }
        stage('6. Publicacion Gold y Metricas') {
            steps {
                bat 'python publish.py'
                bat 'python metrics.py'
            }
        }
    }
}