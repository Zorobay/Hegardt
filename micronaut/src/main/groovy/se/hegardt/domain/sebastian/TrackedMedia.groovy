package se.hegardt.domain.sebastian

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import jakarta.persistence.CascadeType
import jakarta.persistence.Entity
import jakarta.persistence.EnumType
import jakarta.persistence.Enumerated
import jakarta.persistence.FetchType
import jakarta.persistence.GeneratedValue
import jakarta.persistence.GenerationType
import jakarta.persistence.Id
import jakarta.persistence.OneToMany
import jakarta.persistence.SequenceGenerator
import jakarta.persistence.Table
import se.hegardt.model.MediaType

import java.time.LocalDate

@Entity
@CompileStatic
@EqualsAndHashCode(includes=['id'])
@Table(name = 'tracked_media', schema = 'sebastian')
class TrackedMedia {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = 'tracked_media_seq')
    @SequenceGenerator(name = 'tracked_media_seq', sequenceName = 'tracked_media_seq', schema = 'sebastian', allocationSize = 1)
    Long id

    @Enumerated(EnumType.STRING)
    MediaType type

    String title
    LocalDate release_date
    Integer tmdb_id
    Float rating
    String posterPath

    @OneToMany(mappedBy = 'tracked_media', cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.EAGER)
    List<TrackedMediaWatch> watches = []

    TrackedMediaWatch getEarliestWatch() {
        return watches.sort{it.timestamp}.last
    }
}
