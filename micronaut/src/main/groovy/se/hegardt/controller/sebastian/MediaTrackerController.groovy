package se.hegardt.controller.sebastian

import groovy.transform.CompileStatic
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import se.hegardt.domain.sebastian.TrackedMedia
import se.hegardt.dto.sebastian.TrackedMediaDto
import se.hegardt.service.IMediaTrackerService

@Controller('/sebastian/media_tracker')
@CompileStatic
class MediaTrackerController {

    private final IMediaTrackerService mediaTrackerService

    MediaTrackerController(IMediaTrackerService mediaTrackerService) {
        this.mediaTrackerService = mediaTrackerService
    }

    @Get('/getAll')
    HttpResponse<List<TrackedMediaDto>> getAll() {
        return HttpResponse.ok(mediaTrackerService.getAll()
            .sort { tmA, tmB -> tmB.earliestWatch.timestamp <=> tmA.earliestWatch.timestamp }
            .collect { TrackedMedia tm -> TrackedMediaDto.from(tm) })
    }
}
