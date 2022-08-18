*** Settings ***
Library           JavaRemote            MyKeywords
Suite Teardown    Stop remote server

*** Test Cases ***
First
    Say Hello    Robot Framework