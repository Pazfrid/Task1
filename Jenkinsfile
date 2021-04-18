properties(
    [
        parameters(
            [string(defaultValue: "", name: 'text')]
            )

    ]
    )

node{
    sh "env "
    echo params.text
    sh "echo 'Hello World'"
    sh "pwd"
    sh "ls -l"
    git credentialsId: '98b78c62-fb2b-4f72-8241-3fb972a5b449', url: 'https://github.com/Pazfrid/Task1.git'
    sh "python3 Encrypt2.py ${params.text}"
}