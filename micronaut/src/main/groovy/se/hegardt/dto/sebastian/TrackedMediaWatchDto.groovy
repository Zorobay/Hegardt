package se.hegardt.dto.sebastian

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.sebastian.TrackedMediaWatch

import java.time.OffsetDateTime

@Serdeable
@CompileStatic
class TrackedMediaWatchDto {

    OffsetDateTime timestamp

    static TrackedMediaWatchDto from(TrackedMediaWatch tmw) {
        return new TrackedMediaWatchDto(
            timestamp: tmw.timestamp
        )
    }
}
