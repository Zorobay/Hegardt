package se.hegardt.service

import groovy.transform.CompileStatic
import se.hegardt.domain.sebastian.TrackedMedia

@CompileStatic
interface IMediaTrackerService {

    List<TrackedMedia> getAll();
}
