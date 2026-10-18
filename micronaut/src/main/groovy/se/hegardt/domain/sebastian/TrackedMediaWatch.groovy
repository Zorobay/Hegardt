package se.hegardt.domain.sebastian

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import jakarta.persistence.Entity
import jakarta.persistence.EnumType
import jakarta.persistence.Enumerated
import jakarta.persistence.FetchType
import jakarta.persistence.GeneratedValue
import jakarta.persistence.GenerationType
import jakarta.persistence.Id
import jakarta.persistence.ManyToOne
import jakarta.persistence.SequenceGenerator
import jakarta.persistence.Table
import se.hegardt.model.MediaType

import java.time.LocalDate
import java.time.LocalDateTime
import java.time.OffsetDateTime

@Entity
@CompileStatic
@EqualsAndHashCode(includes=['id'])
@Table(name = 'tracked_media_watch', schema = 'sebastian')
class TrackedMediaWatch {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = 'tracked_media_watch_seq')
    @SequenceGenerator(name = 'tracked_media_watch_seq', sequenceName = 'tracked_media_watch_seq', schema = 'sebastian', allocationSize = 1)
    Long id

    @ManyToOne(fetch = FetchType.LAZY)
    TrackedMedia tracked_media

    OffsetDateTime timestamp
}
