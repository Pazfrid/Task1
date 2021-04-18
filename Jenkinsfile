properties(
    [
        parameters(
            [string(defaultValue: "", name: 'text')]
            )

    ]
    )

node{
    sh "env "
    git credentialsId: '98b78c62-fb2b-4f72-8241-3fb972a5b449', url: 'https://github.com/Pazfrid/Task1.git'
    sh "python3 Encrypt2.py ${params.text} > chiper.txt"
    archiveArtifacts artifacts: 'chiper.txt'
}