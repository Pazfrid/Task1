properties(
    [
        parameters(
            [string(defaultValue: "", name: 'text')]
            )

    ]
    )

node{
    stage("get sources"){
        // sh "env "
        git credentialsId: '98b78c62-fb2b-4f72-8241-3fb972a5b449', url: 'https://github.com/Pazfrid/Task1.git'
    }
    // archiveArtifacts artifacts: 'chiper.txt'

    stage("build"){
        sh "python3 Encrypt2.py ${params.text} > chiper.txt"
    }
    stage("deploy"){
        sh 'ls -la'
        sh 'curl -upaz:APAYgvTTr7FmvQ1ejSQkdzKF9Fw -T chiper.txt "http://172.17.0.3:8082/artifactory/Test1/chiper.txt"'
    }
}