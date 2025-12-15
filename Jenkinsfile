pipeline {
    agent any

    parameters {
        string(
            name: 'VAR_STR',
            defaultValue: 'Valor por defecto',
            description: 'Parámetro string'
        )
        choice(
            name: 'VAR_CHOICE',
            choices: ['Primera opción', 'Segunda opción', 'Tercera opción'],
            description: 'Parámetro choice'
        )
        booleanParam(
            name: 'VAR_BOOL',
            defaultValue: true,
            description: 'Parámetro boolean'
        )
    }

    stages {

        stage('Primer pasito') {
            steps {
                sh 'echo "${VAR_STR}"'
            }
        }

        stage('Segundo pasito') {
            steps {
                sh 'echo "hola gente" > test.txt'
            }
        }

        stage('Tercer pasito') {
            steps {
                sh 'cat test.txt'
            }
        }

        stage('Preparar entorno Python') {
            steps {
                sh '''
                    echo "Creando entorno virtual..."
                    python3 -m venv venv
                    . venv/bin/activate
                    python --version
                '''
            }
        }

        stage('Ejecutar script Python') {
            steps {
                sh '''
                    . venv/bin/activate
                    python script.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente ✅'
        }
        failure {
            echo 'Pipeline falló ❌'
        }
    }
}
