pipeline {
    agent {
        label 'agent_node'
    }

    environment {
        VENV = 'venv'
    }

    stages {

        stage('Build Application') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python3 -m unittest discover -s . -p "test_*.py"
                '''
            }
        }

        stage('Staging') {
            steps {
                sh '''
                    if [ -f flask_app.pid ]; then
                    kill -9 $(cat flask_app.pid) || true
                    rm flask_app.pid
                    fi

                    . venv/bin/activate

                    # Start Gunicorn using bash and disown to prevent Jenkins from killing it
                    bash -c "nohup gunicorn -b 0.0.0.0:5000 app:app > flask.log 2>&1 & echo \$! > flask_app.pid && disown"
                '''
            }
        }

        stage('Prod') {
            steps {
                sh '''
                    if [ -f flask_app.pid ]; then
                    kill -9 $(cat flask_app.pid) || true
                    rm flask_app.pid
                    fi

                    . venv/bin/activate

                    # Start Gunicorn using bash and disown to prevent Jenkins from killing it
                    bash -c "nohup gunicorn -b 0.0.0.0:8090 app:app > flask.log 2>&1 & echo \$! > flask_app.pid && disown"
                '''
            }
        }
    }
    post {
        success {
            echo '✅ Build and Deployment Successful!'
        }
        failure {
            echo '❌ Build failed or tests did not pass.'
        }
    }
}
