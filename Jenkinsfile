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
                sh 'docker build -t crm-automation .'
            }
        }

        stage('Testleri Koştur (Run)') {
            steps {
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
        emailext (
            subject: "Jenkins Otomasyon Sonucu: ${currentBuild.currentResult} - Build #${env.BUILD_NUMBER}",
            body: """
                <h2>CRM Otomasyon Koşum Özeti</h2>
                <p>Test süreci tamamlandı. Sistemin son durumu aşağıdadır:</p>
                <p><strong>Sonuç:</strong> ${currentBuild.currentResult}</p>
                <br>
                <p>Detaylı HTML raporunu incelemek için aşağıdaki bağlantıya tıklayın:</p>
                <p><a href="${env.BUILD_URL}Otomasyon_20Raporu/"><strong>Jenkins Raporunu Görüntüle</strong></a></p>
            """,
            to: "bayrakfatih400@gmail.com",
            mimeType: 'text/html'
        )
    }
    }
}