# aaaa

mkdir -p ./github/workflows/
touch ./github/workflows/config.yml

language: java
after_success:

- mvn clean cobertura:cobertura
- mvn test
