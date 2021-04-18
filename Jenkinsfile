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
    sh "python3 Encrypt2.py ${params.text}"
}