pipeline {
    agent any

    parameters {
        string(name: 'VAR_STR', defaultValue: 'Valor por defecto', description: 'lo que sea')
        choice(name: 'VAR_CHOICE', choices: ['Primera opción', 'Segunda opción', 'Tercera opción'], description: 'lo que sea')
        booleanParam(name: 'VAR_BOOL', defaultValue: true, description: 'lo que sea')
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

        stage('Ejecutar script Python') {
            steps {
                sh 'python3 script.py'
            }
        }
    }
}
