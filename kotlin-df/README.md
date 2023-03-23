
Data wrangling with Kotlin Dataframe.

Input data is a csv file with salaries of Software Developers in Turkiye `./TR-maaslar-2023.csv`.

# result snippet
```
     Seviye count
 0   Junior   446
 1      Mid   375
 2   Senior   299
 3 Tanımsız    44
```

# build and run

```bash
gradle clean
gradle build
gradle run
# or
java -cp app/build/classes/kotlin/main com.github.leventarican.salary.AppKt
```

# development setup

- Kotlin Dataframe 0.9.1
- Gradle 8.0.2
- Kotlin 1.8.10
- Java 17 (Temurin)
- IntelliJ IDEA 2022.3.3
- GNU bash 5.1