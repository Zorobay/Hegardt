package se.hegardt.domain

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import jakarta.annotation.Nullable
import jakarta.persistence.*
import se.hegardt.domain.abstr.BaseEntity

@Entity
@CompileStatic
@EqualsAndHashCode(includes = ['id'])
class Occupation extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "occupation_seq")
    @SequenceGenerator(name = "occupation_seq", sequenceName = "occupation_seq", allocationSize = 1)
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
