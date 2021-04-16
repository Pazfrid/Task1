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
    sh "python3 Encrypt.py"
}