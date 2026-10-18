package se.hegardt.service

import groovy.transform.CompileStatic
import jakarta.inject.Singleton
import se.hegardt.domain.sebastian.TrackedMedia
import se.hegardt.repository.sebastian.ITrackedMediaRepository

@Singleton
@CompileStatic
class MediaTrackerService implements IMediaTrackerService{

    private final ITrackedMediaRepository trackedMediaRepository

    MediaTrackerService(ITrackedMediaRepository trackedMediaRepository) {
        this.trackedMediaRepository = trackedMediaRepository
    }
    List<TrackedMedia> getAll() {
        return trackedMediaRepository.findAll()
    }
}
