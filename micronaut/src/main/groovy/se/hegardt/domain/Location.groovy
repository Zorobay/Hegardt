package se.hegardt.domain

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import jakarta.annotation.Nullable
import jakarta.persistence.Entity
import jakarta.persistence.EnumType
import jakarta.persistence.Enumerated
import jakarta.persistence.GeneratedValue
import jakarta.persistence.GenerationType
import jakarta.persistence.Id
import jakarta.persistence.SequenceGenerator
import se.hegardt.domain.abstr.BaseEntity
import se.hegardt.model.LocationFetchStatus

@Entity
@CompileStatic
@EqualsAndHashCode(includes = ['id'])
class Location extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = 'location_seq')
    @SequenceGenerator(name = 'location_seq', sequenceName = 'location_seq', allocationSize = 1)
    Long id

    String city = ''
    String country = ''
    String region = ''
    String notes = ''

    @Nullable
    Double latitude

    @Nullable
    Double longitude

    @Enumerated(EnumType.STRING)
    LocationFetchStatus fetchStatus
}
