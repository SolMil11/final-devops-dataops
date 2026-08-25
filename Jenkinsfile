pipeline {
    agent any
    stages {
        stage('Validar Python') {
            steps {
                bat 'python --version'
            }
        }
        stage('Instalar dependencias') {
            steps {
                bat 'pip install pandas'
            }
        }
        stage('Ejecucion Extraccion Raw') {
            steps {
                echo 'Generando las 50 ordenes de compra para CIPSA...'
                bat 'python extract.py'
            }
        }
        stage('Ejecucion Transformacion Silver') {
            steps {
                echo 'Procesando y clasificando ordenes de compra...'
                bat 'python transform.py'
            }
        }
        stage('Validacion final') {
            steps {
                echo 'Pipeline ejecutado correctamente para CIPSA CIPTECH'
            }
        }
    }
}