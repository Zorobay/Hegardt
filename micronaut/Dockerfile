FROM eclipse-temurin:21-jdk-jammy AS build
WORKDIR /app

# Copy Gradle wrapper and dependency files first for layer caching
COPY gradlew .
COPY gradle/ gradle/
COPY build.gradle .
COPY settings.gradle .
COPY gradle.properties .

# Download dependencies (cached unless build files change)
RUN chmod +x gradlew && ./gradlew dependencies --no-daemon -q || true

# Copy source and build
COPY src/ src/
RUN ./gradlew assemble --no-daemon -q

# ── Runtime image ─────────────────────────────────────────────────────────────
FROM eclipse-temurin:21-jre-jammy
WORKDIR /app

# Non-root user for security
RUN addgroup --system hegardt && adduser --system --ingroup hegardt hegardt

COPY --from=build /app/build/libs/*-all.jar app.jar

RUN chown hegardt:hegardt app.jar
USER hegardt

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
