package se.hegardt.repository.sebastian

import groovy.transform.CompileStatic
import io.micronaut.data.annotation.Repository

@SuppressWarnings(['AbstractClassWithoutAbstractMethod'])
@Repository
@CompileStatic
abstract class TrackedMediaRepository implements ITrackedMediaRepository {
}
