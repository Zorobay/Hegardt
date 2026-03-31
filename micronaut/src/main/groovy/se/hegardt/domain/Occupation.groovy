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

@Entity
@CompileStatic
@EqualsAndHashCode(includes = ['id'])
class Occupation extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = 'occupation_seq')
    @SequenceGenerator(name = 'occupation_seq', sequenceName = 'occupation_seq', allocationSize = 1)
    Long id

    String notes

    @ManyToOne(cascade = CascadeType.ALL)
    @Nullable
    Location location

    @Embedded
    PartialDate date = new PartialDate()

    @PrePersist
    @PreUpdate
    void computeDates() {
        date?.computeDate()
    }
}
