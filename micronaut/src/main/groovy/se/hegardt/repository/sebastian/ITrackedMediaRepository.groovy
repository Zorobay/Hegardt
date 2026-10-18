package se.hegardt.repository.sebastian

import groovy.transform.CompileStatic
import io.micronaut.data.jpa.repository.JpaRepository
import se.hegardt.domain.sebastian.TrackedMedia

@CompileStatic
interface ITrackedMediaRepository extends JpaRepository<TrackedMedia, Long> {

}
