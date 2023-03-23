plugins {
    kotlin("jvm") version "1.8.0"
    application
}

group = "com.github.leventarican"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    // latest version of kotlin dataframe: https://plugins.gradle.org/plugin/org.jetbrains.kotlinx.dataframe/0.9.1
    implementation("org.jetbrains.kotlinx:dataframe-core:0.9.1")
    testImplementation(kotlin("test"))
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(8)
}

application {
    mainClass.set("MainKt")
}