package se.hegardt.dto.sebastian

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.sebastian.TrackedMedia
import se.hegardt.domain.sebastian.TrackedMediaWatch
import se.hegardt.model.MediaType

@Serdeable
@CompileStatic
class TrackedMediaDto {
    Long id
    String title
    Integer tmdb_id
    Float rating
    String posterPath
    MediaType type
    List<TrackedMediaWatchDto> watches = []

    static TrackedMediaDto from(TrackedMedia trackedMedia) {
        return new TrackedMediaDto(
            id: trackedMedia.id,
            title: trackedMedia.title,
            tmdb_id: trackedMedia.tmdb_id,
            rating: trackedMedia.rating,
            posterPath: trackedMedia.posterPath,
            type: trackedMedia.type,
            watches: trackedMedia.watches.collect { TrackedMediaWatch tmw -> TrackedMediaWatchDto.from(tmw) }
        )
    }
}
