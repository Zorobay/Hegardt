package se.hegardt.domain

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import jakarta.annotation.Nullable
import jakarta.persistence.CascadeType
import jakarta.persistence.Embedded
import jakarta.persistence.Entity
import jakarta.persistence.GeneratedValue
import jakarta.persistence.GenerationType
import jakarta.persistence.Id
import jakarta.persistence.ManyToOne
import jakarta.persistence.PrePersist
import jakarta.persistence.PreUpdate
import jakarta.persistence.SequenceGenerator
import se.hegardt.domain.abstr.BaseEntity

@Entity()
@CompileStatic
@EqualsAndHashCode(includes = ['id'])
class LifeEvent extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "life_event_seq")
    @SequenceGenerator(name = "life_event_seq", sequenceName = "life_event_seq", allocationSize = 1)
    Long id

    String notes

    @Embedded
    PartialDate date = new PartialDate()

    @Nullable
    @ManyToOne(cascade = CascadeType.ALL)
    Location location

    @PrePersist
    @PreUpdate
    void computeDates() {
        date?.computeDate()
    }
}
