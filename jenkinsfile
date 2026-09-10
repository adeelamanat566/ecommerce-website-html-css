pipeline {
    agent any{
        stages{
            stage(buil){
                step{
                    sh 'docker compose config'
                    sh 'docker compose build -t '
                }
            }
            stage(test){
                step{
                    input(
                        message: 'do you wantcontinues?',
                        ok: 'yes we should'
                    )
                }
            }
            stage(deploy){
                step{
                    sh 'docker compose run -d'
                }
            }
        }
    }
    post{
        always{
            echo 'finised oipli'
            
        }
        success{
            echo 'success'
        }
        failure{
            echo 'failure'
        }




    }

}

