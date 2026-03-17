package se.hegardt.model

import groovy.transform.CompileStatic

@CompileStatic
enum LocationFetchStatus {
    FETCHED_WITH_SUCCESS,
    FETCHED_WITH_ERRORS,
    AWAITING
}
