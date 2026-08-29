pipeline {
    agent any

    triggers {
        cron('H 3 * * *')
    }

    stages {
        stage('Kodu Çek (Checkout)') {
            steps {
                checkout scm
            }
        }

        stage('Docker İmajını İnşa Et') {
            steps {
                // Windows kullandığın için 'bat' komutu kullanıyoruz
                sh 'docker build -t crm-automation .'
            }
        }

        stage('Testleri Koştur (Run)') {
            steps {
                // -e parametresi ile gizli API anahtarını konteynerin içine aktarıyoruz
                sh 'docker run --rm -e LLM_API_KEY="$LLM_API_KEY" crm-automation'
            }
        }
    }

    post {
    always {
        echo 'Pipeline işlemi tamamlandı!'
        publishHTML(target: [
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: '.',
            reportFiles: 'report.html',
            reportName: 'Otomasyon Raporu'
        ])
    }
    }
}